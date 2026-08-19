# Agent Instructions

## Repository Purpose

This repository contains the installable `analyze-gold-outlook` skill. Use it to produce evidence-backed short-, medium-, and long-term gold outlooks. Treat `analyze-gold-outlook/SKILL.md` as the authoritative entrypoint and keep the skill folder self-contained.

## Invoke the Skill

When the user asks about gold prices, 黄金、金价、黄金股、金银比、TIPS、实际利率、美联储、美元流动性, gold allocation, or a gold market forecast, load and follow:

```text
analyze-gold-outlook/SKILL.md
```

In clients with explicit skill invocation, use:

```text
$analyze-gold-outlook
```

Example request:

```text
Use $analyze-gold-outlook to analyze USD and RMB gold over the next month,
quarter, and two years. Check whether A-share gold miners are leading bullion,
then provide base, bull, and bear scenarios with invalidation triggers.
```

## Required Workflow

1. Read `analyze-gold-outlook/SKILL.md` completely before taking task actions.
2. Define the instrument, currency, horizon, as-of time, and user decision. Distinguish USD gold, RMB gold, ETFs, and miners.
3. For a current outlook, retrieve timely evidence from primary sources. Preserve observation date, release date, unit, frequency, and source. If current data cannot be accessed, state the limitation and do not fabricate values.
4. Build the causal chain before assigning a direction: shock → growth/inflation expectations → Fed path and term premium → real yields → dollar/liquidity → positioning and flows → gold.
5. Separate short-, medium-, and long-term conclusions. Do not force one direction across all horizons.
6. Lead the final answer with the conclusion, then explain the dominant causal chain, contradictions, scenarios, monitoring triggers, and invalidation conditions.

## Progressive Reference Loading

Load only the references needed for the request:

| Request | Required reference |
| --- | --- |
| Any full gold outlook | `references/framework.md` |
| Current macro and market indicators | `references/indicators.md` and `references/data-sources.md` |
| A-share gold miners or miner/bullion lead-lag | `references/a-share-gold-equities.md` |
| Structured scoring or confidence audit | `references/scoring.md` |
| Full report or concise answer formatting | `references/output-template.md` |

Do not load every reference by default. Follow the links from `SKILL.md` and use progressive disclosure.

## Scoring

Use the scorer only after mapping observed evidence to an impact from `-2` to `+2` and a confidence from `0` to `1`. Omit missing evidence instead of entering a neutral zero.

```bash
python3 analyze-gold-outlook/scripts/score_gold_outlook.py INPUT.json --format markdown
```

Treat the result as an audit trail, not a trained price forecast. Explain any qualitative override.

## Analytical Guardrails

- Do not double-count Fed pricing, nominal yields, real yields, breakevens, and the dollar when they reflect the same macro shock.
- Do not treat a high gold-silver ratio as an automatic gold buy; interpret it with both metals' absolute price directions.
- Do not treat A-share miner strength as a bullion lead before checking RMB translation, costs, equity beta, breadth, earnings revisions, and company events.
- Do not present central-bank purchase estimates as a daily timing indicator.
- Do not invent a point target without a disclosed valuation, technical, options, or scenario method.
- Write in coherent paragraphs and use tables only when they improve horizon, scenario, or indicator comparisons.

## Repository Validation

Run these checks after changing skill logic or scripts:

```bash
python3 -m py_compile analyze-gold-outlook/scripts/score_gold_outlook.py
python3 analyze-gold-outlook/scripts/test_score_gold_outlook.py
```

If the OpenAI skill-creator validator is available, also run `quick_validate.py` against `analyze-gold-outlook`. Keep user-facing documentation at the repository root; do not place additional README files inside the installable skill folder.
