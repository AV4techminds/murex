# Murex Functional Consultant — Master 200+ Concept Checklist

> **Purpose:** Complete Murex Functional foundation from absolute zero to interview-ready level.
>
> **Scope:** Capital Markets + FO + MO + BO + Murex functional modules + products + lifecycle + risk/P&L + settlement + accounting + regulatory + EOD/SOD + functional configuration/testing + production scenarios.
>
> **Tracking rule:** Mark `[x]` only when you can explain the concept, its purpose, its place in the lifecycle, and at least one banking/Murex example.

---

# 1. Capital Markets Foundation

## 1.1 Banking & Markets
- [ ] Investment Banking
- [ ] Capital Markets
- [ ] Buy Side
- [ ] Sell Side
- [ ] Commercial Banking vs Investment Banking
- [ ] Trading Desk
- [ ] Treasury
- [ ] Operations
- [ ] Finance
- [ ] Risk
- [ ] Compliance
- [ ] Regulatory Reporting
- [ ] Market Participants
- [ ] Broker
- [ ] Dealer
- [Exchange]
- [ ] Clearing House
- [ ] Central Counterparty (CCP)

## 1.2 Core Trading Terms
- [ ] Trade
- [ ] Transaction
- [ ] Position
- [ ] Portfolio
- [ ] Book
- [ ] Counterparty
- [ ] Legal Entity
- [ ] Trader
- [ ] Desk
- [ [ ] Account
- [ ] Instrument
- [ ] Product
- [ ] Market Data
- [ ] Static Data
- [ ] Reference Data
- [ ] Market Value
- [ ] Notional
- [ ] Price
- [ ] Rate
- [ ] Currency
- [ ] Settlement
- [ ] Clearing
- [ ] Collateral

---

# 2. FO / MO / BO — Core Operating Model

## 2.1 Front Office (FO)
- [ ] What is Front Office?
- [ ] Trading Desk
- [ ] Trader
- [ ] Sales
- [ ] Structuring
- [ ] Trade Idea
- [ ] Price Discovery
- [ ] Quote
- [ ] Trade Negotiation
- [ ] Trade Capture
- [ ] Trade Booking
- [ ] Trade Amendment
- [ ] Trade Cancellation
- [ ] Trade Confirmation
- [ ] Position Visibility
- [ ] P&L Visibility
- [ ] Risk Visibility
- [ ] Limit Checks
- [ ] Pre-Trade Checks
- [ ] Post-Trade Checks

## 2.2 Middle Office (MO)
- [ ] What is Middle Office?
- [ ] Trade Validation
- [ ] Trade Enrichment
- [ ] Trade Verification
- [ ] Trade Confirmation Monitoring
- [ ] Position Control
- [ ] P&L Control
- [ ] Risk Control
- [ ] Limit Monitoring
- [ ] Exposure Monitoring
- [ ] Counterparty Risk Checks
- [ ] Market Risk Checks
- [ ] Credit Risk Checks
- [ ] Trade Lifecycle Monitoring
- [ ] Exception Management
- [ ] Break Management
- [ ] Reconciliation
- [ ] Static Data Control
- [ ] Market Data Control
- [ ] Settlement Instruction Validation
- [ ] Regulatory Control
- [ ] End-of-Day Controls

## 2.3 Back Office (BO)
- [ ] What is Back Office?
- [ ] Settlement
- [ ] Payment Processing
- [ ] Delivery
- [ ] Receipt
- [ ] Settlement Instructions
- [ ] SSI
- [ ] Confirmation Processing
- [ ] Matching
- [ ] Clearing
- [ ] Netting
- [ ] Cash Settlement
- [ ] Securities Settlement
- [ ] Failed Settlement
- [ ] Settlement Status
- [ ] Payment Status
- [ ] Nostro
- [ ] Custodian
- [ ] Correspondent Bank
- [ ] Accounting
- [ ] GL Posting
- [ ] Reconciliation
- [ ] Corporate Actions
- [ ] Back Office Reporting

## 2.4 FO → MO → BO Relationship
- [ ] End-to-End Operating Model
- [ ] FO Trade Capture → MO Control → BO Settlement
- [ ] FO/MO/BO Data Handover
- [ ] Trade Status Lifecycle
- [ ] Exception Flow
- [ ] Break Resolution
- [ ] Reconciliation Flow
- [ ] Escalation Flow
- [ ] Business Day / EOD Flow

---

# 3. Murex / MX.3 Functional Foundation

- [ ] What is Murex?
- [ ] What is MX.3?
- [ ] Why banks use Murex
- [ ] Murex front-to-back scope
- [ ] Murex architecture — functional view
- [ ] Murex modules
- [ ] Murex user roles
- [ ] Murex environments
- [ ] Murex data concepts
- [ ] Murex trade lifecycle
- [ ] Murex workflow concepts
- [ ] Murex static data
- [ ] Murex market data
- [ ] Murex position
- [ ] Murex risk
- [ ] Murex P&L
- [ ] Murex settlement
- [ ] Murex accounting
- [ ] Murex reporting
- [ ] Murex Datamart
- [ ] Murex regulatory reporting

---

# 4. Trade Lifecycle — Deep Dive

## 4.1 Trade Creation
- [ ] Trade Idea
- [ ] Quote
- [ ] Negotiation
- [ ] Execution
- [ ] Trade Capture
- [ ] Trade Booking
- [ ] Trade ID
- [ ] Trade Date
- [ ] Value Date
- [ ] Maturity Date

## 4.2 Trade Processing
- [ ] Validation
- [ ] Enrichment
- [ ] Static Data Lookup
- [ ] Market Data Lookup
- [ ] Counterparty Enrichment
- [ ] Settlement Instruction Enrichment
- [ ] Product Validation
- [ ] Limit Validation
- [ ] Risk Validation
- [ ] Confirmation
- [ ] Matching
- [ ] Settlement Preparation
- [ ] Accounting Preparation

## 4.3 Trade Lifecycle Events
- [ ] New Trade
- [ ] Amendment
- [ ] Partial Amendment
- [ ] Cancellation
- [ ] Exercise
- [ ] Expiry
- [ ] Early Termination
- [ ] Novation
- [ ] Assignment
- [ ] Unwind
- [ ] Compression
- [ ] Rollover
- [ ] Reset
- [ ] Fixing

## 4.4 Trade Status
- [ ] New
- [ ] Validated
- [ ] Confirmed
- [ ] Matched
- [ ] Settled
- [ ] Failed
- [ ] Cancelled
- [ ] Matured
- [ ] Expired
- [ ] Rejected

---

# 5. Financial Products — Functional Understanding

## 5.1 FX
- [ ] FX Market
- [ ] Currency Pair
- [ ] Base Currency
- [ ] Quote Currency
- [ ] FX Spot
- [ ] FX Forward
- [ ] FX Swap
- [ ] FX Option
- [ ] Value Date
- [ ] Spot Date
- [ ] Forward Points
- [ ] FX Settlement

## 5.2 Money Market
- [ ] Deposits
- [ ] Loans
- [ ] Borrowing
- [ ] Lending
- [ ] Interest Calculation
- [ ] Maturity
- [ ] Money Market Settlement

## 5.3 Fixed Income
- [ ] Bond
- [ ] Issuer
- [ ] Face Value
- [ ] Coupon
- [ ] Coupon Frequency
- [ ] Maturity
- [ ] Yield
- [ ] Clean Price
- [ ] Dirty Price
- [ ] Accrued Interest
- [ ] Bond Settlement
- [ ] Amortization

## 5.4 Interest Rates
- [ ] Interest Rate
- [ ] Yield Curve
- [ ] Zero Curve
- [ ] Discount Factor
- [ ] Forward Rate
- [ ] Floating Rate
- [ ] Fixed Rate
- [ ] Interest Rate Swap
- [ ] Pay Fixed
- [ ] Receive Fixed
- [ ] Reset
- [ ] Fixing
- [ ] Swap Cashflows

## 5.5 Derivatives
- [ ] Derivative
- [ ] Futures
- [ ] Options
- [ ] Call
- [ ] Put
- [ ] Strike
- [ ] Premium
- [ ] Expiry
- [ ] Exercise
- [ ] Swaption
- [ ] OTC Derivative
- [ ] Exchange-Traded Derivative

## 5.6 Equity / Credit / Commodity
- [ ] Equity
- [ ] Equity Trade
- [ ] Dividend
- [ ] Equity Derivative
- [ ] Credit Risk
- [ ] Credit Default Swap
- [ ] Commodity
- [ ] Commodity Future
- [ ] Commodity Option

---

# 6. Static Data

- [ ] What is Static Data?
- [ ] Why Static Data matters
- [ ] Legal Entity
- [ ] Counterparty
- [ ] Customer
- [ ] Trader
- [ ] Desk
- [ ] Book
- [ ] Portfolio
- [ ] Product
- [ ] Instrument
- [ ] Currency
- [ ] Calendar
- [ ] Business Day Convention
- [ ] Holiday Calendar
- [ ] Settlement Instruction
- [ ] SSI
- [ ] Account
- [ ] Payment Method
- [ ] Netting Set
- [ ] Legal Agreement
- [ ] Reference Data Hierarchy
- [ ] Static Data Dependencies
- [ ] Static Data Validation
- [ ] Static Data Change Management

---

# 7. Market Data

- [ ] What is Market Data?
- [ ] Market Data Sources
- [ ] Price
- [ ] FX Rate
- [ ] Interest Rate
- [ ] Yield
- [ ] Curve
- [ ] Discount Curve
- [ ] Forward Curve
- [ ] Volatility
- [ ] Credit Spread
- [ ] Fixing
- [ ] Market Data Snapshot
- [ ] Historical Market Data
- [ ] Real-Time Market Data
- [ ] End-of-Day Market Data
- [ ] Missing Market Data
- [ ] Stale Market Data
- [ ] Incorrect Market Data
- [ ] Market Data Validation
- [ ] Market Data Hierarchy

---

# 8. Front Office — Detailed Functional Module

## 8.1 Trading
- [ ] Trading Workspace
- [ ] Trade Entry
- [ ] Product Selection
- [ ] Counterparty Selection
- [ ] Book Selection
- [ ] Notional
- [ ] Price
- [ ] Rate
- [ ] Currency
- [ ] Dates
- [ ] Trade Validation
- [ ] Trade Booking

## 8.2 Trader View
- [ ] Open Trades
- [ ] Positions
- [ ] P&L
- [ ] Market Value
- [ ] Risk
- [ ] Limits
- [ ] Exposure
- [ ] Trade Search
- [ ] Trade Modification
- [ ] Trade Cancellation

## 8.3 FO Controls
- [ ] Pre-Trade Validation
- [ ] Limit Check
- [ ] Credit Check
- [ ] Market Risk Check
- [ ] Static Data Check
- [ ] Product Eligibility
- [ ] Trading Permission
- [ ] Exception Handling

---

# 9. Middle Office — Detailed Functional Module

## 9.1 Trade Control
- [ ] Trade Validation
- [ ] Trade Enrichment
- [ ] Trade Completeness
- [ ] Trade Status
- [ ] Confirmation Status
- [ ] Matching Status
- [ ] Settlement Status

## 9.2 Risk & Control
- [ ] Position Control
- [ ] P&L Control
- [ ] Market Risk
- [ ] Credit Risk
- [ ] Counterparty Exposure
- [ ] Limit Monitoring
- [ ] Concentration
- [ ] Sensitivities
- [ ] Stress Testing
- [ ] Exception Monitoring

## 9.3 Reconciliation
- [ ] FO vs MO Reconciliation
- [ ] Murex vs External System
- [ ] Trade Count
- [ ] Notional
- [ ] Position
- [ ] P&L
- [ ] Cash
- [ ] Settlement
- [ ] Break Identification
- [ ] Break Classification
- [ ] Break Resolution

---

# 10. Risk Management

- [ ] Market Risk
- [ ] Credit Risk
- [ ] Counterparty Risk
- [ ] Liquidity Risk
- [ ] Operational Risk
- [ ] Exposure
- [ ] Position
- [ ] Sensitivity
- [ ] Greeks
- [ ] Delta
- [ ] Gamma
- [ ] Vega
- [ ] Theta
- [ ] PV01
- [ ] DV01
- [ ] VaR
- [ ] Stress Testing
- [ ] Scenario Analysis
- [ ] Limit
- [ ] Limit Breach
- [ ] Risk Aggregation
- [ ] Risk by Desk
- [ ] Risk by Book
- [ ] Risk by Counterparty
- [ ] Risk by Product

---

# 11. P&L and Valuation

- [ ] What is P&L?
- [ ] Realized P&L
- [ ] Unrealized P&L
- [ ] Mark-to-Market
- [ ] Market Value
- [ ] Fair Value
- [ ] Valuation
- [ ] Profit
- [ ] Loss
- [ ] P&L Attribution
- [ ] Price Effect
- [ ] Rate Effect
- [ ] FX Effect
- [ ] Time Effect
- [ ] New Trade P&L
- [ ] Carry
- [ ] Accrual
- [ ] P&L Explain
- [ ] Daily P&L
- [ ] Month-to-Date P&L
- [ ] Year-to-Date P&L

---

# 12. Position Management

- [ ] What is Position?
- [ ] Position by Book
- [ ] Position by Desk
- [ ] Position by Product
- [ ] Position by Currency
- [ ] Long Position
- [ ] Short Position
- [ ] Net Position
- [ ] Gross Position
- [ ] Intraday Position
- [ ] End-of-Day Position
- [ ] Position Aggregation
- [ ] Position Reconciliation
- [ ] Position Break
- [ ] Position Adjustment

---

# 13. Back Office — Detailed Functional Module

## 13.1 Settlement
- [ ] Settlement Lifecycle
- [ ] Settlement Date
- [ ] Settlement Amount
- [ ] Cash Settlement
- [ ] Securities Settlement
- [ ] Delivery vs Payment
- [ ] Free of Payment
- [ ] Settlement Instruction
- [ ] SSI
- [ ] Settlement Matching
- [ ] Settlement Confirmation
- [ ] Settlement Failure
- [ ] Failed Trade
- [ ] Re-Settlement
- [ ] Settlement Netting

## 13.2 Payments
- [ ] Payment
- [ ] Receipt
- [ ] Payment Instruction
- [ ] Payment Status
- [ ] Payment Failure
- [ ] Payment Repair
- [ ] Nostro
- [ ] Correspondent Bank
- [ ] Custodian
- [ ] Bank Account

## 13.3 Post-Trade
- [ ] Confirmation
- [ ] Matching
- [ ] Clearing
- [ ] Netting
- [ ] Settlement
- [ ] Accounting
- [ ] Reconciliation
- [ ] Corporate Actions

---

# 14. Accounting

- [ ] Trading Book Accounting
- [ ] Banking Book Accounting
- [ ] Accounting Event
- [ ] Accounting Rule
- [ ] Debit
- [ ] Credit
- [ ] Journal
- [ ] General Ledger
- [ ] GL Account
- [ ] Accounting Date
- [ ] Value Date
- [ ] Accrual
- [ ] Amortization
- [ ] Realized P&L
- [ ] Unrealized P&L
- [ ] Revaluation
- [ ] Accounting Reconciliation
- [ ] Sub-Ledger
- [ ] General Ledger Integration

---

# 15. Collateral

- [ ] What is Collateral?
- [ ] Collateral Agreement
- [ ] Margin
- [ ] Initial Margin
- [ ] Variation Margin
- [ ] Collateral Call
- [ ] Collateral Eligibility
- [ ] Haircut
- [ ] Collateral Valuation
- [ ] Collateral Settlement
- [ ] Collateral Reconciliation

---

# 16. Treasury

- [ ] Treasury Function
- [ ] Liquidity
- [ ] Funding
- [ ] Cash Position
- [ ] Cash Forecast
- [ ] Liquidity Risk
- [ ] Funding Requirement
- [ ] Treasury Trade
- [ ] Intercompany Funding
- [ ] Cash Management
- [ ] Nostro Management

---

# 17. Regulatory Reporting

- [ ] Regulatory Reporting Fundamentals
- [ ] Regulatory Data
- [ ] Data Lineage
- [ ] Regulatory Templates
- [ ] Reporting Population
- [ ] Reporting Cutoff
- [ ] Regulatory Validation
- [ ] Regulatory Reconciliation
- [ ] Exception Management
- [ ] Auditability
- [ ] Submission
- [ ] Resubmission
- [ ] Regulatory Adjustments
- [ ] RWA
- [ ] Capital Requirements
- [ ] Leverage Ratio
- [ ] Exposure
- [ ] Basel Concepts
- [ ] PRA
- [ ] ECB
- [ ] MAS
- [ ] HKMA

---

# 18. EOD / SOD

## 18.1 Start of Day
- [ ] SOD Concept
- [ ] Market Data Load
- [ ] Static Data Validation
- [ ] Position Initialization
- [ ] Opening Balances
- [ ] Batch Dependencies
- [ ] SOD Controls

## 18.2 End of Day
- [ ] EOD Concept
- [ ] Trade Cutoff
- [ ] Trade Validation
- [ ] Market Data Load
- [ ] Valuation
- [ ] P&L
- [ ] Risk
- [ ] Position
- [ ] Settlement
- [ ] Accounting
- [ ] Datamart
- [ ] Reporting
- [ ] Reconciliation
- [ ] EOD Controls
- [ ] EOD Failure Handling

---

# 19. Murex Workflow & Functional Configuration

- [ ] Workflow Concept
- [ ] Workflow States
- [ ] Workflow Transitions
- [ ] Validation Rules
- [ ] Business Rules
- [ ] Eligibility Rules
- [ ] Product Configuration
- [ ] Static Data Configuration
- [ ] Market Data Configuration
- [ ] Settlement Configuration
- [ ] Accounting Configuration
- [ ] Reporting Configuration
- [ ] User Roles
- [ ] Permissions
- [ ] Functional Parameters
- [ ] Calendars
- [ ] Business Day Rules
- [ ] Approval Flow
- [ ] Exception Flow

---

# 20. Functional Testing

- [ ] Requirement Analysis
- [ ] Functional Specification
- [ ] Test Scenario
- [ ] Test Case
- [ ] Test Data
- [ ] Expected Result
- [ ] Actual Result
- [ ] Positive Testing
- [ ] Negative Testing
- [ ] Boundary Testing
- [ ] Regression Testing
- [ ] Integration Testing
- [ ] SIT
- [ ] UAT
- [ ] Smoke Testing
- [ ] Production Validation
- [ ] Defect
- [ ] Defect Lifecycle
- [ ] Defect RCA
- [ ] Test Evidence
- [ ] Sign-Off

---

# 21. Functional Production Support

- [ ] Trade Not Captured
- [ ] Trade Rejected
- [ ] Wrong Trade Data
- [ ] Missing Static Data
- [ ] Missing Market Data
- [ ] Incorrect Position
- [ ] Incorrect P&L
- [ ] Risk Mismatch
- [ ] Settlement Failure
- [ ] Accounting Mismatch
- [ ] Datamart Missing Data
- [ ] Report Mismatch
- [ ] EOD Failure
- [ ] SOD Failure
- [ ] Reconciliation Break
- [ ] Limit Breach
- [ ] Interface Failure
- [ ] Functional RCA
- [ ] Incident Severity
- [ ] SLA
- [ ] Escalation
- [ ] Business Communication
- [ ] Workaround
- [ ] Permanent Fix
- [ ] Preventive Action

---

# 22. End-to-End Functional Scenarios

## Scenario A — FX Trade
- [ ] Trader creates FX Spot
- [ ] Trade captured
- [ ] Trade validated
- [ ] Counterparty enriched
- [ ] SSI identified
- [ ] Position updated
- [ ] P&L calculated
- [ ] Risk calculated
- [ ] Confirmation generated
- [ ] Settlement prepared
- [ ] Payment processed
- [ ] Accounting generated
- [ ] Datamart updated
- [ ] Report generated

## Scenario B — Interest Rate Swap
- [ ] Trade creation
- [ ] Counterparty
- [ ] Book
- [ ] Notional
- [ ] Fixed/Float legs
- [ ] Rate
- [ ] Reset
- [ ] Cashflows
- [ ] Valuation
- [ ] P&L
- [ ] Risk
- [ ] Confirmation
- [ ] Settlement
- [ ] Accounting
- [ ] Reporting

## Scenario C — Bond Trade
- [ ] Buy/Sell
- [ ] Bond selection
- [ ] Face value
- [ ] Price
- [ ] Yield
- [ ] Coupon
- [ ] Accrued interest
- [ ] Settlement
- [ ] Position
- [ ] Valuation
- [ ] P&L
- [ ] Accounting
- [ ] Reporting

## Scenario D — Trade Amendment
- [ ] Existing trade
- [ ] Amendment request
- [ ] Validation
- [ ] Recalculation
- [ ] Position impact
- [ ] P&L impact
- [ ] Risk impact
- [ ] Confirmation
- [ ] Settlement impact
- [ ] Accounting impact
- [ ] Audit trail

## Scenario E — Trade Cancellation
- [ ] Cancellation request
- [ ] Validation
- [ ] Position reversal
- [ ] P&L reversal
- [ ] Risk reversal
- [ ] Settlement cancellation
- [ ] Accounting reversal
- [ ] Confirmation
- [ ] Audit trail

## Scenario F — Regulatory Reporting
- [ ] Source data
- [ ] Trade data
- [ ] Position data
- [ ] Risk data
- [ ] Datamart
- [ ] Regulatory rules
- [ ] Report generation
- [ ] Validation
- [ ] Reconciliation
- [ ] Exception handling
- [ ] Submission
- [ ] Audit trail

---

# 23. Interview Readiness

## Functional Questions
- [ ] Explain Murex
- [ ] Explain MX.3
- [ ] Explain FO/MO/BO
- [ ] Explain trade lifecycle
- [ ] Explain trade capture
- [ ] Explain static data
- [ ] Explain market data
- [ ] Explain position
- [ ] Explain P&L
- [ ] Explain risk
- [ ] Explain settlement
- [ ] Explain accounting
- [ ] Explain Datamart
- [ ] Explain regulatory reporting
- [ ] Explain EOD/SOD

## Product Questions
- [ ] Explain FX Spot
- [ ] Explain FX Forward
- [ ] Explain FX Swap
- [ ] Explain FX Option
- [ ] Explain Bond
- [ ] Explain IRS
- [ ] Explain Futures
- [ ] Explain Options
- [ ] Explain Swaption
- [ ] Explain CDS

## Scenario Questions
- [ ] Trade missing from position
- [ ] Trade missing from Datamart
- [ ] P&L mismatch
- [ ] Risk mismatch
- [ ] Settlement failed
- [ ] Accounting mismatch
- [ ] Market data missing
- [ ] Static data missing
- [ ] EOD failed
- [ ] Regulatory report mismatch
- [ ] Reconciliation break
- [ ] Trade amendment impact
- [ ] Trade cancellation impact

---

# 24. Functional Master Progress

| Module | Target | Completed | Status |
|---|---:|---:|---|
| Capital Markets | 40+ | 0 | [ ] |
| FO | 40+ | 0 | [ ] |
| MO | 40+ | 0 | [ ] |
| BO | 40+ | 0 | [ ] |
| Trade Lifecycle | 40+ | 0 | [ ] |
| Products | 60+ | 0 | [ ] |
| Static Data | 25+ | 0 | [ ] |
| Market Data | 20+ | 0 | [ ] |
| Risk | 25+ | 0 | [ ] |
| P&L / Valuation | 20+ | 0 | [ ] |
| Position | 15+ | 0 | [ ] |
| Settlement | 25+ | 0 | [ ] |
| Accounting | 20+ | 0 | [ ] |
| Collateral | 10+ | 0 | [ ] |
| Treasury | 10+ | 0 | [ ] |
| Regulatory | 20+ | 0 | [ ] |
| EOD/SOD | 25+ | 0 | [ ] |
| Workflow / Configuration | 20+ | 0 | [ ] |
| Functional Testing | 20+ | 0 | [ ] |
| Production Support | 25+ | 0 | [ ] |
| End-to-End Scenarios | 6+ | 0 | [ ] |
| Interview Readiness | 50+ | 0 | [ ] |

> The target counts are planning estimates, not an official Murex syllabus. The actual number of sub-concepts will grow as we break each module into lessons.

---

# 25. Definition of Done — Functional

For every major topic:

- [ ] I know **what** it is.
- [ ] I know **why** it is used.
- [ ] I understand **where it fits in FO/MO/BO**.
- [ ] I understand its place in the **trade lifecycle**.
- [ ] I can explain a banking example.
- [ ] I can explain the Murex functional perspective.
- [ ] I can trace its downstream/upstream impact.
- [ ] I can explain one production issue.
- [ ] I can answer interview questions.
- [ ] I have written notes in Git.
- [ ] I have completed a practical scenario where applicable.

---

# Recommended Learning Order

1. [ ] Capital Markets
2. [ ] FO / MO / BO
3. [ ] Trade Lifecycle
4. [ ] FX
5. [ ] Fixed Income
6. [ ] Interest Rates
7. [ ] Derivatives
8. [ ] Static Data
9. [ ] Market Data
10. [ ] Position Management
11. [ ] P&L / Valuation
12. [ ] Risk
13. [ ] Back Office
14. [ ] Settlement
15. [ ] Accounting
16. [ ] Collateral
17. [ ] Treasury
18. [ ] Regulatory Reporting
19. [ ] EOD / SOD
20. [ ] Workflow / Configuration
21. [ ] Functional Testing
22. [ ] Production Support
23. [ ] End-to-End Scenarios
24. [ ] Functional Interviews

> **Final target:** Do not become a memorization-only functional consultant. The goal is to understand how a trade moves through **FO → MO → BO → Risk/P&L → Settlement → Accounting → Datamart/Reporting**, and then connect that business flow to **MxML, SQL, Linux, Control-M and Technical Services**.
