Show me Phase 0 notes in markdown format

Below is the complete **Phase 0 — Murex Orientation** notes in Markdown format. Save it in your Git repository as:

```text
phase-0-orientation/phase-0-murex-orientation.md
```

```markdown
# Phase 0 — Murex Orientation

## 1. Purpose of Phase 0

Phase 0 builds the foundation for learning Murex MX.3.

Before learning Murex screens, Datamart, MxML, MSL, or production support,
you must understand:

- What Murex is
- Where Murex is used in a bank
- Who uses Murex
- How a trade moves through the system
- What static data and market data mean
- How Murex connects to reporting and other systems
- What a Production Support person is expected to know

After Phase 0, you should be able to explain the complete Murex ecosystem
in simple business language.

---

## 2. What is Murex MX.3?

### Simple definition

Murex MX.3 is an integrated capital-markets platform used by banks and
financial institutions for:

- Trading
- Treasury
- Risk management
- Collateral management
- Operations
- Finance and accounting
- Regulatory reporting
- Data management
- Integration with upstream and downstream systems

### Telugu-English explanation

Murex ante bank lo trade enter chesina taruvata, aa trade ki price, risk,
settlement, accounting, reporting anni systems madhya connect ayi process
avvadaniki use ayye platform.

Example:

A trader books an FX Forward in Murex. The same trade can be used for:

- Confirmation
- Settlement
- Risk calculation
- Accounting
- Datamart reporting
- Regulatory reporting
- Reconciliation

---

## 3. Why Banks Use Murex

Banks use Murex because it provides one connected platform for many
front-office, middle-office, back-office, risk, and finance activities.

| Business Need | How Murex Helps |
|---|---|
| Trade booking | Capture and manage trades |
| Pricing and valuation | Calculate price, MTM, P&L |
| Risk management | Calculate exposure, limits, market risk |
| Operations | Manage confirmation and settlement |
| Finance | Generate accounting events and financial reporting |
| Collateral | Manage collateral agreements and margin |
| Reporting | Feed data to Datamart, BI, regulatory reports |
| Integration | Exchange data with upstream/downstream systems |

---

## 4. Murex in a Bank

### Front Office

Front Office users are mainly traders and sales teams.

They use Murex to:

- Book trades
- View positions
- Check pricing
- Monitor P&L
- Manage trading books

Example:

A trader books an FX Forward to buy USD 1 million against INR for a
future value date.

### Middle Office

Middle Office controls and validates trades.

They may handle:

- Trade validation
- Risk checks
- Confirmations
- Exception management
- Trade amendments
- Business controls

### Back Office

Back Office handles post-trade processing.

They manage:

- Settlement
- Payments
- Cash flows
- Clearing
- Accounting
- Reconciliation

### Risk

Risk teams use Murex to understand exposure and potential losses.

They monitor:

- Market risk
- Credit exposure
- Counterparty exposure
- Limits
- Stress scenarios
- VaR concepts

### Finance

Finance teams use Murex for:

- Accounting
- Accruals
- P&L
- General Ledger reporting
- Financial reconciliation

### Technology and Support

Technology teams support:

- Murex application
- Interfaces
- Batch jobs
- EOD processing
- Datamart
- MxML integration
- Database and infrastructure
- Incident and problem management

---

## 5. Murex MX.3 Architecture Overview

You do not need deep infrastructure knowledge at the beginning.
For support and techno-functional work, understand these layers:

| Layer | Plain Meaning | Why It Matters |
|---|---|---|
| Presentation | Desktop/web user interface | Users view trades, reports, and workspaces |
| Business | Pricing, workflow, risk, accounting, collateral engines | Business calculations and rules happen here |
| Orchestration | Coordinates processing and distributes tasks | Important for multi-step jobs and dependencies |
| Technical Services | Authentication, authorization, messaging, caching, logging | Used for access, service, and interface issues |
| Data / Datamart | Financial database and reporting structures | Important for SQL, feeders, extracts, reconciliation |
| Integration | Connects Murex with external systems | Important for MxML, files, APIs, confirmations |

### Simplified architecture flow

```text
User / Upstream System
        ↓
Presentation Layer
        ↓
Business Layer
        ↓
Orchestration Layer
        ↓
Technical Services
        ↓
Murex Data / Datamart
        ↓
Reports / Extracts / Downstream Systems
```

---

## 6. Trade Lifecycle Overview

This is the most important flow to remember.

```text
Trade Input
→ Validation
→ Enrichment
→ Booking
→ Workflow
→ Valuation / P&L / Risk
→ Confirmation
→ Settlement
→ Accounting
→ Datamart Feeder
→ Report / Extract
→ Reconciliation
```

### Example: FX Forward

Assume a bank books an FX Forward:

- Buy USD 1,000,000
- Sell INR
- Trade date: 14-Oct-2026
- Value date: 14-Jan-2027
- Counterparty: Bank A
- Book: India FX Book

The trade may move through:

```text
Trade captured
→ Validated
→ Enriched with counterparty/book/calendar data
→ Booked
→ Workflow updated
→ Valuation calculated
→ Confirmation generated
→ Settlement prepared
→ Accounting events created
→ Datamart feeder processed
→ Report generated
→ Reconciliation performed
```

---

## 7. Core Murex Terminology

| Term | Meaning |
|---|---|
| Trade | A financial transaction agreed between two parties |
| Contract | Economic agreement and terms behind a transaction |
| Event | Lifecycle action such as booking, fixing, payment, amendment, cancellation |
| Cash Flow | Expected payment or receipt created by a trade |
| Book | Business/trading ownership grouping for trades |
| Portfolio | Collection of trades/positions for analysis or reporting |
| Position | Net exposure created by one or more trades |
| Counterparty | External party with whom the bank trades |
| Legal Entity | Legally registered bank/company entity that owns or enters the trade |
| Static Data | Relatively stable reference data such as counterparty, book, calendar, SSI |
| Market Data | Rates, curves, FX prices, volatility, fixings used for valuation/risk |
| Workflow | States and tasks that control how an object is processed |
| Datamart | Reporting-oriented data layer for reports/extractions |
| MxML | Murex XML-based integration framework for messages/business objects |
| MSL | Murex Scripting Language for business validation, enrichment, routing rules |
| Batch / EOD | Scheduled processing, especially end-of-day valuation/risk/reporting |

---

## 8. Static Data vs Market Data

| Item | Static Data | Market Data |
|---|---|---|
| Meaning | Reference data used repeatedly | Current market observations |
| Example | Counterparty, book, calendar, currency, SSI | FX rate, yield curve, fixing, volatility |
| Changes | Less frequently | Can change frequently |
| Used for | Trade validation, enrichment, settlement | Pricing, valuation, risk |
| Example issue | Inactive counterparty | Missing FX rate or stale curve |

### Example

For an FX Forward:

- Counterparty, book, calendar, and settlement instruction are static data.
- FX spot rate, forward points, and discount curve are market data.

---

## 9. Murex Environments

| Environment | Purpose |
|---|---|
| DEV | Configuration/development work |
| SIT | Systems and interfaces tested together |
| UAT | Business users validate requirements and scenarios |
| Pre-Production | Production-like validation before release, where used |
| PROD | Live business processing |

### Environment flow

```text
DEV
→ SIT
→ UAT
→ Pre-Production
→ PROD
```

---

## 10. Murex Support Ecosystem

Murex does not work alone. It connects with many systems.

```text
Upstream Systems
→ Murex
→ Datamart / Reports
→ Downstream Systems
→ Reconciliation
```

Examples of connected systems:

| System Type | Examples |
|---|---|
| Upstream trade source | Dealing platform, order management system, front-office system |
| Market-data source | Rates, curves, FX prices, volatility provider |
| Confirmation system | SWIFT, confirmation platform |
| Settlement system | Payment system, clearing system |
| Risk system | Risk engine, limit system |
| Reporting system | Datamart, BI tool, regulatory reporting system |
| Scheduler | Control-M or similar batch scheduler |
| Database | Murex database and reporting database |

---

## 11. Typical Murex Support Responsibilities

A Murex Production Support person may need to:

- Monitor batch jobs and EOD processing
- Investigate failed interfaces
- Analyze logs
- Check trade status and workflow
- Validate static data and market data
- Run SQL queries for reconciliation
- Support Datamart/reporting issues
- Support MxML message failures
- Raise and update incidents
- Prepare RCA and runbooks
- Coordinate with business, development, and infrastructure teams

---

## 12. Important Support Mindset

For every issue, collect:

```text
1. What is the business impact?
2. Which trade/report/message is affected?
3. Which environment and business date?
4. What is the expected result?
5. What is the actual result?
6. Which job/interface failed?
7. What error appears in the log?
8. What changed recently?
9. What is the next safe action?
```

---

## 13. Phase 0 Cheat Sheet

```text
Murex = integrated capital-markets platform.

Front Office = trades.
Middle Office = controls and validations.
Back Office = settlement and operations.
Risk = exposure and limits.
Finance = accounting and P&L.
Technology = support, batch, integration, reporting.

Main flow:
Trade → Validation → Booking → Workflow → Valuation
→ Confirmation → Settlement → Accounting → Datamart → Report.

Static data = reference data.
Market data = valuation/risk data.

Murex support = logs + batch + SQL + workflow + data + business impact.
```

---

## 14. Phase 0 Revision Questions

1. What is Murex MX.3?
2. Which teams use Murex in a bank?
3. What is the difference between Front Office and Back Office?
4. What is the difference between static data and market data?
5. What is a trade lifecycle?
6. What is a Datamart?
7. What is MxML?
8. What is MSL?
9. Why is Control-M important in Murex support?
10. What information should you collect before investigating a Murex issue?

---

## 15. Practical Assignment

Draw one diagram in your notebook or in Markdown:

```text
Murex Trade-to-Report Flow
```

Include:

- Upstream system
- Trade capture
- Validation
- Workflow
- Valuation
- Confirmation
- Settlement
- Accounting
- Datamart
- Report
- Reconciliation

Then explain the diagram aloud in 2 minutes.

---

## 16. Next Chapter

Next, study:

```text
Phase 0, Chapter 1:
What is Murex MX.3?
```

Then continue with:

```text
Capital Markets Bank Functions
→ MX.3 Architecture
→ Trade Lifecycle
→ Core Terminology
→ Environments, Access, and Audit
```
```

This is your **Phase 0 base notes**. After you save it, the next step is to expand it into individual detailed chapters, starting with:

```text
Phase 0, Chapter 1: What is Murex MX.3?
```

