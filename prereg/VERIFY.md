# Digest Verification — Finding and Disclosure

**Status: the declared digest for NFL 2025 cannot be reproduced. This page states why, what remains true, and what is no longer claimed.**

## The finding

`RA_NFL2025_PreReg.json` declares:

```json
"sha256": "270ba5bccf8cbcb86c1f9fb5f78f461da03d896f8fd07c76252b7298a04452be"
```

That digest is not a hash of the file containing it, and cannot be. A file cannot carry its own SHA-256: hashing a byte stream that already contains the answer is a preimage problem, not achievable by construction.

The digest was therefore computed over some earlier form of the data — most plausibly the same content before the `sha256` field was inserted. That intermediate artifact was not retained.

## What was tested

| Test | Serialisations | Result |
|---|---|---|
| Full object, with and without the `sha256` field | 576 | No match |
| Metadata object alone, `sha256` field removed | 96 | No match |

Varied across: indent width (none, 1, 2, 4), separators, ASCII escaping, key ordering, trailing newline, line endings, and encoding. **672 combinations, no match.**

## What remains true

The **content** of the pre-registration file is independently verified, and that verification does not depend on the digest:

| Check | Result |
|---|---|
| Roster vs Pro-Football-Reference, slot by slot | 32 of 32 exact |
| Traded slots 25 and 26 (Dart, Pearce) | Correct — the configuration that corrupted other cohorts |
| RI recomputed from pillar scores under v3.9 | 32 of 32 exact |
| `rank` field consistent with RI ordering | Pass |
| `gap` = pick − ri_rank across all 19 calls | Pass |
| Call lists consistent with board rows | Pass |
| Threshold consistency at \|gap\| ≥ 6 | Pass |

## What is no longer claimed

**The digest is not evidence of temporal precedence.** It cannot be checked by a referee, and it was not published to any external timestamped location before outcomes were consulted. It is a self-asserted value inside the artifact it describes.

The precedence evidence that does exist is weaker but real: a dated third-party record of the session in which the scores were produced, held by the platform on which that session occurred, and the `locked` field's stated date of 31 August 2026. Neither is cryptographic. Both are disclosed for what they are.

## The corrected procedure, for every future cohort

1. Score the cohort and write the score file. **Do not include a digest field inside it.**
2. Compute the digest over the finished file.
3. **Publish the digest somewhere external and timestamped** — a public commit, a dated post, anything held by a third party.
4. Only then consult outcomes.

Step 3 is what the earlier procedure lacked. A digest recorded only inside its own artifact proves nothing about when the artifact existed.

## Current digest of the published file

Recomputed over the file as published in this repository, on the date shown:

```bash
sha256sum prereg/RA_NFL2025_PreReg.json
```

This digest is reproducible by anyone. It establishes that the file has not changed since publication. It does not, and is not presented to, establish anything about what existed before that date.
