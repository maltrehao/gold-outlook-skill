# Agent Instructions

## Repository Purpose

This repository contains the installable `analyze-gold-outlook` skill. Use it to produce evidence-backed short-, medium-, and long-term gold outlooks with an explicit analytical narrative. Treat `analyze-gold-outlook/SKILL.md` as the authoritative entry point and keep the skill folder self-contained.

## Invoke the Skill

Load and follow `analyze-gold-outlook/SKILL.md` when the user asks about gold prices, bullion, gold miners, the gold-silver ratio, technical levels, support or resistance, TIPS, real yields, Federal Reserve policy, dollar liquidity, gold allocation, or a gold-market forecast.

In clients with explicit skill invocation, use:

```text
$analyze-gold-outlook
```

Example request:

```text
Use $analyze-gold-outlook to analyze USD and RMB gold over the next month,
quarter, and two years. Explain the evidence-to-conclusion path, combine the
macro framework with technical confirmation, check whether A-share gold miners
are leading bullion, and provide scenarios with invalidation triggers.
```

## Required Workflow

1. Read `analyze-gold-outlook/SKILL.md` completely before taking task actions.
2. Define the instrument, currency, horizon, as-of time, and user decision. Distinguish USD gold, RMB gold, ETFs, futures, and miners.
3. For a current outlook, retrieve timely evidence from primary sources. Preserve observation date, release date, unit, frequency, instrument, contract, and source. If current data cannot be accessed, state the limitation and do not fabricate values.
4. Build an evidence ledger before deciding. Record each decisive observation, its causal mechanism, relevant horizon, directional implication, confidence, and strongest alternative explanation.
5. Build the causal chain: shock -> growth and inflation expectations -> Federal Reserve path and term premium -> real yields -> dollar and liquidity -> positioning and flows -> gold.
6. Add a multi-timeframe technical overlay. Start with price structure and trend, then use momentum, volatility, volume, and open interest as confirmation. Identify support, resistance, and invalidation zones without false precision.
7. Reconcile macro and technical conflicts by horizon. Do not force one direction across short-, medium-, and long-term windows.
8. Lead the final answer with the conclusion, then explain the observations, causal transmission, technical confirmation or divergence, contradictions, scenarios, monitoring triggers, and invalidation conditions.

## Explanation Contract

Do not return only directional labels, a scorer table, or a target price unless the user explicitly asks for result-only output. Provide a compact, auditable reasoning summary that explains what changed, why it matters, what confirms or contradicts the thesis, and what would change the view. Do not expose private scratch work or hidden chain-of-thought.

## Progressive Reference Loading

Load only the references needed for the request:

| Request | Required reference |
| --- | --- |
| Any full gold outlook | `references/framework.md`, `references/indicators.md`, `references/output-template.md` |
| Current macro and market indicators | `references/indicators.md`, `references/data-sources.md` |
| Current outlook, timing, entry, or price levels | `references/technical-analysis.md` |
| A-share gold miners or miner/bullion lead-lag | `references/a-share-gold-equities.md` |
| Structured scoring or confidence audit | `references/scoring.md` |

Do not load every reference by default. Follow the links from `SKILL.md` and use progressive disclosure.

## Scoring

Use the scorer only after mapping observed evidence to an impact from `-2` to `+2` and a confidence from `0` to `1`. Omit missing evidence instead of entering a neutral zero. Aggregate all technical sub-indicators into one `technical_state` signal in the `cross_asset_positioning` family.

```bash
python3 analyze-gold-outlook/scripts/score_gold_outlook.py INPUT.json --format markdown
```

Treat the result as an audit trail, not a trained price forecast. Explain the evidence behind each material family score and any qualitative override.

## Analytical Guardrails

- Do not double-count Federal Reserve pricing, nominal yields, real yields, breakevens, and the dollar when they reflect the same macro shock.
- Do not stack moving averages, RSI, MACD, Bollinger Bands, and Fibonacci levels as independent votes. Price structure comes first; indicators confirm or challenge it.
- Do not treat a high gold-silver ratio as an automatic gold buy; interpret it with both metals' absolute price directions.
- Do not treat A-share miner strength as a bullion lead before checking RMB translation, costs, equity beta, breadth, earnings revisions, and company events.
- Do not present central-bank purchase estimates as a daily timing indicator.
- Do not invent a point target without a disclosed valuation, technical, options, or scenario method.
- Write in coherent paragraphs and use tables only when they improve horizon, scenario, evidence, or indicator comparisons.

## Repository Validation

Run these checks after changing skill logic or scripts:

```bash
python3 -m py_compile analyze-gold-outlook/scripts/score_gold_outlook.py
python3 analyze-gold-outlook/scripts/test_score_gold_outlook.py
```

If the OpenAI skill-creator validator is available, also run `quick_validate.py` against `analyze-gold-outlook`. Keep user-facing documentation at the repository root; do not place additional README files inside the installable skill folder.
