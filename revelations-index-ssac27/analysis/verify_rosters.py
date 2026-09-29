"""
RA Roster Verifier — implements Roster Construction Protocol v1.0
Run on every draft roster before it enters a scoring pass.

Usage:
    v = RosterVerifier("NHL", 2021, expected=31, forfeits={11})
    v.load({1:"Owen Power", 2:"Matthew Beniers", ...})   # slot -> player, None for forfeit
    v.cross_check(other_cohorts)                          # {(league,year): {slot: player}}
    v.report()
"""
import re, sys

BAD_ANNOTATION = re.compile(r"\((traded|via|from)\b", re.I)

EXPECTED = {
    "NFL": {y: 32 for y in range(2020, 2026)},
    "NBA": {y: 30 for y in range(2020, 2026)},
    # NHL 2020: 31 teams. NHL 2021: 32 teams less Arizona forfeit at #11.
    "NHL": {2020: 31, 2021: 31, 2022: 32, 2023: 32, 2024: 32, 2025: 32},
}
KNOWN_FORFEITS = {("NHL", 2021): {11}}


class RosterVerifier:
    def __init__(self, league, year, expected=None, forfeits=None, source=None, retrieved=None):
        self.league, self.year = league, year
        self.expected = expected if expected is not None else EXPECTED.get(league, {}).get(year)
        self.forfeits = forfeits if forfeits is not None else KNOWN_FORFEITS.get((league, year), set())
        self.source, self.retrieved = source, retrieved
        self.roster, self.failures, self.passes = {}, [], []

    def load(self, roster):
        self.roster = dict(roster)
        return self

    def _fail(self, n, msg): self.failures.append(f"CHECK {n} FAILED — {msg}")
    def _pass(self, n, msg): self.passes.append(f"check {n} pass — {msg}")

    def run(self, other_cohorts=None, round2_names=None):
        r = self.roster
        players = [p for p in r.values() if p]
        slots = sorted(r)

        # 1 slot count
        if self.expected is not None and len(players) != self.expected:
            self._fail(1, f"{len(players)} players, expected {self.expected}")
        else:
            self._pass(1, f"{len(players)} players")

        # 2 slot continuity
        span = list(range(1, max(slots) + 1)) if slots else []
        if slots != span:
            self._fail(2, f"slots not contiguous 1..{max(slots) if slots else 0}")
        else:
            self._pass(2, f"slots 1..{max(slots)} contiguous")

        # 3 within-year uniqueness
        dup = sorted({p for p in players if players.count(p) > 1})
        if dup: self._fail(3, f"duplicate within cohort: {dup}")
        else: self._pass(3, "no within-cohort duplicates")

        # 4 cross-year uniqueness
        if other_cohorts:
            clash = []
            for (lg, yr), other in other_cohorts.items():
                if (lg, yr) == (self.league, self.year): continue
                for p in players:
                    if p in [x for x in other.values() if x]:
                        clash.append(f"{p} also in {lg} {yr}")
            if clash: self._fail(4, "; ".join(clash))
            else: self._pass(4, "no cross-cohort duplicates")

        # 5 round contamination
        if round2_names:
            bad = sorted(set(players) & set(round2_names))
            if bad: self._fail(5, f"not first-round selections: {bad}")
            else: self._pass(5, "no round-2+ contamination")

        # 6 forfeits
        bad = []
        for f in self.forfeits:
            if f not in r: bad.append(f"slot {f} missing entirely")
            elif r[f] is not None: bad.append(f"slot {f} holds '{r[f]}' but was forfeited")
        vac = [s for s, p in r.items() if p is None and s not in self.forfeits]
        if vac: bad.append(f"unexpected vacant slots: {vac}")
        if bad: self._fail(6, "; ".join(bad))
        else: self._pass(6, f"forfeits correct {sorted(self.forfeits) or '(none)'}")

        # 7 annotation cleanliness
        dirty = sorted(p for p in players if BAD_ANNOTATION.search(p))
        if dirty: self._fail(7, f"trade annotations in name field: {dirty}")
        else: self._pass(7, "name fields clean")

        # 8 provenance
        if not self.source or not self.retrieved:
            self._fail(8, "source name and retrieval date not recorded")
        else:
            self._pass(8, f"source: {self.source}, retrieved {self.retrieved}")
        return self

    def report(self):
        ok = not self.failures
        print(f"\n{'='*62}\n{self.league} {self.year} — RCP v1.0 VERIFICATION\n{'='*62}")
        for p in self.passes: print("  " + p)
        for f in self.failures: print("  !! " + f)
        print(f"\n  RESULT: {'PASS — cleared for scoring' if ok else 'FAIL — do not score'}")
        return ok


def diff_by_slot(workbook, source):
    """Slot-keyed diff. Returns (errors, wrongly_present, wrongly_absent)."""
    errs = [(s, workbook.get(s), source.get(s))
            for s in sorted(set(workbook) | set(source))
            if workbook.get(s) != source.get(s)]
    wp = sorted({p for p in workbook.values() if p} - {p for p in source.values() if p})
    wa = sorted({p for p in source.values() if p} - {p for p in workbook.values() if p})
    return errs, wp, wa


if __name__ == "__main__":
    # self-test: a roster with every defect must fail every applicable check
    bad = {1: "A", 2: "A", 3: "B (traded)", 5: "C"}
    v = RosterVerifier("NHL", 2021, expected=31, forfeits={11}).load(bad).run()
    assert len(v.failures) >= 5, "verifier failed to catch seeded defects"
    good = {i: f"P{i}" for i in range(1, 33)}
    good[11] = None
    v2 = RosterVerifier("NHL", 2021, source="test", retrieved="2026-09-11").load(good).run()
    assert not v2.failures, f"clean roster wrongly failed: {v2.failures}"
    print("verifier self-test: PASS (catches seeded defects, clears a clean roster)")
