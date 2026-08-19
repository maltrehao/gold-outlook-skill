# Data Sources and Hygiene

## Contents

1. Source hierarchy
2. Primary-source map
3. Retrieval rules
4. Timestamp and revision rules
5. Minimum evidence set

## 1. Source hierarchy

Prefer, in order: official statistical and policy institutions; exchanges, index providers, and issuer filings; audited or methodologically transparent industry organizations; reputable data vendors and financial media. Use social media only to locate a claim, then verify it at the primary source.

Current analysis requires browsing. Cite direct pages or releases, not search-result pages. If a series is paywalled or inaccessible, state the limitation and use a disclosed proxy rather than inventing data.

## 2. Primary-source map

| Topic | Preferred source |
| --- | --- |
| Real yields, nominal yields, broad dollar, Fed balance sheet, reserves, TGA, ON RRP | Federal Reserve and FRED series pages; U.S. Treasury for account and financing data |
| Fed decisions and projections | Federal Reserve FOMC statements, minutes, SEP, speeches; market-implied paths from a disclosed futures/OIS source |
| Inflation, employment, growth | BLS, BEA, Census, and other responsible U.S. agencies |
| Treasury borrowing and issuance | U.S. Treasury Quarterly Refunding, TBAC materials, Monthly Statement, auction results, debt data |
| Futures positioning | CFTC Commitments of Traders |
| USD gold and silver benchmarks | LBMA or recognized exchange/market data with timestamp and contract disclosed |
| Technical price and derivatives data | A disclosed spot, futures, exchange, or ETF source with adjusted OHLC history; CME or the relevant exchange for volume and open interest |
| China gold price/premium | Shanghai Gold Exchange and other official exchange data |
| A-share miner prices and filings | Shanghai/Shenzhen exchanges, company filings, and a disclosed price provider |
| Gold ETF holdings | Fund sponsor filings/pages or a transparent aggregator with methodology |
| Central-bank and physical demand | IMF/official reserve disclosures, central-bank publications, and transparent industry datasets; note lags and estimates |

Do not hard-code a single ticker as “gold.” Specify spot, fix, front-month futures, continuous futures, or ETF. Roll methodology matters for futures.

## 3. Retrieval rules

For each material claim, record:

- Series or instrument name and identifier.
- Value, unit, observation date/time, and release date/time.
- Transformation: daily change, 20-day change, percentile, or revision.
- Source URL and access date.
- Known lag, revision, interpolation, or market-close issue.

Use market data that align in time. If alignment is impossible, write “directional comparison” and avoid precise event attribution.

## 4. Timestamp and revision rules

Economic data refer to a period, are released later, and may be revised. Never write “current inflation is X” without naming the reference month and release date. Market prices require time zone and close. Central-bank gold demand is often estimated and delayed; do not use the latest publication date as the transaction date.

Archive or state the as-of snapshot when reproducibility matters. If data were revised after the forecast date, do not silently substitute the revised series in a backtest.

## 5. Minimum evidence set

For a full current outlook, try to obtain at least:

1. USD gold and silver price direction; gold-silver ratio.
2. 5y and 10y U.S. real yields plus nominal/breakeven decomposition.
3. Fed path repricing and DXY/broad USD direction.
4. Treasury financing/liquidity context and current funding stress check.
5. ETF/CFTC positioning for tactical asymmetry.
6. Central-bank or official demand for structural context.
7. RMB gold and USD/CNY when serving a China-based investor.
8. A-share pure-play gold basket breadth, excess return, and attribution when using miner signals.
9. Adjusted OHLC history, volume/open interest when available, and the exact instrument/contract used for technical analysis.

If several elements are unavailable, produce a scoped answer and clearly list the missing evidence that could change the conclusion.
