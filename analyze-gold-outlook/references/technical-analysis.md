# Technical Analysis for Gold

## Contents

1. Role and boundary
2. Data and instrument discipline
3. Multi-timeframe workflow
4. Signal hierarchy
5. Key levels and targets
6. Macro and technical synthesis
7. Scoring and reporting
8. Failure modes

## 1. Role and boundary

Use technical analysis to answer three questions: whether price action confirms the macro thesis, whether the current location offers favorable timing, and where the thesis is invalidated. Technical analysis is strongest for days-to-months timing and risk definition. It is not a substitute for the real-rate, dollar, liquidity, fiscal-credit, or demand mechanisms that drive the medium- and long-term gold regime.

Start with market structure. Indicators summarize price and must not be counted as independent causal evidence. A bullish moving-average stack, positive MACD, and high RSI may all describe the same trend.

## 2. Data and instrument discipline

State the exact instrument: spot gold, LBMA benchmark, CME futures contract, continuous futures series, ETF, Shanghai gold, or RMB gold. Record timezone, session close, adjustment or roll method, and as-of timestamp. Do not mix spot levels with futures volume or open interest without saying so.

For a standard analysis, obtain adjusted open, high, low, and close data. Add exchange volume and open interest for futures when available. Use at least 250 daily observations for 200-day trend analysis and at least three years of weekly data for structural levels. If only a chart image is available, label all readings approximate.

## 3. Multi-timeframe workflow

Use top-down analysis and assign each timeframe a job:

| Decision horizon | Primary chart | Confirmation chart | Main task |
| --- | --- | --- | --- |
| Days to 6 weeks | Daily | 4-hour when reliable | Tactical trend, breakout quality, pullback risk, event levels |
| 1 to 6 months | Weekly and daily | Monthly for context | Swing structure, trend persistence, major support/resistance |
| 6 months to 3+ years | Monthly and weekly | Daily only for entry | Secular structure; macro regime remains authoritative |

On each chart, identify the latest confirmed swing high and low, the sequence of higher highs/higher lows or lower highs/lower lows, and whether price is trending, ranging, or transitioning. A close through a level is stronger than an intraday breach; require follow-through or a successful retest before treating a breakout as confirmed.

## 4. Signal hierarchy

Apply signals in this order:

1. **Price structure:** swing sequence, range boundaries, break of structure, failed breakout, and reclaim. Structure determines the primary technical state.
2. **Trend:** slope and ordering of the 20-, 50-, and 200-day moving averages, plus price position relative to them. Use weekly equivalents for longer horizons. Distance from trend is a stretch measure, not an automatic reversal signal.
3. **Momentum:** use RSI(14) and MACD(12,26,9) as confirmation. Look for momentum regime, acceleration/deceleration, and divergence only after structure is defined. Overbought can indicate strong trend persistence.
4. **Volatility:** use ATR(14), realized volatility, and optional Bollinger width to distinguish orderly trend, compression, breakout expansion, and unstable liquidation. Scale stops and scenario ranges to volatility.
5. **Participation:** use futures volume and open interest, ETF flows, and breadth across silver and miners. Rising price with expanding participation is stronger than a thin short-covering rally. Interpret price/open-interest combinations cautiously because positioning composition is not observable from open interest alone.

For event windows, compare price, real yields, and the dollar immediately before and after CPI, payrolls, FOMC decisions, Treasury refunding, auctions, or geopolitical shocks. Event reactions can reveal which macro variable the market currently treats as dominant.

## 5. Key levels and targets

Define support and resistance as zones using, in descending priority: repeated weekly/daily swing levels, former range boundaries, breakout/retest areas, high-volume or high-acceptance zones when transparent data are available, anchored VWAP from a disclosed major event, and major moving averages. Round numbers and Fibonacci retracements may be secondary confluence only; never present them as causal or precise by themselves.

Separate three types of levels:

- **Confirmation:** a close and hold beyond a level that raises confidence in the thesis.
- **Risk/invalidation:** a structural break that makes the current technical thesis wrong.
- **Target/reference:** a prior swing, measured move, ATR range, or options-implied range. State the method and timeframe.

Avoid exact point forecasts when data support only a zone. A technical target is a scenario reference, not a guaranteed destination.

## 6. Macro and technical synthesis

| Macro evidence | Technical evidence | Interpretation |
| --- | --- | --- |
| Bullish | Bullish | Higher-conviction long thesis; manage crowding and extension risk |
| Bullish | Bearish or deteriorating | Long-term thesis may remain intact, but timing is weak; wait for stabilization or lower conviction |
| Bearish | Bullish | Rally may be positioning-driven or anticipate a macro turn; require real-yield/dollar confirmation |
| Bearish | Bearish | Downside thesis is aligned; watch oversold liquidation and policy-response risk |

When macro and technical evidence diverge, state whether the conflict is across horizons, whether the macro catalyst is already priced, and the exact price or macro trigger that resolves it. Do not average the conflict into a vague neutral call.

## 7. Scoring and reporting

Collapse the complete technical diagnosis into one `technical_state` entry in the `cross_asset_positioning` family. Use horizon-specific impact and confidence. Technical evidence normally has material short-term impact, smaller medium-term impact, and no independent long-term impact.

Report the technical state in one substantive paragraph or compact table covering: trend/structure, momentum, volatility, participation, support/resistance zones, confirmation, invalidation, and whether it confirms the macro thesis. Explain the evidence behind the label; do not output only indicator values.

## 8. Failure modes

- Using a continuous futures series without disclosing roll adjustments.
- Calling a breakout from an intraday wick without a close, follow-through, or retest.
- Treating overbought RSI as an automatic sell signal in a strong trend.
- Counting correlated indicators as multiple independent confirmations.
- Drawing many levels until one fits the narrative.
- Optimizing moving-average windows or Fibonacci anchors on the same sample used to claim success.
- Letting a short-term oscillator reverse a structural macro conclusion without a change in price structure or causal regime.
