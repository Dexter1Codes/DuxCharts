# Capstone session: AI-Driven Intraday Market Intelligence and Decision Support

Loaded automatically when Claude Code starts in this folder. This session plans and
builds the university capstone. DSA, interview theory, applications and overall
planning live in other sessions.

## The project

An interactive market intelligence platform for the Indian market (NIFTY, BANK NIFTY,
selected stocks) that helps intraday traders understand market behaviour. Objectives
from the proposal: market analysis (trend, volatility, momentum, activity),
probabilistic forecasting of short-term moves, historical pattern comparison, strategy
evaluation on historical data with simulated trading, analysis of NSE's new Closing
Auction Session (CAS), and decision support with explanations. Research and simulation
only, no real trades, no guaranteed profits. Evaluated on historical data with measurable
criteria.

Keep it educational: no public buy/sell recommendations, because publishing those in
India falls under SEBI Research Analyst regulation.

## Team and time

- **Me (Dhairya):** most of the development. I plan in outcomes, not hours: each day has one
  capstone deliverable ("login route working with tests", "teammates' data loaded"). I'm also using this project to learn React, Node/Express and MongoDB, so
  explain decisions as we build; don't just hand me finished code.
- **Two teammates:** Data Science specialisation, 5–6 hours a week each. They own
  research and data: sourcing, cleaning, analysis, and later the models.

## Deadline

A working basic version goes to the faculty in **the first week of December 2026**.
So it must be demo-ready by **30 November**. Final defence around April–May 2027.

## Proposed stack and December scope (to confirm with me first)

- **Data (teammates):** historical + daily data for NIFTY, BANK NIFTY and a few stocks,
  including CAS data. Python scripts that clean it and write to MongoDB.
- **Analysis (teammates):** indicators (trend, volatility, momentum), a simple
  "days like today" historical comparison, CAS statistics. Python, writing results to MongoDB.
- **Backend (me):** Node + Express REST API over MongoDB.
- **Frontend (me):** React dashboard: market overview, indicators, similar historical days, CAS view.
- **Security layer (me), my differentiator:** login with roles, ownership checks, rate
  limiting, input validation, a hash of every ingested data file plus an audit log of
  ingestion. On my SDE resume this project leads with the full stack; on my security
  resume it leads with this layer. Both framings must stay true.
- **After December (Jan–Mar):** probabilistic forecasting model, strategy simulation and
  backtesting, deeper explanations.

## First tasks for this session

1. Agree the December scope with me, item by item.
2. Write a **full task description for each teammate**: what to build, inputs, outputs,
   file and data formats, where results land in MongoDB, how "done" is checked, and dates.
3. Write the **dependency map**: what I'm blocked on from them, what they're blocked on
   from me, and the interfaces that unblock both sides early (the MongoDB collections and
   document shapes, the API contract), so nobody waits on anybody.
4. A milestone timeline from now to 30 November, by week, for all three of us.
5. Then set up the repo and start building.

## Shared state

- Daily sheet (I tick outcomes there; capstone milestones show on its Goals view): https://claude.ai/code/artifact/e527805f-2dbc-45e2-b728-242e889b3d33
- Plan file, read only from here: `/mnt/c/Users/dhair/Documents/appsec/TASKS.md`
- Don't change the plan or the sheet from here. Bring milestone dates back to the
  planning session so the tracker can show them.

## How I plan

Outcomes, never hours. Break the work into deliverables small enough to finish in a
day, each with a clear "done" (working, tested where it matters, committed). The
milestone timeline you write should be deliverables with an owner and a week, which the
planning session puts on my Goals tracker.
