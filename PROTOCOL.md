# Roster Construction Protocol — RCP v1.0

**Issued 11 September 2026.** Mandatory for every draft roster entering a Revelations Index workbook.

---

## The error this prevents

Sixteen roster errors were found across three NHL cohorts, plus two in NFL 2022 and one in NFL 2020. **Every one occurred at a slot that changed hands in a trade. Not one occurred at a pick that stayed with its original team.**

The cause is a single reproducible method failure:

> Rosters were built by recalling **which team ended up with which player**, then assigning that player to the team's original slot.

When a pick is traded, the team and the slot separate. Building by team puts the player in the wrong slot — and because the trading team usually also *received* a pick, the error propagates as a transposition. Picks 19/22/24 in NHL 2020 rotated three ways. Picks 20/22 in NHL 2021 swapped. Bystedt moved sixteen slots in NHL 2022.

**The slot is the record. The team is an attribute of the slot. The player is an attribute of the slot.**

---

## Rule 1 — Transcribe by slot, never by team

Read the source top to bottom, slot 1 to slot N. For each slot, record in this order:

`pick number → player selected at that number → team that made the selection`

Never begin from a team name. Never begin from a player name. If you find yourself asking "where did Team X pick?", stop — that question produces the error.

## Rule 2 — One named, dated, slot-ordered source

The source must present selections **in slot order**. Acceptable: official league draft records, Pro-Football-Reference, myNHLdraft, full-draft trackers that list every pick sequentially.

Unacceptable as a primary source: team-by-team summaries, "best available" retrospectives, memory, or any prior Revelations workbook.

Record the source name and retrieval date in the sheet.

## Rule 3 — Second source for every traded slot

A slot annotated with a trade in the primary source gets confirmed against a second independent source before it is accepted. Traded slots are where 100% of errors occurred; they get 100% of the scrutiny.

## Rule 4 — Forfeited and vacant slots are recorded, not skipped

A forfeited pick occupies its slot number with no player. Do not renumber. Do not compress. NHL 2021 pick 11 is vacant and slot 12 is still slot 12.

## Rule 5 — Never annotate a player with a later trade

`Isaac Howard (traded)` is not a roster entry. A draft record captures one moment. Where a player went afterward belongs in notes, never in the name field. The presence of a "(traded)" annotation is itself evidence the roster was built by the wrong method.

## Rule 6 — Run the verifier before scoring

No roster enters a scoring pass until it passes every check below.

---

## Mandatory verification checks

| # | Check | Fails when |
|---|---|---|
| 1 | **Slot count** | Player count ≠ expected selections for that year |
| 2 | **Slot continuity** | Slot numbers are not 1…N with no gaps |
| 3 | **Within-year uniqueness** | Any player appears twice in one cohort |
| 4 | **Cross-year uniqueness** | Any player appears as a first-rounder in two different drafts |
| 5 | **Round contamination** | Any listed player was actually selected in round 2 or later |
| 6 | **Forfeit handling** | A known forfeited slot holds a player, or is missing entirely |
| 7 | **Annotation cleanliness** | Any name field contains "(traded)", "(via …)", or similar |
| 8 | **Outcome alignment** | A slot carries outcome data but no player, or vice versa |

Checks 1–4 and 6–8 run from the roster alone. Check 5 requires the source.

## Expected first-round counts

| League | Rule | Notes |
|---|---|---|
| NFL | 32 | Forfeitures possible; verify per year |
| NBA | 30 | Stable |
| NHL | One per team, less forfeits | **2020 = 31** (31 teams). **2021 = 31** (32 teams, Arizona forfeited #11). 2022–2025 = 32 |
| MLB | Varies | Competitive Balance Round A sits between rounds 1 and 2 — decide inclusion explicitly and apply it uniformly |

The NHL line is where the workbook README was wrong: it attributed 2020's 31 picks to the Arizona forfeit. 2020 had 31 picks because the league had 31 teams. Arizona's penalty cost a 2020 **second**-round pick and the **2021 first**-round pick.

---

## Correction workflow for an existing roster

1. Retrieve a slot-ordered source. Record name and date.
2. Transcribe slot → player independently. Do not read the existing roster while transcribing.
3. Diff the two lists programmatically, by slot.
4. For each mismatch, confirm the correct entry against a second source.
5. Run all eight checks on the corrected roster.
6. Record the error count and the corrections in a dated log.
7. **Re-key the outcome data.** A wrong player in a slot means the outcome recorded there belongs to the wrong person. Outcomes follow the player, not the slot.

Step 7 is the one most easily missed. Helge Grans's outcome sat in Mavrik Bourque's slot; Cameron Lund's sat in Filip Bystedt's. Correcting the name without re-keying the outcome converts a visible error into an invisible one.

---

*Revelations Analytics · RCP v1.0 · Applies to NFL, NBA, NHL and MLB workbooks without exception*
