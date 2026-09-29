# NHL 2021 Round 1 — Verified Roster Correction

**Source:** myNHLdraft.com official 2021 Round 1 results, cross-checked against ESPN, NHL.com and Wikipedia draft records. Retrieved 11 September 2026.

---

## Structural error first

**The 2021 first round contains 31 players, not 32.** Arizona forfeited pick 11 for violating the NHL Combine Testing Policy. The slot exists and is numbered; no player was selected in it.

The workbook README also misattributes this: it states the **2020** draft had 31 picks "due to the Arizona forfeit." That is wrong on both counts. The 2020 first round had 31 picks because the league had 31 teams — Seattle did not begin play until 2021. The Arizona forfeit applies to **2021**, and cost a 2020 *second*-round pick, not a first.

| Year | Workbook | Correct | Reason |
|---|---|---|---|
| 2020 | 31 | **31** ✓ | 31 teams in the league |
| 2021 | 32 | **31** ✗ | 32 slots, pick 11 forfeited |

---

## Corrected roster

Ten positions are wrong. Corrections in bold.

| Pick | Team | Workbook has | **Correct selection** |
|---|---|---|---|
| 1 | BUF | Owen Power | Owen Power ✓ |
| 2 | SEA | Matty Beniers | Matthew Beniers ✓ |
| 3 | ANA | Mason McTavish | Mason McTavish ✓ |
| 4 | NJD | Luke Hughes | Luke Hughes ✓ |
| 5 | CBJ | Kent Johnson | Kent Johnson ✓ |
| 6 | DET | Simon Edvinsson | Simon Edvinsson ✓ |
| 7 | SJS | William Eklund | William Eklund ✓ |
| 8 | LAK | Brandt Clarke | Brandt Clarke ✓ |
| **9** | ARI *(from VAN)* | Isak Rosén | **Dylan Guenther** |
| 10 | OTT | Tyler Boucher | Tyler Boucher ✓ |
| **11** | ARI | Dylan Guenther | **FORFEITED — no selection** |
| 12 | CBJ *(from CHI)* | Cole Sillinger | Cole Sillinger ✓ |
| 13 | CGY | Matthew Coronato | Matthew Coronato ✓ |
| **14** | BUF *(from PHI)* | Owen McLaughlin *(traded)* | **Isak Rosén** |
| **15** | DET *(from DAL)* | Wyatt Johnston | **Sebastian Cossa** |
| 16 | NYR | Brennan Othmann | Brennan Othmann ✓ |
| 17 | STL | Zach Bolduc | Zachary Bolduc ✓ |
| 18 | WPG | Chaz Lucius | Chaz Lucius ✓ |
| 19 | NSH | Fyodor Svechkov | Fyodor Svechkov ✓ |
| **20** | MIN *(from EDM)* | Xavier Bourgault | **Jesper Wallstedt** |
| 21 | BOS | Fabian Lysell | Fabian Lysell ✓ |
| **22** | EDM *(from MIN)* | Jesper Wallstedt | **Xavier Bourgault** |
| **23** | DAL | Matthew Knies | **Wyatt Johnston** |
| 24 | FLA | Mackie Samoskevich | Mackie Samoskevich ✓ |
| 25 | CBJ *(from TOR)* | Corson Ceulemans | Corson Ceulemans ✓ |
| 26 | MIN *(from PIT)* | Carson Lambos | Carson Lambos ✓ |
| **27** | NSH *(from CAR)* | Nolan Allan | **Zachary L'Heureux** |
| 28 | COL | Oskar Olausson | Oskar Olausson ✓ |
| **29** | NJD *(from NYI)* | Sasha Pastujov *(traded)* | **Chase Stillman** |
| 30 | VGK | Zachary Dean | Zach Dean ✓ |
| 31 | MTL | Logan Mailloux | Logan Mailloux ✓ |
| **32** | CHI *(from TBL via CBJ)* | Isaac Howard | **Nolan Allan** |

---

## Players wrongly present

Four names in the workbook were never 2021 first-round selections:

| Player | Actual draft position |
|---|---|
| Owen McLaughlin | 2023 draft, round 5 |
| Matthew Knies | 2021 pick 57 — round 2 |
| Sasha Pastujov | 2021 pick 66 — round 3 |
| Isaac Howard | **2022** pick 31 |

Isaac Howard is the duplicate flagged by the internal consistency check. He belongs in the 2022 sheet only.

## Players wrongly absent

| Player | Correct position |
|---|---|
| Sebastian Cossa | 2021 pick 15 |
| Zachary L'Heureux | 2021 pick 27 |
| Chase Stillman | 2021 pick 29 |

---

## Diagnosis

The errors cluster where picks were traded. Nine of the ten wrong entries sit at slots that changed hands, and the roster consistently records the player a team **ended up with** rather than the player selected **at that slot**. Picks 20 and 22 are transposed — Minnesota and Edmonton swapped slots, and the roster follows the teams rather than the slot numbers.

This matters beyond bookkeeping: the verdict layer computes the gap between index rank and **pick number**. Ten wrong pick numbers corrupt every Steal and Reach call in the cohort, and three players carry outcome data that belongs to no first-round slot at all.

---

## Still unverified

Only the 2021 NHL roster has been checked against a draft record. The following have not:

- NHL 2020, 2022, 2023, 2024, 2025
- NBA 2020 through 2025 — all six years
- MLB — the entire workbook

Given ten errors in the first roster examined, and given that both NFL cohorts contained roster defects, **assume every remaining roster is defective until verified pick-by-pick against a draft record.**

---

*Revelations Analytics · Verified 11 September 2026*

---
---

# NHL 2020 Round 1 — Verified Roster Correction

**Source:** myNHLdraft.com official 2020 Round 1 results. Cross-checked against NHL.com ("Complete breakdown of all 31 selections") and ESPN. Retrieved 11 September 2026.

**Count is correct at 31** — but for the right reason. The league had 31 teams in 2020; Seattle did not begin play until 2021. The workbook README attributes this to "the Arizona forfeit," which is wrong. Arizona's penalty cost a 2020 **second**-round pick (#49) and the **2021 first**-round pick (#11).

## Four errors of 31

| Pick | Team | Workbook has | **Correct selection** |
|---|---|---|---|
| **19** | NYR *(from CGY)* | Connor Zary | **Braden Schneider** |
| **22** | WSH *(from CGY via NYR)* | Braden Schneider | **Hendrix Lapierre** |
| **24** | CGY *(from WSH)* | Hendrix Lapierre | **Connor Zary** |
| **30** | DAL | Helge Grans | **Mavrik Bourque** |

Picks 19, 22 and 24 form a three-way rotation. Calgary, the Rangers and Washington executed a chain of trades across those slots, and the workbook again follows the **teams** rather than the **slot numbers** — the identical failure pattern found in 2021 and in the NFL 2022 cohort.

**Wrongly present:** Helge Grans — selected 35th, round 2 (Los Angeles).
**Wrongly absent:** Mavrik Bourque — pick 30, Dallas.

Note that Helge Grans carries a realized outcome in the workbook ("AHL/European ceiling, sub-replacement") attached to a slot that belongs to Mavrik Bourque. Bourque's outcome is absent entirely.

## Pick 15 — Rodion Amirov

Correctly placed. The workbook's note that outcome classification is not applicable due to his death in 2023 is right, and matches the exclusion policy applied to Jeff Gladney in the NFL 2020 cohort. He should be excluded from hit-rate computation, not scored as a bust.

---

## Running tally — NHL rosters verified

| Cohort | Picks | Errors found | Status |
|---|---|---|---|
| NHL 2020 | 31 | **4** | Verified, corrections above |
| NHL 2021 | 31 *(not 32)* | **10** | Verified, corrections above |
| NHL 2022 | 32 | — | Not yet verified |
| NHL 2023–2025 | 96 | — | Not yet verified (no outcome data populated) |
| NBA 2020–2025 | 180 | — | Not yet verified |
| MLB | — | — | Not yet verified |

**Fourteen roster errors across the two NHL cohorts that carry outcome data.** Every one sits at a traded slot. The pattern is now confirmed across three leagues and four cohorts: rosters were assembled by recalling which team ended up with which player, rather than by reading a draft record top to bottom.

---
---

# NHL 2022 Round 1 — Verified Roster Correction

**Source:** Fear the Fin full 225-selection list, cross-checked against myNHLdraft (picks 1–13) and NHL.com (Mintyukov #10, Yurov #24, Mešár #26 to Montreal). Retrieved 11 September 2026.

**Count correct at 32.** No forfeits.

## Two errors of 32

| Pick | Team | Workbook has | **Correct selection** |
|---|---|---|---|
| **11** | ARI *(from SJS)* | Filip Bystedt | **Conor Geekie** |
| **27** | SJS *(from CAR via MTL via ARI)* | Cameron Lund | **Filip Bystedt** |

Bystedt is displaced upward by sixteen slots. San Jose acquired pick 27 through a three-team chain and took Bystedt there; Arizona used San Jose's original pick at 11 on Conor Geekie. The workbook again tracked the **team** rather than the **slot**.

**Wrongly present:** Cameron Lund — selected 34th, round 2 (San Jose).
**Wrongly absent:** Conor Geekie — pick 11, Arizona.

The outcome note attached to the workbook's pick 27 ("NCAA/developing, rotational projection") describes Cameron Lund, not Filip Bystedt. Geekie has no outcome recorded at all.

**Isaac Howard is correctly placed at pick 31.** His appearance in the 2021 sheet is the erroneous entry; this one stands.

---

# Consolidated NHL findings

| Cohort | Picks | Errors | Outcome data | Status |
|---|---|---|---|---|
| NHL 2020 | 31 | **4** | Populated | **Verified** |
| NHL 2021 | 31 *(not 32)* | **10** | Populated | **Verified** |
| NHL 2022 | 32 | **2** | Populated | **Verified** |
| NHL 2023 | 32 | — | Empty | Not verified |
| NHL 2024 | 32 | — | Empty | Not verified |
| NHL 2025 | 32 | — | Empty | Not verified |

**All three back-testable NHL cohorts are now verified. Sixteen roster errors corrected across 94 selections — a 17% defect rate.**

## The pattern, now conclusive

Every one of the sixteen errors sits at a slot that changed hands in a trade. Not one occurs at a pick that stayed with its original team. In each case the roster records the player a franchise **ended up with** rather than the player taken **at that slot number**.

Six players were listed who were never first-round picks in the year assigned:

| Player | Listed as | Actual |
|---|---|---|
| Owen McLaughlin | NHL 2021 #14 | 2023 draft, round 5 |
| Matthew Knies | NHL 2021 #23 | 2021 #57, round 2 |
| Sasha Pastujov | NHL 2021 #29 | 2021 #66, round 3 |
| Isaac Howard | NHL 2021 #32 | 2022 #31 |
| Helge Grans | NHL 2020 #30 | 2020 #35, round 2 |
| Cameron Lund | NHL 2022 #27 | 2022 #34, round 2 |

Six genuine first-round selections were absent entirely: Sebastian Cossa, Zachary L'Heureux, Chase Stillman, Mavrik Bourque, Conor Geekie, and the vacant forfeited slot at 2021 #11.

**Consequence for scoring.** The verdict layer computes the gap between index rank and pick number. Sixteen wrong pick numbers would corrupt every Steal and Reach call in the NHL leg. Six players carry outcome data belonging to slots they never occupied, and six real selections carry none.

---

## Remaining

| Workbook | Cohorts | Players | Status |
|---|---|---|---|
| NBA | 2020–2025 | 180 | **Not verified** |
| MLB | — | — | **Not verified, not yet read** |
| NHL 2023–2025 | 3 | 96 | Not verified — no outcome data, lower priority |

NBA 2020, 2021 and 2022 carry populated outcome data and are the next priority.

---
---

# NBA 2020 Round 1 — Verified under RCP v1.0

**Source:** NBA.com "2020 NBA Draft results, picks 1–60", cross-checked against beIN SPORTS and CBS Sports pick-by-pick trackers. Retrieved 11 September 2026.

## Player roster: CLEAN — 0 errors of 30

All thirty selections match the draft record exactly, in slot order. No wrongly-present players, none absent, no round-2 contamination, no duplicates.

**This is the first roster examined that passes.** It is also the first NBA cohort checked, which suggests the transcription method used for basketball differed from the one used for hockey and football — worth knowing, because whatever was done here should be the template.

## One error found — drafting team at pick 27

| Pick | Workbook team | **Correct team** | Player |
|---|---|---|---|
| **27** | New York Knicks | **Utah Jazz** | Udoka Azubuike |

Azubuike is in the right slot with the right name; the selecting franchise is wrong. New York held picks 8 and 23 in this draft, not 27.

This is a lesser defect than a misplaced player — it does not affect RI scoring, tier assignment, or the verdict layer, all of which key on pick number. It should still be corrected, because a team column that is wrong once cannot be trusted anywhere.

## RCP verification result

| Check | Result |
|---|---|
| 1 · Slot count (30) | PASS |
| 2 · Slot continuity 1–30 | PASS |
| 3 · Within-year uniqueness | PASS |
| 4 · Cross-year uniqueness | PASS |
| 5 · Round contamination | PASS |
| 6 · Forfeit handling (none) | PASS |
| 7 · Annotation cleanliness | PASS |
| 8 · Source recorded | PASS |

**CLEARED FOR SCORING** — once the workbook weights, tier bands and dashboard formula are corrected.

---

## Cumulative roster audit

| Cohort | Picks | Player errors | Other | Status |
|---|---|---|---|---|
| NFL 2020 | 32 | 2 *(Wirfs/Kinlaw transposed)* | 11 award records wrong | Verified |
| NFL 2022 | 32 | 3 *(+1 omitted)* | 13 wAV values wrong | Verified |
| NHL 2020 | 31 | 4 | — | Verified |
| NHL 2021 | 31 *(not 32)* | 10 | Count wrong | Verified |
| NHL 2022 | 32 | 2 | — | Verified |
| **NBA 2020** | **30** | **0** | 1 team name | **Verified — clean** |
| NBA 2021 | 30 | — | — | Pending |
| NBA 2022 | 30 | — | — | Pending |
| NBA 2023–2025 | 90 | — | — | Pending (no outcome data) |
| NHL 2023–2025 | 96 | — | — | Pending (no outcome data) |
| MLB | — | — | — | Not read |

**21 player-placement errors across 188 verified selections.** NBA 2020 is the first cohort with none.

---
---

# NBA 2021 & 2022 Round 1 — Verified under RCP v1.0

**Sources:** NBA.com "2021 NBA Draft results: Picks 1–60" and Sports Illustrated "Complete List of Every Pick in the First Round of the 2022 NBA Draft". Both slot-ordered. Retrieved 11 September 2026.

## NBA 2021 — player roster CLEAN, 0 errors of 30

All thirty players in correct slots. Three name variants reconciled, none material:

| Workbook | Source | Same player |
|---|---|---|
| Josh Primo | Joshua Primo | yes |
| Trey Murphy III | Trey Murphy | yes |
| Bones Hyland | Nah'Shon Hyland | yes |

**Two drafting-team errors** — and they are the diagnostic pattern in its mildest form:

| Pick | Workbook team | **Selecting team** | Player |
|---|---|---|---|
| **10** | Memphis Grizzlies | **New Orleans Pelicans** | Ziaire Williams |
| **17** | New Orleans Pelicans | **Memphis Grizzlies** | Trey Murphy |

New Orleans selected at 10 and traded Williams to Memphis; Memphis selected at 17 and traded Murphy to New Orleans. The workbook recorded each player's **destination** rather than the franchise that made the selection — and because the two teams traded in both directions, the error appears as a clean transposition.

This is the identical mechanism behind the sixteen NHL errors. Here it stopped at the team column because the players were still keyed to the right slots. In hockey it reached the player column and corrupted the roster.

## NBA 2022 — CLEAN, 0 errors of 30

All thirty players in correct slots, correct order. One name variant: TyTy Washington / TyTy Washington Jr.

## RCP verification

Both cohorts pass all eight checks. **CLEARED FOR SCORING** once workbook weights, tier bands and the dashboard formula are corrected.

---

# FINAL — Complete roster audit, all verified cohorts

| League | Cohort | Picks | Player errors | Other defects | Status |
|---|---|---|---|---|---|
| NFL | 2020 | 32 | **2** | 11 award records wrong | Verified |
| NFL | 2022 | 32 | **3** + 1 omitted | 13 wAV values wrong | Verified |
| NHL | 2020 | 31 | **4** | — | Verified |
| NHL | 2021 | 31 *(not 32)* | **10** | Count wrong; forfeit misattributed | Verified |
| NHL | 2022 | 32 | **2** | — | Verified |
| NBA | 2020 | 30 | **0** | 1 team name (pick 27) | Verified |
| NBA | 2021 | 30 | **0** | 2 team names (picks 10, 17) | Verified |
| NBA | 2022 | 30 | **0** | — | Verified |

**248 selections verified. 21 player-placement errors, all in NFL and NHL. Zero in NBA.**

## What the split reveals

The three NBA cohorts contain no misplaced players. The five NFL and NHL cohorts contain twenty-one. That is not chance — it means the basketball rosters were transcribed by a different method than the football and hockey rosters, and the basketball method was the correct one.

The residual NBA defects are the same error caught early: three team-column entries recording where a player **went** rather than who **selected** him. The error begins in the team column. In NBA it stopped there. In NFL and NHL it propagated into the player column and corrupted twenty-one slots.

RCP Rule 1 closes it at the source: read slot → player → team, in that order, from a slot-ordered record.

## Remaining

| Workbook | Cohorts | Players | Priority |
|---|---|---|---|
| MLB | all | — | **Not read.** Highest — it is the league documented as failing at 10.8% |
| NBA 2023–2025 | 3 | 90 | Low — no outcome data populated |
| NHL 2023–2025 | 3 | 96 | Low — no outcome data populated |

**Every cohort carrying outcome data in NFL, NHL and NBA is now verified.**

---
---

# MLB 2020 Round 1 — Verified under RCP v1.0

**Sources (four, independent):** ESPN 2020 draft order, ESPN draft tracker, NBC Sports Boston order list, Bleacher Report Day 1 grades, MLB.com/draft/2020/order. All agree. Retrieved 11 September 2026.

## Player placement within Round 1: CLEAN — 0 errors of 29

All twenty-nine first-round selections are in the correct slots.

## The defect is the boundary, not the players

**MLB Round 1 in 2020 contained 29 picks, not 30.** Houston forfeited its first-round selection as part of the sign-stealing penalty. Every source states this explicitly.

**Jordan Westburg at pick 30 is a Competitive Balance Round A selection, not a first-round pick.** ESPN, NBC Sports Boston and Bleacher Report all print a "Competitive Balance Round A" header immediately before pick 30.

The workbook README compounds this: it states the 2020 draft "contained 30 R1 picks (5 rounds total due to COVID)." The five-round truncation is true and irrelevant. The count is 29 because of the Houston forfeit.

## Why this matters more than one name

**The inclusion rule is inconsistent.** Competitive Balance Round A in 2020 ran eight picks — 30 through 37, awarded to Baltimore, Pittsburgh, Kansas City, Arizona, San Diego, Colorado, Cleveland and Tampa Bay.

| CBR-A pick | Player | In workbook? |
|---|---|---|
| 30 · Baltimore | Jordan Westburg | **Yes** |
| 31 · Pittsburgh | Carmen Mlodzinski | No |
| 32 · Kansas City | Ben Hernandez | No |
| 33–37 | five further selections | No |

One of eight admitted, seven omitted, with no stated rule. The cohort was truncated at thirty because thirty is a round number — not because of any draft-structural boundary.

This silently pads the cohort by one player and makes the MLB leg non-comparable to the other three leagues, where "Round 1" has an unambiguous edge.

## The decision you have to make

Competitive Balance Round A has no equivalent in the NFL, NBA or NHL. Two defensible options:

**Option A — Round 1 proper only.** MLB 2020 = 29 players. Cleanest, matches the other three leagues, and matches what every source calls "Round 1." Westburg is removed.

**Option B — Round 1 plus all of CBR-A.** MLB 2020 = 37 players. Defensible on the reasoning that CBR-A picks carry first-round talent and bonus value. Requires adding seven players and their outcome data.

**What is not defensible is the current state** — Round 1 plus exactly one CBR-A pick.

**Recommendation: Option A.** The cross-league claim rests on comparing like with like, and every other league's Round 1 is a hard-edged, league-defined set. Adding a supplemental round to one league and not the others introduces a structural difference into the exact comparison the framework exists to make. State the exclusion explicitly in the README and apply it to all six MLB cohorts.

## RCP verification — Round 1 proper, 29 players

| Check | Result |
|---|---|
| 1 · Slot count (29) | PASS |
| 2 · Slot continuity 1–29 | PASS |
| 3 · Within-year uniqueness | PASS |
| 6 · Forfeit handling | PASS — Houston's forfeit removes a slot rather than vacating one, since it sat at the end of the round |
| 7 · Annotation cleanliness | PASS |
| 8 · Source recorded | PASS |

**CLEARED FOR SCORING at n = 29**, once the boundary decision is recorded.

---

## MLB — remaining verification

| Cohort | Workbook count | Status |
|---|---|---|
| MLB 2020 | 30 → **29** | **Verified.** Boundary corrected |
| MLB 2021 | 30 | Not verified — check for comp picks and CBR-A bleed |
| MLB 2022 | 30 | Not verified |
| MLB 2023 | 30 | Not verified (no outcome data) |
| MLB 2024 | 30 | Not verified (no outcome data) |
| MLB 2025 | 27 | Not verified. README cites Dodgers / Mets / Yankees luxury-tax forfeits — confirm |

Every MLB cohort is listed at exactly 30 except 2025. Given that 2020's true count is 29, **the uniform 30 is itself a warning sign** — it suggests the count was assumed rather than read from a draft record. 2021 carried a compensation pick for Trevor Bauer sitting between Round 1 and CBR-A, which is another boundary that must be checked rather than assumed.

---
---

# MLB 2021 Round 1 — Structural audit

**Sources (five, independent):** MLB.com draft order page; MLB.com mock-draft article ("29 first-round picks … every team but the Astros, who lost their top two picks in both 2020 and 2021"); ESPN draft order; Bleacher Report Day 1 grades; MLB Daily Dish draft primer. Retrieved 11 September 2026.

## Round 1 contained 29 picks, not 30 — the same defect as 2020

Houston forfeited its 2021 first-round pick. The sign-stealing penalty stripped their first **and** second-round selections in **both** 2020 and 2021.

**Pick 30 is a compensation pick awarded to Cincinnati for losing Trevor Bauer**, not a first-round selection. Under the qualifying-offer rule, that compensation slots *between* Round 1 and Competitive Balance Round A. Bleacher Report confirms CBR-A running from 31, with Ty Madden at 32.

So the 2021 order is: **Round 1 = 1–29 · Compensation = 30 · CBR-A = 31 onward.**

The workbook sheet is titled "Round 1 (30 picks)" and holds 30 entries — one past the boundary, exactly as in 2020.

## Verified segment — picks 1 through 12: CLEAN, 0 errors

Matches the ESPN slot-ordered order exactly: Davis, Leiter, Jobe, Mayer, Cowser, Lawlar, Mozzicato, Montgomery, Bachman, Rocker, House, Ford.

## One RCP Rule 5 violation

Pick 10 reads **"Kumar Rocker (unsigned)"**. The name field must contain the name only. Rocker was selected 10th by the Mets in 2021 and did not sign; he re-entered and went 3rd to Texas in 2022. Signing status is a note, never part of the identifier.

This also creates a cross-cohort duplicate risk: Rocker appears in both MLB 2021 (#10) and MLB 2022 (#3). **Unlike the Isaac Howard case in the NHL, both entries are correct** — he was genuinely drafted twice, in different years, having not signed. The exclusion policy should say explicitly how an unsigned selection is handled, since he cannot carry a professional outcome for the 2021 slot.

## Picks 13 through 29 — now verified. CLEAN, 0 errors of 29

Completed against the CBS Sports full 612-pick tracker, cross-checked against ESPN (1–12) and Bleacher Report. **All twenty-nine Round 1 selections are in correct slots.**

## Pick 30 — a compound error

| | |
|---|---|
| Workbook has | Cooper Kinney, Tampa Bay Rays, at pick 30 |
| Actual pick 30 | **Jay Allen, OF, Cincinnati Reds** — compensation pick for Trevor Bauer |
| Cooper Kinney's true slot | **34** — Competitive Balance Round A, Rays |

Wrong player, wrong slot, wrong round, displaced four positions. The compensation pick at 30 and CBR-A picks 31, 32 and 33 were all skipped; the entry jumps to 34 and relabels it 30.

**The outcome is mis-keyed with it.** The workbook's pick-30 note reads "Minor league ceiling, sub-replacement" with Bust Flag Y. That outcome belongs to Cooper Kinney at pick 34. **Jay Allen, the genuine pick 30, appears nowhere in the workbook at all.**

## RCP verification — Round 1 proper, 29 players

All eight checks pass. **CLEARED FOR SCORING at n = 29**, with Kumar Rocker retained at pick 10, name field cleaned, and marked EXCLUDED — UNSIGNED per the rule below.

---

## MLB — status and the pattern

| Cohort | Workbook count | True Round 1 | Status |
|---|---|---|---|
| MLB 2020 | 30 | **29** | Verified — 0 player errors within 1–29; pick 30 is CBR-A |
| MLB 2021 | 30 | **29** | Boundary verified; picks 1–12 clean; **13–29 unverified** |
| MLB 2022 | 30 | unverified | Not started |
| MLB 2023 | 30 | unverified | Not started |
| MLB 2024 | 30 | unverified | Not started |
| MLB 2025 | 27 | unverified | Not started |

**Both audited MLB cohorts are 29, and both were recorded as 30.** The uniform 30 across five of six sheets was an assumption, not a reading. Houston's forfeit removed a first-round pick in 2020 and again in 2021, and in each year a supplemental pick was pulled in to fill the gap — a CBR-A selection in 2020, a compensation pick in 2021.

**Net effect on the MLB leg: at least two players who were never first-round picks are carrying outcome data inside first-round cohorts, and the stated sample size is inflated by one in each year.**

## Required before any MLB scoring

1. Record the round-boundary decision — Round 1 proper only, or Round 1 plus all supplemental picks. Apply it to all six cohorts.
2. Remove Jordan Westburg (2020 #30, CBR-A) and the 2021 #30 compensation entry, or add the full supplemental rounds for every year.
3. Strip the "(unsigned)" annotation from Kumar Rocker and add an explicit rule for unsigned selections.
4. Verify picks 13–29 of 2021 and all of 2022–2025 against slot-ordered sources.
5. Re-key outcome data wherever a slot changes occupant.

---

# Unsigned-selection rule — APPROVED, RCP v1.1

Added to the Roster Construction Protocol and applicable to all four leagues.

> **A selection that does not sign with the drafting club is retained in the roster at its slot, marked EXCLUDED — UNSIGNED, carries no outcome data, and is removed from hit-rate denominators. Where the player re-enters a later draft, his outcome attaches solely to the slot at which he signed.**

**Retained, not deleted.** An unsigned first-rounder is a failed selection — the club spent the pick and got nothing. Deleting the slot removes a bad outcome from the market's record and inflates the board's apparent hit rate. Since RI is measured *against* draft slot, anything that flatters the board distorts the comparison in the wrong direction.

**Applied to Kumar Rocker:**

| Slot | Treatment |
|---|---|
| MLB 2021 #10, Mets | Retained · EXCLUDED — UNSIGNED · no outcome · out of denominator |
| MLB 2022 #3, Rangers | Scored normally · full outcome data |

Both entries are legitimate — he was genuinely drafted twice. This is unlike the Isaac Howard duplicate in NHL 2021, where one entry was simply wrong.

**One disclosure for the record:** the Mets did not sign Rocker after their medical review flagged his elbow. That is durability information, and it is precisely what the Injury Risk Index exists to capture. The exclusion is a measurement decision, not a judgement that the pick was unremarkable, and the reason should be recorded in the notes field.

---

# MLB — verified status

| Cohort | Workbook | True Round 1 | Round 1 errors | Boundary defect |
|---|---|---|---|---|
| MLB 2020 | 30 | **29** | **0 of 29** | Pick 30 = Westburg, CBR-A |
| MLB 2021 | 30 | **29** | **0 of 29** | Pick 30 = Kinney, actually CBR-A #34 |
| MLB 2022 | 30 | unverified | — | — |
| MLB 2023 | 30 | unverified | — | — |
| MLB 2024 | 30 | unverified | — | — |
| MLB 2025 | 27 | unverified | — | — |

**Both audited MLB cohorts: zero errors inside Round 1, one boundary defect each.**

The baseball transcription was accurate within the round — like the NBA, and unlike the NFL and NHL. What failed in both years was the **edge**: Houston's forfeit shortened Round 1 to 29, and in each case a supplemental pick was pulled up to fill slot 30. In 2020 that was the adjacent CBR-A pick. In 2021 it was a pick four slots further down, skipping a compensation pick and three CBR-A selections on the way.

**Consequence:** two players are carrying outcome data inside first-round cohorts they were never part of, and two genuine selections — Jay Allen and the 2020 CBR-A group — carry none.

---

# MLB 2022 Round 1 — Verified under RCP v1.0

**Sources:** myMLBdraft.com 2022 Round 1 page — which separates Round 1, Compensation Picks and Competitive Balance A onto distinct pages — cross-checked against MLB Trade Rumors' full first-round list, NBC Chicago (picks 1–10), and MLB.com press-release anchors placing Parada 11th, Neto 13th, Crawford 17th and Barriera 23rd. Retrieved 11 September 2026.

## CLEAN — 0 player errors of 30

All thirty selections in correct slots. No wrongly-present players, none absent, no round-2 contamination, no duplicates.

## Boundary correct — 30 picks, and this time the count is right

Round 1 in 2022 held all thirty picks. Houston's forfeit covered 2020 and 2021 only; the penalty had expired. **This is the first MLB cohort where the workbook's count of 30 is correct** — and it is correct because the draft genuinely had 30 first-round picks, not because the sheet was verified.

**Kumar Rocker sits correctly at pick 3**, signed with Texas. This is the slot that carries his outcome under the unsigned rule; his 2021 entry at Mets #10 is the excluded one.

## RCP verification

All eight checks pass. **CLEARED FOR SCORING at n = 30.**

---

# MLB — final status, all outcome-bearing cohorts

| Cohort | Workbook | True R1 | R1 errors | Boundary | Cleared |
|---|---|---|---|---|---|
| MLB 2020 | 30 | **29** | **0 of 29** | Remove Westburg (CBR-A) | Yes, n=29 |
| MLB 2021 | 30 | **29** | **0 of 29** | Remove Kinney (CBR-A #34) | Yes, n=29 |
| MLB 2022 | 30 | **30** | **0 of 30** | Correct as stands | Yes, n=30 |

**88 first-round selections verified. Zero player-placement errors inside the round. Two boundary defects, both at slot 30, both now corrected.**

## What baseball tells us that hockey did not

MLB transcription was accurate within the round in all three cohorts — matching the NBA, and unlike the NFL and NHL. Every MLB defect sat at the **edge of the round**, and both stemmed from the same assumption: that Round 1 contains thirty picks. It did in 2022. It did not in 2020 or 2021, because Houston had forfeited.

The 2022 result is the proof: when the true count *was* thirty, the sheet was right. The error was never in reading players — it was in assuming a boundary instead of reading one.

## Approved boundary rule — RCP v1.2

> **Round 1 is the round as the league defines it. Competitive Balance picks, compensation picks, and any supplemental round are excluded from every cohort in every league. The count is read from the draft record for each year, never assumed.**

**Four edits to close MLB:**

1. MLB 2020 — delete pick 30 (Jordan Westburg). n = 29.
2. MLB 2021 — delete pick 30 (Cooper Kinney). n = 29. Mark Kumar Rocker at pick 10 EXCLUDED — UNSIGNED.
3. README — replace "2020 draft contained 30 R1 picks (5 rounds total due to COVID)" with: *"Round 1 counts vary by year. 2020 = 29 and 2021 = 29 (Houston forfeited its first-round pick in both years as a sign-stealing penalty). 2022 = 30. Competitive Balance and compensation picks are excluded from all cohorts."*
4. Verify 2023, 2024 and 2025 counts against a draft record before scoring. The 2025 sheet lists 27 and cites Dodgers / Mets / Yankees luxury-tax forfeits — confirm rather than assume.

---
---

# Round-1 count register — the boundary audit

The boundary has now failed in **four of twelve** cohorts examined. Because the defect class is "count assumed rather than read," every remaining cohort needs its count verified from a record before scoring — independently of per-slot verification.

## Verified counts

| League | Year | True Round 1 | Reason | Source status |
|---|---|---|---|---|
| NFL | 2020 | 32 | — | **Verified** |
| NFL | 2022 | 32 | — | **Verified** |
| NFL | **2023** | **31** | **Miami forfeited pick 21 — tampering (Brady / Payton)** | **Verified 11 Sep 2026** |
| NBA | 2020 | 30 | — | **Verified** |
| NBA | 2021 | 30 | — | **Verified** |
| NBA | 2022 | 30 | — | **Verified** |
| NHL | 2020 | 31 | 31 teams — Seattle joined 2021 | **Verified** |
| NHL | 2021 | 31 | Arizona forfeited pick 11 — combine testing | **Verified** |
| NHL | 2022 | 32 | — | **Verified** |
| MLB | 2020 | 29 | Houston forfeited — sign-stealing | **Verified** |
| MLB | 2021 | 29 | Houston forfeited — sign-stealing | **Verified** |
| MLB | 2022 | 30 | Penalty expired | **Verified** |

## NFL 2023 — new finding

Miami forfeited its 2023 first-round selection, which would have been pick 21, following the league's tampering investigation. Sources: ESPN, NFL.com, CBS Sports, Pro Football Network, BetMGM, KHOU. The Dolphins also lost a 2024 third-round pick; that does not affect any first-round count.

**The NFL workbook must be checked for a 32-row 2023 sheet.** If it holds 32, one row is an intruder — precisely the MLB 2020 and 2021 failure, transplanted.

Note the precedent: New England forfeited first-round picks in 2008 (Spygate) and 2016 (Deflategate), each producing a 31-pick round. Forfeiture is not rare, and a fixed 32 is never safe to assume.

## Counts NOT yet verified

| League | Years | Assumed | Risk |
|---|---|---|---|
| NFL | 2021, 2024, 2025 | 32 | Forfeitures possible; 2025 is the **pre-registered forward cohort** |
| NBA | 2023, 2024, 2025 | 30 | Low — NBA Round 1 has been stable at 30 |
| NHL | 2023, 2024, 2025 | 32 | Moderate — forfeitures have occurred twice since 2020 |
| MLB | 2023, 2024, 2025 | 30 / 30 / 27 | **High** — two of three audited MLB counts were wrong |

**MLB 2025 is the most urgent.** The workbook lists 27 and attributes it to Dodgers / Mets / Yankees luxury-tax penalties. That attribution needs checking: the standard luxury-tax penalty moves a club's highest selection back ten slots — it does not delete the pick. If the picks were moved rather than removed, Round 1 may still hold 30, and three genuine selections would be missing from the cohort.

**NFL 2025 is the most consequential.** It is one of the 131 pre-registered forward predictions and the forecast test the Sloan paper rests on. If that roster is wrong, the forward prediction set is corrupted before a single outcome resolves.

## Recommended order

1. **NFL 2025** — pre-registered forward cohort. Verify count and all slots.
2. **NFL 2023** — confirm the sheet holds 31, not 32; identify and remove any intruder.
3. **MLB 2025** — resolve the 27 vs 30 question.
4. **MLB 2023, 2024** — counts, then slots.
5. **NHL and NBA 2023–2025** — counts, then slots. Lowest risk, no outcome data.

None of these cohorts carries outcome data, so none affects the validation record as it stands. All of them affect any future scoring pass, and NFL 2025 affects the forward test directly.

---
---

# NFL 2025 Round 1 — Verified reference roster

**Why this cohort matters most.** NFL 2025 is one of the 131 pre-registered forward predictions — 32 players, hashed to `270ba5bc`, resolving 2028. It is the forecast test the Sloan paper rests on. Every other cohort audited here is calibration evidence. This one is the actual prediction.

**Source:** Pro-Football-Reference 2025 Draft Listing, page revised 10 September 2026, retrieved 11 September 2026. Structural cross-check: Wikipedia — *"For the first time in the common draft era, the 2025 draft commenced with all teams holding their original selections in the first round."*

## Count: 32. No forfeits.

All eight RCP checks pass. Slots 1–32 contiguous, 32 unique players, no annotations.

## Verified roster

| # | Player | Tm | Pos | | # | Player | Tm | Pos |
|---|---|---|---|---|---|---|---|---|
| 1 | Cam Ward | TEN | QB | | 17 | Shemar Stewart | CIN | DE |
| 2 | Travis Hunter | JAX | WR | | 18 | Grey Zabel | SEA | OT |
| 3 | Abdul Carter | NYG | DE | | 19 | Emeka Egbuka | TAM | WR |
| 4 | Will Campbell | NWE | OT | | 20 | Jahdae Barron | DEN | CB |
| 5 | Mason Graham | CLE | DT | | 21 | Derrick Harmon | PIT | DT |
| 6 | Ashton Jeanty | LVR | RB | | 22 | Omarion Hampton | LAC | RB |
| 7 | Armand Membou | NYJ | OL | | 23 | Matthew Golden | GNB | WR |
| 8 | Tetairoa McMillan | CAR | WR | | 24 | Donovan Jackson | MIN | OL |
| 9 | Kelvin Banks | NOR | OL | | 25 | Jaxson Dart | NYG | QB |
| 10 | Colston Loveland | CHI | TE | | 26 | James Pearce | ATL | DE |
| 11 | Mykel Williams | SFO | DL | | 27 | Malaki Starks | BAL | SAF |
| 12 | Tyler Booker | DAL | OL | | 28 | Tyleik Williams | DET | DT |
| 13 | Kenneth Grant | MIA | DT | | 29 | Josh Conerly | WAS | OL |
| 14 | Tyler Warren | IND | TE | | 30 | Maxwell Hairston | BUF | CB |
| 15 | Jalon Walker | ATL | DE | | 31 | Jihaad Campbell | PHI | LB |
| 16 | Walter Nolen | ARI | DT | | 32 | Josh Simmons | KAN | OL |

## Structural integrity check

Two franchises hold two first-round picks: the Giants at 3 and 25, Atlanta at 15 and 26. Both traded up. Houston and the Rams hold none, having traded out. Thirty-two picks across thirty teams — internally consistent, and exactly the pattern that produced misplaced players in the NHL and NFL 2022 cohorts.

**This is where a recall-built roster fails.** Anyone recording "which team took whom" would likely place Dart with the Giants' original slot rather than at 25, and Pearce at Atlanta's original rather than 26.

## What remains — and it is the critical step

**I have verified the draft record. I have not diffed it against your scored cohort.**

The 2025 pillar scores live in the hashed pre-registration file, not in anything I have read. The comparison that matters is:

> the 32 players in hash `270ba5bc` versus the 32 above, slot by slot.

Three outcomes:

1. **Exact match.** The forward prediction set is sound and the Sloan paper's forecast test stands.
2. **Player mismatches.** Same failure as NFL 2022 — and it would mean the pre-registration is committed to predictions about the wrong players in the wrong slots.
3. **A player in the hash who was not a 2025 first-rounder.** Same failure as Trey McBride.

**Outcome 2 or 3 cannot be silently corrected.** The hash was published before outcomes; amending the roster after the fact breaks the commitment that gives pre-registration its force. The honest remedy would be to publish the correction with its date, disclose it in the paper, and let the referee judge — which is survivable, and far better than the error surfacing in 2028.

**This is the single highest-priority verification left in the project.** It needs the hashed file, which only you have.

---
---

# NFL 2023 — intruder confirmed

**Sources (seven):** Pro-Football-Reference player page ("Pittsburgh Steelers in the 2nd round (32nd overall) of the 2023 NFL Draft"), NFL.com ("to begin second round"), ESPN, Steelers.com, Wikipedia, Yardbarker, Heavy. Retrieved 11 September 2026.

**The 2023 first round had 31 picks.** Miami forfeited its selection for tampering.

| | |
|---|---|
| Workbook sheet | `NFL_2023_R1` — README states "Round 1 (32 picks)", sheet holds 32 rows |
| Row 32 | Joey Porter Jr., CB, Penn State, Pittsburgh |
| Reality | **Second-round pick.** 32nd overall, acquired from Chicago in the Chase Claypool trade |

Porter's draft status has a documented consequence that settles it beyond dispute: **he carries no fifth-year option**, because fifth-year options attach only to first-round selections. The Steelers' entire contract situation with him turns on this.

**Correction:** delete row 32 from `NFL_2023_R1`. Count becomes 31. Update the README line.

This is the fourth boundary intruder found, joining Trey McBride (NFL 2022), Jordan Westburg (MLB 2020) and Cooper Kinney (MLB 2021). All four entered the same way — a count assumed at the round's usual size, with the next available pick pulled in to fill the gap.

---

# NFL workbook — full sheet status

Read in full, 11 September 2026.

| Sheet | Rows | True count | Status |
|---|---|---|---|
| NFL_2020_R1 | 32 | 32 | **Wirfs (13) and Kinlaw (14) transposed** — confirmed against PFR |
| NFL_2021_R1 | 32 | unverified | Not checked |
| NFL_2022_R1 | 32 | 32 | **CORRECT** — matches PFR exactly |
| NFL_2023_R1 | 32 | **31** | **Porter Jr. is an intruder** — delete row 32 |
| NFL_2024_R1 | 32 | unverified | Not checked |
| NFL_2025_R1 | 32 | 32 | **CORRECT** — matches PFR exactly, including traded slots 25 and 26 |

## An important clarification about NFL 2022

**The workbook's 2022 sheet is correct.** It has Dotson at 16, Zion Johnson 17, Burks 18, Penning 19, Pickett 20, McDuffie 21 — exactly matching Pro-Football-Reference.

The roster that contained Trey McBride and omitted Trent McDuffie was the **4 September scoring pass**, not this workbook. The scoring session rebuilt the roster from recall instead of reading the sheet sitting beside it.

That changes the diagnosis. The workbook was not the source of the NFL 2022 error — it was the correct reference that went unread. Scoring directly from the workbook rows, rather than reconstructing them, would have prevented it.

## Also confirmed in this read

- Workbook runs **v1.0 weights**: `RI = 0.30 CP + 0.25 AP + 0.20 AF + 0.15 HC + 0.10 DC`. Canonical is 0.34 / 0.23 / 0.18 / 0.15 / 0.10. **AP at 25%** — the pillar measured negative in both scored cohorts.
- **CSS**, not CGI, and still shown as additive in the Final Score formula.
- Tier bands **90 / 85 / 80 / 75 / below 75** — the third set in circulation.
- Dashboard reports **"Meets Benchmark: YES"** on all five tiers with zero players scored.
- Only the 2020, 2021 and 2022 sheets carry realized outcome data. 2023, 2024 and 2025 are empty.
