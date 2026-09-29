# Outcome Data — Provenance

Every outcome value in `nfl_2020_outcomes.csv` and `nfl_2022_outcomes.csv` comes from a single source, applied uniformly.

| Field | Definition | Source |
|---|---|---|
| `wav` | Weighted career Approximate Value through the 2025 season | Pro-Football-Reference draft listing |
| `pro_bowls` | Pro Bowl selections to date | Pro-Football-Reference draft listing |
| `all_pro_1st` | First-team All-Pro selections to date | Pro-Football-Reference draft listing |
| `seasons_started` | Seasons as a primary starter | Pro-Football-Reference draft listing |

**Retrieved:** 11 September 2026
**NFL 2020:** `pro-football-reference.com/years/2020/draft.htm` — page revision 10 Sep 2026
**NFL 2022:** `pro-football-reference.com/years/2022/draft.htm` — page revision 9 Sep 2026

## Why one source rather than per-record citation

Every value on both sheets is read from a single published table per cohort. A per-record citation would repeat the same URL 64 times. The stronger guarantee is that a referee can open two pages and check all 64 rows against them directly.

## Snapshot stability

Pro-Football-Reference lists every 2020 first-rounder's final season as 2025, so the 2026 season had not yet accrued Approximate Value for these cohorts at retrieval. "Through the 2025 season" is therefore stable as of the retrieval date. It will not remain so: these values move as careers continue, and any future re-run should record its own retrieval date.

## Corrections made against this source

Verification against Pro-Football-Reference corrected values that had been carried in project documents:

- **NFL 2020:** 11 of 32 Pro Bowl / All-Pro records were wrong in the source workbook. Errors ran in both directions — Burrow recorded at 2 Pro Bowls against an actual 3; Terrell and Aiyuk at 1 against an actual 0.
- **NFL 2022:** 13 of 32 `wav` values were wrong in the original scoring pass. Olave carried 24 against an actual 27; Jermaine Johnson II carried 23 against an actual 19.
- **NFL 2020 pick order:** Tristan Wirfs and Javon Kinlaw were transposed. PFR places Wirfs at 13 and Kinlaw at 14.

Full log in `../DATA_PROVENANCE.md`.
