---
name: analyze-gold-outlook
description: Analyze and forecast gold across short-, medium-, and long-term horizons using U.S. real yields and Federal Reserve policy, the dollar, dollar liquidity and Treasury financing, fiscal and monetary credibility, official-sector demand, technical price structure and momentum, the gold-silver ratio, positioning, and A-share gold-mining equities as a conditional leading signal. Use for current gold outlooks, gold investment theses, technical and macro synthesis, scenario analysis, timing and risk checks, explanations of gold moves, price-level analysis, or comparisons of bullion, gold ETFs, and gold miners. Trigger on requests about gold prices, 黄金、金价、黄金股、金银比、技术面、支撑阻力、TIPS、实际利率、美联储、美元流动性与黄金配置.
---

# Analyze Gold Outlook

## Objective

Produce an evidence-backed gold view instead of a mechanical indicator tally. Separate observation, causal interpretation, technical confirmation, and forecast; state what is known as of a specific date, what is inferred, and what would invalidate the view. Never return only directional labels, a score, or a price target unless the user explicitly requests a result-only answer.

## Workflow

1. Define the instrument, currency, horizon, and decision. Distinguish USD gold, RMB gold, gold ETFs, and gold-mining equities. If the user does not specify them, analyze USD gold and add the USD/CNY translation when relevant to a China-based investor.
2. Gather current evidence before forecasting. Browse for time-sensitive data and prefer official or primary sources. Record observation date, publication date, frequency, and unit. Never present stale releases as current.
3. Build an evidence ledger before reaching a conclusion. For every material signal, record the observation, date, source, relevant horizon, causal mechanism, directional implication, confidence, and the strongest alternative explanation. Distinguish facts from inference.
4. Read [references/framework.md](references/framework.md) to build the causal chain. Treat real rates and the dollar as the main short-to-medium pricing variables, liquidity and Treasury financing as transmission variables, and fiscal/monetary credibility plus official demand as structural variables.
5. Read [references/indicators.md](references/indicators.md) for indicator definitions, transformations, and failure modes. Use levels and changes together. Do not double-count nominal yields, real yields, inflation expectations, and Fed pricing as independent evidence when they express the same move.
6. For a current outlook, timing question, entry discussion, or price-level request, read [references/technical-analysis.md](references/technical-analysis.md). Diagnose trend, structure, momentum, volatility, and confirmation across appropriate timeframes. Use technical analysis mainly for short-to-medium timing and invalidation; do not let an oscillator override the long-term macro regime.
7. When using A-share gold equities, read [references/a-share-gold-equities.md](references/a-share-gold-equities.md). Treat miners as a conditional, not universal, leading signal. Decompose their move into RMB gold, costs, equity beta, company events, and earnings revisions before inferring anything about bullion.
8. When a structured score is useful, map each observed signal to a gold impact from -2 to +2 with a confidence from 0 to 1, then run `python3 scripts/score_gold_outlook.py INPUT.json --format markdown`. Read [references/scoring.md](references/scoring.md) before assigning impacts. Use the score as an audit trail, not as a substitute for judgment. Collapse technical sub-indicators into one technical-state signal inside the cross-asset/positioning family.
9. Reconcile conflicts by horizon. A short-term bearish real-rate shock can coexist with a long-term bullish fiscal-credit thesis. Prefer a conditional conclusion over forcing all horizons into one direction.
10. Write the report using [references/output-template.md](references/output-template.md). Lead with the conclusion, then show the supporting observations and explain the dominant causal chain, technical confirmation or divergence, competing explanations, scenarios, monitoring triggers, and invalidation conditions. Provide an auditable reasoning summary, not private scratch work or hidden chain-of-thought.

## Required Analytical Narrative

Unless the user explicitly asks for only a conclusion, every answer must include all of the following in proportion to the question:

1. **What changed:** the dated market or macro observations that matter.
2. **Why it matters:** the transmission from the shock through expectations, real yields, the dollar/liquidity, flows, and gold.
3. **What the technical state confirms or contradicts:** trend, price structure, momentum, volatility, and key levels.
4. **Why the conclusion is not certain:** conflicting evidence, alternative attribution, missing data, and what is already priced.
5. **What changes the view:** observable confirmation and invalidation conditions for each relevant horizon.

Do not expose unfiltered internal deliberation. Present the compact, decision-relevant evidence and causal rationale that a reader can verify.

## Analytical Guardrails

- Do not claim deterministic prediction or invent a point target without a disclosed valuation or technical method.
- Do not return a naked bullish/bearish verdict or a scorer table without explaining the evidence, mechanism, contradictions, and invalidation path.
- Do not infer causality from one-day correlation. Require confirmation across price, rates, the dollar, and flows or positioning.
- Do not equate a high gold-silver ratio with an unconditional gold buy. Interpret the ratio jointly with both metals' price directions.
- Do not equate Fed easing with automatic dollar weakness or gold strength. Ask whether easing is already priced, whether inflation and term premium are rising, and whether the move is growth-scare easing or reflationary easing.
- Do not use the popular `Fed assets - TGA - ON RRP` identity as a complete liquidity model. Explain the funding channel, Treasury maturity mix, reserve conditions, and money-fund absorption.
- Do not use A-share miner strength as a bullion lead when the move is explained by RMB depreciation, cost changes, equity-market beta, M&A, dividends, or firm-specific news.
- Separate price direction from relative performance. A rising gold-silver ratio may mean gold falls less than silver, not that gold rises.
- Match conviction to data coverage and conflicts. Label low-coverage conclusions as provisional.
- Do not stack RSI, MACD, moving averages, Bollinger Bands, and Fibonacci levels as independent votes. Start with price structure, then use momentum and volatility tools as confirmation; aggregate them into one technical-state judgment.

## Source and Style Rules

Use the source hierarchy and retrieval guidance in [references/data-sources.md](references/data-sources.md). Cite the closest primary source for every time-sensitive factual claim. Preserve exact dates and distinguish market timestamps from release periods.

Write in the user's language. Prefer a few substantive sections and full paragraphs over fragmented one-line bullets. Tables are appropriate for dashboards, scenarios, and horizon comparisons. Put the practical conclusion first and keep investment-risk language proportionate rather than boilerplate-heavy.

## Resources

- [references/framework.md](references/framework.md): causal model and horizon logic.
- [references/indicators.md](references/indicators.md): core indicator playbook.
- [references/technical-analysis.md](references/technical-analysis.md): multi-timeframe technical analysis and macro/technical synthesis.
- [references/a-share-gold-equities.md](references/a-share-gold-equities.md): miner leading-signal method.
- [references/scoring.md](references/scoring.md): transparent scoring and confidence rules.
- [references/data-sources.md](references/data-sources.md): primary-source map and data hygiene.
- [references/output-template.md](references/output-template.md): report structure and reusable prompts.
- `scripts/score_gold_outlook.py`: deterministic family-balanced scoring utility.
- `scripts/example_signals.json`: synthetic input example; never treat it as market data.
