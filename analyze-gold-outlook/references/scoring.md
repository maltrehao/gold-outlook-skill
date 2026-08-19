# Scoring and Confidence Method

## Contents

1. Purpose
2. Input scale
3. Family-balanced aggregation
4. Regime labels
5. Confidence and coverage
6. Manual override discipline

## 1. Purpose

Use scoring to expose assumptions and prevent narrative cherry-picking. Do not treat the score as a trained forecast or a price target. The qualitative report remains authoritative because market regimes, data quality, and causal relationships change.

## 2. Input scale

Map each current observation to its expected gold impact for the relevant horizon:

| Impact | Meaning |
| --- | --- |
| +2 | Strongly bullish, unusually large and causally direct |
| +1 | Bullish |
| 0 | Neutral or genuinely balanced; do not use 0 for missing data |
| -1 | Bearish |
| -2 | Strongly bearish, unusually large and causally direct |

Assign confidence from 0 to 1. Use 0.8–1.0 for timely, primary, direct data with a clear causal channel; 0.5–0.8 for good but lagged or partly confounded evidence; and below 0.5 for noisy proxies or unresolved attribution. Omit missing signals.

Every signal entry should include `impact`, `confidence`, `observation`, `as_of`, and `source`. A signal may specify horizon-specific impacts when the same fact has different effects, such as heavy Treasury coupon issuance being tactically bearish but structurally bullish through fiscal credibility.

## 3. Family-balanced aggregation

The script first computes a confidence-weighted average within each family, then applies fixed family weights by horizon. This prevents three correlated rate indicators from outvoting every other family.

| Family | Short | Medium | Long |
| --- | ---: | ---: | ---: |
| Opportunity cost | 30% | 35% | 20% |
| USD and liquidity | 25% | 25% | 10% |
| Fiscal and credibility | 5% | 20% | 45% |
| Risk and official demand | 15% | 10% | 20% |
| Cross-asset/positioning | 25% | 10% | 5% |

Weights renormalize over available families, but the report must show coverage against the full intended weight. Do not claim high conviction from one populated family.

## 4. Regime labels

The aggregate remains on the -2 to +2 impact scale:

| Score | Label |
| --- | --- |
| 0.80 to 2.00 | Bullish |
| 0.25 to 0.79 | Mildly bullish |
| -0.24 to 0.24 | Neutral/mixed |
| -0.79 to -0.25 | Mildly bearish |
| -2.00 to -0.80 | Bearish |

Thresholds are intentionally broad. A score of 0.81 is not economically distinct from 0.79.

## 5. Confidence and coverage

Coverage is the sum of horizon family weights for which at least one valid signal exists. Evidence confidence is the weighted mean of within-family confidence. The script reports a conflict index based on dispersion across family scores.

Use these practical rules:

- Coverage below 60%: provisional view.
- Coverage 60–80%: usable with explicit gaps.
- Coverage above 80%: broad evidence, not guaranteed accuracy.
- Conflict index above 0.9 on the -2 to +2 scale: emphasize scenarios rather than a single directional call.

## 6. Manual override discipline

If qualitative judgment differs from the mechanical label, retain both and explain the override. Valid reasons include a structural break, data release lag, temporary market dysfunction, a signal already fully priced, or a causal channel not represented in the input. “It feels wrong” is not a valid override.
