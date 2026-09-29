# Exclusion Policy

Written before scoring. Applied uniformly to every cohort in every league.

## 1 — Non-sporting termination

A selection whose career ended for reasons unrelated to play is excluded from hit-rate denominators and from all reported correlations. The row is retained and marked; it is never deleted.

| Cohort | Player | Pick | Reason |
|---|---|---|---|
| NFL 2020 | Henry Ruggs | 12 | Removed from the league on non-sporting grounds |
| NFL 2020 | Jeff Gladney | 31 | Died 2022 — outcome classification not applicable |
| NHL 2020 | Rodion Amirov | 15 | Died 2023 — outcome classification not applicable |

## 2 — Unsigned selection

A selection that does not sign with the drafting club is retained at its slot, marked `EXCLUDED-UNSIGNED`, carries no outcome data, and is removed from hit-rate denominators. Where the player re-enters a later draft, his outcome attaches solely to the slot at which he signed.

Retained rather than deleted: an unsigned first-rounder is a failed selection. Deleting the slot removes a bad outcome from the market's record and inflates the board's apparent hit rate. Since the index is measured *against* draft slot, anything that flatters the board distorts the comparison.

Applies to MLB 2021 pick 10, Kumar Rocker. His outcome attaches to MLB 2022 pick 3, where he signed.

## 3 — Forfeited pick

A forfeited selection occupies its slot number with no player. Slots are not renumbered or compressed. Where the forfeit falls at the end of a round, the round is simply shorter.

| Cohort | Effect |
|---|---|
| NFL 2023 | Miami forfeited — Round 1 holds 31 picks |
| NHL 2021 | Arizona forfeited pick 11 — slot vacant, 31 players |
| MLB 2020, 2021 | Houston forfeited — Round 1 holds 29 picks each year |

## 4 — Round boundary

Round 1 is the round as the league defines it. Competitive Balance picks, compensation picks, and any supplemental round are excluded from every cohort in every league. The count is read from the draft record for each year, never assumed.

## 5 — Unscored selection

A selection present in the roster but never scored is retained, marked `NOT-SCORED`, and omitted from correlations. It is disclosed rather than filled: scoring a player whose outcome is already known would contaminate a cohort whose remaining rows were hashed before outcomes were consulted.

Applies to NFL 2022 pick 21, Trent McDuffie.

---

## Effect on the cohorts in this repository

| Cohort | Rows | Scored | Excluded | Basis |
|---|---|---|---|---|
| NFL 2020 | 32 | 30 | 2 | Rule 1 |
| NFL 2022 | 32 | 31 | 1 | Rule 5 |

Reported correlations for NFL 2020 are given both ways — all 32 and exclusions-applied — so a referee can see exactly what the policy costs.
