# Revelations Index — Public Data Repository

Accompanies the MIT Sloan Sports Analytics Conference 2027 Research Paper Competition submission. Published to satisfy the competition's open-source data requirement.

**What is here:** the cohorts as scored, the inputs behind every score, the pre-registration commitments, the outcomes with a source per record, and a complete log of every error found and corrected during verification.

**What is not here:** the weight-derivation procedure and the internal construction of the injury-risk and archetype components. The competition requires the data and encourages but does not require the code.

---

## Structure

```
/
├── README.md                        this file
├── DATA_PROVENANCE.md               every error found, how, and what changed
├── PROTOCOL.md                      pre-registration + roster construction protocol
├── LICENSE-DATA.md                  reproduction for verification; no commercial reuse
│
├── cohorts/
│   ├── nfl_2020_r1.csv              32 picks · scored · in-sample
│   ├── nfl_2022_r1.csv              32 picks · scored · held out of derivation
│   └── nfl_2025_r1_prereg.csv       32 picks · hashed forward cohort
│
├── outcomes/
│   ├── nfl_2020_outcomes.csv        wAV, Pro Bowls, All-Pro, seasons started
│   ├── nfl_2022_outcomes.csv        same
│   └── SOURCES.md                   per-record provenance
│
├── prereg/
│   ├── nfl2025_prereg.json          the hashed file, byte-identical
│   ├── DIGESTS.md                   published digests with lock dates
│   └── HYPOTHESES.md                five hypotheses, thresholds, results
│
├── analysis/
│   ├── verify_rosters.py            RCP v1.2 verifier — 8 checks
│   ├── correlations.py              every reported figure, reproducible
│   └── EXPECTED_OUTPUT.txt          what the scripts should print
│
└── exclusions/
    └── EXCLUSION_POLICY.md          written before scoring; applied uniformly
```

---

## Reproducing the reported figures

```bash
python analysis/verify_rosters.py     # all 8 RCP checks, every cohort
python analysis/correlations.py       # every correlation in the paper
diff <(python analysis/correlations.py) analysis/EXPECTED_OUTPUT.txt
```

Both scripts self-test before reporting and halt rather than print an unverified number. `correlations.py` cross-checks its own Spearman implementation against `scipy.stats.spearmanr` and aborts on any disagreement beyond 1e-9.

---

## Headline figures and where they come from

| Figure | Value | Script | Cohort |
|---|---|---|---|
| RI vs career value, 2020 all-32 | +0.413 | correlations.py | nfl_2020 |
| Draft slot vs career value, 2020 | +0.219 | correlations.py | nfl_2020 |
| RI, 2020 after exclusions (n=30) | +0.342 | correlations.py | nfl_2020 |
| RI vs career value, 2022 (n=31) | +0.525 | correlations.py | nfl_2022 |
| Draft slot, 2022 | +0.368 | correlations.py | nfl_2022 |
| Final Score (RI + CGI − IRI), 2020 | +0.261 | correlations.py | nfl_2020 |
| Athletic Profile, 2020 / 2022 | −0.194 / +0.026 | correlations.py | both |

Outcome measure: weighted career Approximate Value through the 2025 season, Pro-Football-Reference, retrieved after each score file was hashed. Compared within draft class.

---

## Known gaps, stated up front

1. **NFL 2022 stands at 31 of 32.** Trent McDuffie (pick 21) was omitted from the original scoring pass and has not been scored. Adding him now, with his outcome known, would contaminate the cohort — the remaining 31 were hashed before outcomes were consulted. The gap is disclosed rather than filled.
2. **Neither retrospective cohort is blind.** Scores were fixed before outcomes were consulted; they were not generated in ignorance of outcomes, and could not have been. See PROTOCOL.md.
3. **NFL 2025 was locked 31 August 2026**, after its rookie season concluded. It is a partial forward test resting on seasons two and three.
4. **Single evaluator.** No inter-rater reliability testing has been conducted.
5. **Cross-league cohorts are not included.** The NBA, NHL and MLB workbooks exist but contain no scored players. No cross-league validation is claimed.

---

## Why DATA_PROVENANCE.md exists

Verification against primary sources found **22 roster errors across 248 first-round selections** in this project's workbooks, plus 13 incorrect outcome values and 11 incorrect award records. Every one is logged with the source that corrected it and the date.

Most submissions publish a clean dataset and assert it is correct. This one publishes the errors it contained, how they were found, and what changed. A referee can check the corrections against the same public records used to make them.

The errors clustered at two points, and both are now closed by protocol:

- **Traded slots.** Rosters recorded which team a player *ended up with* rather than who was selected *at that slot*. Twenty-one of twenty-two errors sat at traded picks.
- **Round boundaries.** Counts were assumed rather than read. Four cohorts held a player from outside the round — Joey Porter Jr. in NFL 2023, Trey McBride in NFL 2022, Jordan Westburg in MLB 2020, Cooper Kinney in MLB 2021.

---

*Revelations Index · Submission to SSAC27 · Data published under LICENSE-DATA.md*
