# DuxCharts

Market intelligence for Indian equities. It describes what the market is doing
and shows you comparable days from history, with an explanation attached to
every figure. It does not tell you what to trade.

Built around NSE data going back to 2000, including the Closing Auction Session
that NSE introduced in August 2026.

---

## What it does

**Describes the current state.** Trend, volatility, momentum and activity for
NIFTY 50, BANK NIFTY and selected stocks, computed from 26 years of daily data
and summarised in plain language.

**Finds comparable days.** Every trading day is reduced to a vector of its
indicator values. Given a day, the system retrieves the historically closest
sessions and shows what happened next on each of them, as a distribution. This
is nearest-neighbour retrieval over standardised features, not a forecast, and
it is presented as precedent.

**Analyses the Closing Auction Session.** NSE replaced its closing-price
mechanism with a call auction on 3 August 2026. DuxCharts holds every daily CAS
report published since launch and measures how the auction behaves.

**Treats data as something to verify, not trust.** Every ingested file is
hashed and recorded in an audit log, so any number on screen traces back to a
known source file.

## Findings so far

From 11,986 auction observations across 215 stocks over the first 57 trading
days of CAS:

- The auction price **is** the official close. Verified on 228 matched
  observations against an independent data provider: exact agreement, every time.
- Between **4.6% and 7.5%** of a stock's entire daily volume now trades in those
  few closing minutes.
- The auction moves price a median of **0.25%** from its reference. Half of all
  auctions move it more than that; 4.3% move it more than 1%.
- **60% of auctions close above their reference price**, a persistent upward
  bias in the launch regime that does not appear to be documented elsewhere.

A measured honesty check on the similarity search: neighbour direction agrees
with the next session's actual direction **53.5%** of the time, against a base
rate of **53.6%**. There is no predictive edge, and the feature is presented
accordingly.

## Architecture

```
analysis/   Python. Ingestion, indicators, similarity search, CAS statistics.
            Runs offline and writes results to MongoDB.
server/     Node + Express REST API. Authentication, roles, ownership checks,
            input validation, rate limiting.
web/        React dashboard.
```

Analysis is computed ahead of time and stored; the API only reads. The
dashboard never touches the database.

**Stack:** Python (pandas, NumPy, scikit-learn) · MongoDB Atlas via Mongoose ·
Node + Express · React + Vite.

## Data

| Source | Use |
|---|---|
| investing.com | Daily OHLCV, 2000 to present, six instruments |
| NSE Closing Auction Session reports | Daily auction data since 3 Aug 2026 |
| Yahoo Finance | Independent cross-check and daily refresh |

Daily prices were validated day by day against an independent provider:
**99.98%** of 4,502 overlapping sessions matched within 0.01%. NSE publishes the
CAS report in four different column layouts; the loader maps all of them onto one
canonical schema through an alias table.

Data files are not committed. The pipeline regenerates them.

## Status

| Component | State |
|---|---|
| Data pipeline and verification | Complete |
| Indicator engine | Complete |
| Similarity search | In progress |
| MongoDB layer | In progress |
| REST API and security layer | In progress |
| React dashboard | In progress |

Target for the first working release: **30 November 2026.**
Forecasting and strategy backtesting come after, with walk-forward validation
and probability calibration.

## Running it

```bash
python -m venv .venv && ./.venv/bin/pip install -r analysis/requirements.txt
./.venv/bin/python analysis/indicators.py
```

API and dashboard setup will be documented as they land.

## A note on what this is not

DuxCharts is a research and education tool. It places no orders, connects to no
broker, and issues no buy or sell recommendations. In India, publishing
investment recommendations falls under SEBI's Research Analyst framework; this
project stays outside that by design, explaining market behaviour rather than
advising on it. Nothing here is investment advice, and past behaviour of a
market says nothing reliable about its future.

## License

See `LICENSE`.
