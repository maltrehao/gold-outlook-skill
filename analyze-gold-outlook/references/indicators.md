# Core Indicator Playbook

## Contents

1. Priority dashboard
2. Indicator interpretation
3. Gold-silver ratio states
4. Data transformations
5. Common analytical errors

## 1. Priority dashboard

| Family | Core observations | Gold-positive pattern | Gold-negative pattern | Primary horizon |
| --- | --- | --- | --- | --- |
| Opportunity cost | 5y/10y TIPS real yields, Fed path, real-yield curve | Real yields falling because policy expectations ease or inflation compensation rises without a stronger hawkish response | Real yields rising on tighter policy or stronger real growth | Short/medium |
| Dollar | DXY or broad trade-weighted USD, USD/CNY for RMB investors | Broad dollar weakening, or gold holding firm despite dollar strength | Broad dollar strengthening with gold losing relative resilience | Short/medium |
| Liquidity and Treasury | Fed balance sheet context, TGA, ON RRP, reserves, net issuance and maturity mix, auction quality | Improving reserve/liquidity conditions, issuance absorbed without term-premium shock | Funding stress, reserve drain, coupon-supply pressure, weak auctions | Short/medium |
| Fiscal/credibility | Deficit path, interest expense, debt maturity, term premium, policy coordination | Rising fiscal-risk or monetization premium, reserve diversification | Credible consolidation and persistently attractive real safe-asset returns | Medium/long |
| Demand and flows | Central-bank purchases, gold ETF flows, CFTC positioning | Durable official demand plus broadening private inflows | Official-demand slowdown with persistent ETF outflows | Medium; flows short |
| Cross-asset confirmation | Gold-silver ratio, silver direction, A-share miners, global miners | Precious-metal breadth and miner earnings confirmation | Gold isolated while silver/miners and flows deteriorate | Short/medium |

## 2. Indicator interpretation

### TIPS real yields

Use 5-year and 10-year real yields, with 10-year as the standard opportunity-cost anchor and 5-year as a more policy-sensitive cross-check. Observe the current level, 5-day and 20-day change, percentile or z-score, and whether the move comes from nominal yields or inflation breakevens. A fall from 2.2% to 1.9% can be tactically bullish even though 1.9% remains historically restrictive.

Avoid treating daily FRED constant-maturity estimates as executable prices. Market closure, interpolation, and liquidity can matter. For event analysis, pair them with Fed-funds futures or OIS pricing and the nominal Treasury curve.

### Federal Reserve path

Measure the change in expected policy, not only the latest official decision. Compare the number and timing of cuts/hikes priced before and after data releases or speeches. Easing is most gold-positive when it lowers real yields and weakens the dollar without already being fully discounted. “Cuts because inflation is solved” and “cuts because funding stress is acute” can generate different first-round price paths.

### Dollar

Use a broad dollar measure when possible; DXY is heavily weighted toward Europe and is not a complete trade-weighted index. Track correlation over rolling windows rather than assuming a fixed inverse relationship. Gold strength during a rising-dollar period is evidence of unusual underlying demand, but it is not by itself proof of a permanent decoupling.

For a China investor, split RMB gold return approximately into USD gold return, USD/CNY change, and local basis/premium. Do not attribute an RMB gold rally entirely to the global gold thesis.

### Liquidity and Treasury financing

Inspect Fed assets, TGA, ON RRP, bank reserves, SOFR/funding spreads, Treasury net marketable borrowing, bill-versus-coupon composition, and auction tails or bid-to-cover. Use the common net-liquidity identity only as a descriptive shortcut. Its components have different counterparties and transmission channels.

Large coupon issuance can raise term premium and real yields, pressuring gold at first. Persistent issuance can later support the long-term gold thesis if it worsens fiscal credibility. This is a horizon conflict, not a contradiction.

### Fiscal and monetary credibility

Use the primary deficit, total deficit, net interest outlays, debt maturity/refinancing needs, term premium, and the interaction between fiscal policy and central-bank independence. Debt level alone is insufficient. The relevant question is whether the expected real return on government liabilities remains credible without inflation, financial repression, or monetization.

### Central-bank and private flows

Official purchases are structural demand but are released with lags and revisions. Use them for medium/long-term analysis, not precise daily timing. Gold ETF holdings and CFTC futures positioning are timelier but can be crowded and reflexive. Rising price with rising ETF holdings is stronger private-demand confirmation than price rising only on short covering.

### Positioning and technical state

Use CFTC managed-money net length, open interest, ETF holdings, options skew when available, price trend, and distance from moving averages. Positioning answers “how vulnerable is the trade?” rather than “what is fair value?” A crowded long can keep rising if the macro catalyst strengthens; treat crowding as an asymmetry modifier. For trend, structure, momentum, volatility, and level-setting rules, read [technical-analysis.md](technical-analysis.md) rather than improvising an indicator checklist.

## 3. Gold-silver ratio states

Interpret the ratio with both metal prices:

| Gold | Silver | Ratio | Interpretation |
| --- | --- | --- | --- |
| Rising | Rising faster | Falling | Broad precious-metals bull/reflation; silver catch-up confirms risk appetite and industrial breadth |
| Rising | Flat or falling | Rising | Defensive or monetary gold leadership; can confirm stress but signals narrow breadth |
| Falling less | Falling faster | Rising | Risk-off relative outperformance, not an absolute gold bull signal |
| Falling faster | Stable or rising | Falling | Gold-specific weakness or unwind; bearish for gold despite lower ratio |

Use the ratio's percentile, 20-day change, and breakout/reversal behavior. Extreme levels are regime flags, not automatic mean-reversion trades.

## 4. Data transformations

For market series, prefer a compact transformation set:

- Current level and as-of timestamp.
- 1-day/5-day/20-day change for tactical variables.
- 3-month change for medium-term variables.
- Rolling 1-year percentile or z-score when the series is stable enough.
- Event-window change around CPI, payrolls, FOMC, Treasury refunding, or auctions.
- Rolling 60-day correlation with gold, reported as context rather than a law.

Use consistent local closes or explicitly acknowledge timing mismatches. Never combine a U.S. close, an Asian close, and a release timestamp as though they were simultaneous.

## 5. Common analytical errors

- Calling gold an inflation hedge without checking the real-rate response.
- Treating nominal-yield declines as bullish when inflation expectations fall even faster and real yields rise.
- Treating all Treasury issuance as identical, ignoring maturity mix and buyer funding source.
- Treating a high DXY as permanently bearish when crisis demand supports both assets.
- Counting Fed path, nominal yields, real yields, and DXY four times even though they reflect one macro shock.
- Using central-bank buying estimates for daily timing despite reporting lags.
- Calling miner outperformance a gold lead without checking the currency, costs, equity beta, and company events.
- Converting a qualitative long-run thesis into a precise short-term point target.
