# Pre-Registered Hypotheses

Five hypotheses with numeric success conditions, declared before any outcome data was examined. Four failed. All five are reported.

> **AUTHOR CHECK REQUIRED.** This file was reconstructed from the project record. Confirm each threshold and result against your source workbook before publishing. Any line you cannot confirm should be deleted, not guessed at.

---

## H1 — Tier separation

**Condition:** mean career value differs between adjacent projected tiers by at least 25%, in the correct direction.

**Result:** NOT MET.

Absolute tier projection degraded 20–27 points out-of-sample against fitted figures — the signature of single-cohort overfitting. The structural cause is documented in the paper's Section 7.4: tier bands set at 90/80/70/60 on a 0–100 scale assumed a scored population spanning that range, while first-round composites spanned roughly 69 to 94, leaving four of five bands unreachable.

---

## H2 — The index beats the market

**Condition:** the composite's rank correlation with career value equals or exceeds that of actual draft slot, or falls short by no more than 0.05.

**Result:** MET.

| Cohort | Composite | Draft slot | Margin |
|---|---|---|---|
| NFL 2020 (all 32) | +0.413 | +0.219 | +0.194 |
| NFL 2020 (n=30, exclusions applied) | +0.342 | +0.173 | +0.169 |
| NFL 2022 (n=31) | +0.525 | +0.368 | +0.157 |

The margin also holds on three further outcome measures — Pro Bowls, Pro Bowls weighted by All-Pro selections, and seasons as a primary starter — in seven of eight league-year combinations tested. The single exception is seasons as starter in 2022, where draft slot outperforms.

This is the only hypothesis that passed.

---

## H3 — Sub-indices add value

**Condition:** adding the character and injury sub-indices improves the composite's rank correlation with career value by at least 0.05 Spearman.

**Result:** NOT MET — the sub-indices made the model worse.

| Measure | NFL 2020 |
|---|---|
| Five-pillar composite | +0.413 |
| Final Score (composite + CGI − IRI) | +0.261 |
| **Effect** | **−0.152** |

The character index was removed from the headline model. The diagnosis is in Section 7.1: it measured pre-draft media consensus about character rather than character itself, and so re-imported the very board the model was attempting to beat.

---

## H4 — Injury index predicts games missed

**Condition:** prospects scoring 8 or above on the injury risk index miss more games in professional seasons one through three than prospects scoring 3 or below, by a margin of at least 4 games.

**Result:** NOT MET.

> **AUTHOR CHECK:** the games-missed figures behind this result are not in the repository. Either add them to `outcomes/` so the test is reproducible, or state here that the underlying data is not published and the result is reported without supporting detail.

---

## H5 — The comparative signal holds in both directions

**Condition:** upgrade calls and downgrade calls each confirm at 60% or better.

**Definition of a call:** a divergence of 6 or more slots between the composite's rank and actual selection order. A call confirms when an upgraded prospect finishes above his class median career value, or a downgraded prospect finishes at or below it.

**Result:** NOT MET.

| Direction | Confirmed | Rate |
|---|---|---|
| Upgrade calls | 13 of 22 | 59.1% |
| Downgrade calls | 11 of 23 | 47.8% |

Neither direction reaches the threshold, and neither separates from chance at these sample sizes. The asymmetry runs in the predicted direction — the framework identifies underpriced talent more readily than it identifies busts — but it does not replicate cohort to cohort, returning 73% in 2020 and 45% in 2022.

> **AUTHOR CHECK:** the threshold above is 6 slots, read from the NFL 2025 pre-registration file. The retrospective figures in this table were computed at that threshold. Confirm 6 was the value declared in advance for the retrospective cohorts, and not adopted later.

---

## Summary

| | Hypothesis | Result |
|---|---|---|
| H1 | Tier separation ≥ 25% | NOT MET |
| H2 | Composite matches or beats draft slot | **MET** |
| H3 | Sub-indices improve correlation by ≥ 0.05 | NOT MET |
| H4 | Injury index separates games missed by ≥ 4 | NOT MET |
| H5 | Both call directions confirm at ≥ 60% | NOT MET |

One of five. Reported in full, because a framework that publishes only its successes has not been tested.
