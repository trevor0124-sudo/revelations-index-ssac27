#!/usr/bin/env python3
"""
Revelations Index — reproduces every correlation reported in the SSAC27 submission.

Reads only from cohorts/ and outcomes/. Self-tests before reporting and aborts
rather than print an unverified number. Cross-checks its own Spearman
implementation against scipy.stats.spearmanr when scipy is available.

    python analysis/correlations.py
    diff <(python analysis/correlations.py) analysis/EXPECTED_OUTPUT.txt
"""
import csv, os, sys, statistics as st

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEIGHTS = [("CP", 0.34), ("AF", 0.23), ("HC", 0.18), ("AP", 0.15), ("DC", 0.10)]


# ----------------------------------------------------------------- statistics
def spearman(x, y):
    """Rank correlation, tie-averaged. Composites rounded to 6dp before ranking:
    float association order can otherwise conceal genuine ties and move the
    third decimal."""
    n = len(x)
    if n != len(y) or n < 3:
        raise ValueError("need equal-length series of at least 3")

    def ranks(v):
        v = [round(t, 6) for t in v]
        order = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r

    rx, ry = ranks(x), ranks(y)
    mx, my = st.mean(rx), st.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    if den == 0:
        raise ValueError("zero variance")
    return num / den


def self_test():
    cases = [(([1, 2, 3], [10, 20, 30]), 1.0),
             (([1, 2, 3], [30, 20, 10]), -1.0),
             (([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]), 0.8),
             (([1, 1, 2, 3], [1, 2, 2, 4]), 0.8333333)]
    for (a, b), want in cases:
        got = spearman(a, b)
        assert abs(got - want) < 1e-6, f"self-test failed: {a},{b} -> {got}, want {want}"
    try:
        from scipy.stats import spearmanr
    except ImportError:
        return "spearman self-test: PASS (4 cases; scipy absent, cross-check skipped)"
    worst = 0.0
    for (a, b), _ in cases:
        worst = max(worst, abs(spearman(a, b) - spearmanr(a, b).statistic))
    assert worst < 1e-9, f"scipy disagreement {worst:.2e}"
    return f"spearman self-test: PASS (4 cases; scipy agreement to {worst:.1e})"


# ----------------------------------------------------------------------- data
def load(year):
    cohort = os.path.join(ROOT, "cohorts", f"nfl_{year}_r1.csv")
    outcome = os.path.join(ROOT, "outcomes", f"nfl_{year}_outcomes.csv")
    out = {r["player"]: r for r in csv.DictReader(open(outcome))}
    rows = []
    for r in csv.DictReader(open(cohort)):
        if r["status"].startswith("NOT-SCORED"):
            continue
        o = out[r["player"]]
        rows.append(dict(
            pick=int(r["pick"]), player=r["player"], status=r["status"],
            final=float(r["Final"]) if r.get("Final") else None,
            CGI=float(r["CGI"]) if r.get("CGI") else None,
            IRI=float(r["IRI"]) if r.get("IRI") else None,
            wav=int(o["wav"]), pb=int(o["pro_bowls"]),
            ap1=int(o["all_pro_1st"]), st=int(o["seasons_started"]),
            **{k: float(r[k]) for k, _ in WEIGHTS}))
    return rows


def ri(d, keep=None):
    keep = keep or [k for k, _ in WEIGHTS]
    tot = sum(w for k, w in WEIGHTS if k in keep)
    return sum(w * d[k] for k, w in WEIGHTS if k in keep) / tot


def fmt(v):
    return f"{v:+.3f}"


# --------------------------------------------------------------------- report
def report(rows, label, excluded=False):
    if excluded:
        rows = [d for d in rows if d["status"] == "scored"]
    print(f"\n{label}  ·  n = {len(rows)}")
    print(f"  {'outcome measure':24}{'RI':>9}{'4-pillar':>10}{'slot':>9}{'edge':>8}")
    measures = [("wAV", lambda d: d["wav"]),
                ("Pro Bowls", lambda d: d["pb"]),
                ("Pro Bowls + 2x All-Pro", lambda d: d["pb"] + 2 * d["ap1"]),
                ("Seasons as starter", lambda d: d["st"])]
    wins = 0
    for name, f in measures:
        y = [f(d) for d in rows]
        if len(set(y)) < 3:
            print(f"  {name:24}{'n/a — insufficient variance':>36}")
            continue
        a = spearman([ri(d) for d in rows], y)
        b = spearman([ri(d, ["CP", "AF", "HC", "AP"]) for d in rows], y)
        c = spearman([-d["pick"] for d in rows], y)
        wins += (a - c) > 0
        print(f"  {name:24}{fmt(a):>9}{fmt(b):>10}{fmt(c):>9}{fmt(a - c):>8}")
    y = [d["wav"] for d in rows]
    print(f"  pillars vs wAV: " + "  ".join(
        f"{k} {fmt(spearman([d[k] for d in rows], y))}" for k, _ in WEIGHTS))
    print(f"  RI beats draft slot on {wins}/4 measures")
    return wins


def main():
    print("=" * 74)
    print("REVELATIONS INDEX — REPRODUCIBLE CORRELATIONS")
    print("=" * 74)
    print(self_test())
    print("\nOutcome measure: weighted career Approximate Value through the 2025 season,")
    print("Pro-Football-Reference, retrieved after each score file was hashed.")
    print("Draft slot is sign-flipped: positive means the board ordered correctly.")

    r20, r22 = load(2020), load(2022)
    assert len(r20) == 32, f"2020 cohort should hold 32 scored rows, got {len(r20)}"
    assert len(r22) == 31, f"2022 cohort should hold 31 scored rows, got {len(r22)}"
    print(f"\ncohorts loaded: 2020 n={len(r20)} · 2022 n={len(r22)} (Trent McDuffie unscored)")

    report(r20, "NFL 2020 — all 32 picks (in-sample: weights and bands derived here)")
    report(r20, "NFL 2020 — exclusion policy applied", excluded=True)
    report(r22, "NFL 2022 — held out of derivation; not blind")

    print("\n" + "=" * 74)
    print("Sub-index check (2020 only — CGI and IRI were scored for that cohort)")
    y = [d["wav"] for d in r20]
    base = spearman([ri(d) for d in r20], y)
    adj = spearman([ri(d) + d["CGI"] - d["IRI"] for d in r20], y)
    print(f"  five-pillar RI                {fmt(base)}")
    print(f"  Final Score = RI + CGI - IRI  {fmt(adj)}   cost {fmt(adj - base)}")
    print("=" * 74)


if __name__ == "__main__":
    sys.exit(main())
