# Murex Techno-Functional Topics List

## Purpose

Build end-to-end Murex techno-functional understanding:

> Financial Markets → Trade Lifecycle → Murex Functional Modules
> → Market Data → Risk → Accounting → Settlement
> → Technical Architecture → Datamart → Interfaces
> → Workflow/Events → Batch → Integration
> → Oracle → Unix/Linux → Production Support

Learning approach:

> Concept → Business Example → Murex Flow → Technical View
> → Configuration Concepts → Integration → Troubleshooting
> → Interview Questions → Glossary

---

# PART A — FINANCIAL MARKETS FOUNDATION

## 01 — Financial Markets Basics

- [ ] Financial markets overview
- [ ] Front Office
- [ ] Middle Office
- [ ] Back Office
- [ ] Trade lifecycle
- [ ] Trade capture
- [ ] Trade validation
- [ ] Trade enrichment
- [ ] Trade confirmation
- [ ] Settlement
- [ ] Accounting
- [ ] Risk management
- [ ] Position
- [ ] P&L
- [ ] Market data
- [ ] Static data
- [ ] Reference data
- [ ] Counterparty
- [ ] Portfolio
- [ ] Book

---

# 02 — Financial Instruments

- [ ] Cash products
- [ ] FX
- [ ] FX Spot
- [ ] FX Forward
- [ ] FX Swap
- [ ] FX Option
- [ ] Interest Rate products
- [ ] Deposits
- [ ] FRA
- [ ] Interest Rate Swap
- [ ] OIS
- [ ] Cross Currency Swap
- [ ] Bonds
- [ ] Money Market instruments
- [ ] Equities
- [ ] Equity derivatives
- [ ] Futures
- [ ] Options
- [ ] Commodity products
- [ ] Structured products
- [ ] Credit products
- [ ] Product taxonomy

---

# PART B — MUREX FUNDAMENTALS

# 03 — Murex Overview

- [ ] What is Murex
- [ ] MX.3 overview
- [ ] Murex platform concepts
- [ ] Murex modules
- [ ] Functional architecture
- [ ] Technical architecture
- [ ] Front Office
- [ ] Middle Office
- [ ] Back Office
- [ ] Risk
- [ ] Accounting
- [ ] Settlement
- [ ] Reporting
- [ ] Integration
- [ ] Data management

---

# 04 — Murex Environment Concepts

- [ ] Development environment
- [ ] Testing environment
- [ ] UAT
- [ ] Production
- [ ] Environment promotion
- [ ] Configuration migration
- [ ] Release management
- [ ] Version management
- [ ] Deployment concepts
- [ ] Environment troubleshooting

---

# PART C — TRADE LIFECYCLE

# 05 — End-to-End Trade Lifecycle

- [ ] Trade capture
- [ ] Trade validation
- [ ] Trade enrichment
- [ ] Static data lookup
- [ ] Market data lookup
- [ ] Trade confirmation
- [ ] Trade amendment
- [ ] Trade cancellation
- [ ] Trade settlement
- [ ] Accounting
- [ ] Position update
- [ ] Risk calculation
- [ ] P&L
- [ ] Reporting
- [ ] Reconciliation

---

# 06 — Trade Capture

- [ ] Trade entry
- [ ] Trade economics
- [ ] Trade attributes
- [ ] Counterparty
- [ ] Book
- [ ] Portfolio
- [ ] Trader
- [ ] Product
- [ ] Currency
- [ ] Trade date
- [ ] Value date
- [ ] Maturity date
- [ ] Notional
- [ ] Price
- [ ] Rate
- [ ] Quantity

---

# 07 — Trade Events

- [ ] Trade creation
- [ ] Amendment
- [ ] Cancellation
- [ ] Exercise
- [ ] Expiry
- [ ] Fixing
- [ ] Reset
- [ ] Settlement
- [ ] Maturity
- [ ] Lifecycle events
- [ ] Event processing
- [ ] Event dependencies

---

# 08 — Trade Validation and Enrichment

- [ ] Validation rules
- [ ] Mandatory fields
- [ ] Static data validation
- [ ] Counterparty validation
- [ ] Product validation
- [ ] Book validation
- [ ] Currency validation
- [ ] Market data validation
- [ ] Enrichment
- [ ] Defaulting
- [ ] Reference data lookup
- [ ] Validation failures

---

# PART D — MUREX FUNCTIONAL AREAS

# 09 — Front Office

- [ ] Trade capture
- [ ] Trade blotter
- [ ] Trade inquiry
- [ ] Position
- [ ] P&L
- [ ] Market data usage
- [ ] Trader workflow
- [ ] Deal management
- [ ] Amendments
- [ ] Cancellations

---

# 10 — Static Data

- [ ] Static data concepts
- [ ] Counterparties
- [ ] Legal entities
- [ ] Books
- [ ] Portfolios
- [ ] Traders
- [ ] Products
- [ ] Currencies
- [ ] Calendars
- [ ] Business centers
- [ ] Settlement instructions
- [ ] Static data dependencies
- [ ] Static data troubleshooting

---

# 11 — Market Data

- [ ] Market data concepts
- [ ] Yield curves
- [ ] Interest rates
- [ ] FX rates
- [ ] Volatility
- [ ] Equity prices
- [ ] Commodity prices
- [ ] Credit spreads
- [ ] Fixings
- [ ] Market data sources
- [ ] Market data loading
- [ ] Market data validation
- [ ] Market data hierarchy
- [ ] Market data troubleshooting

---

# 12 — Risk Management

- [ ] Risk concepts
- [ ] Market risk
- [ ] Credit risk
- [ ] Liquidity risk
- [ ] Counterparty risk
- [ ] Exposure
- [ ] Sensitivities
- [ ] Greeks
- [ ] VaR
- [ ] Stress testing
- [ ] Scenario analysis
- [ ] Limit management
- [ ] Risk aggregation
- [ ] Risk reporting
- [ ] Risk batch processing
- [ ] Risk troubleshooting

---

# 13 — P&L

- [ ] P&L concepts
- [ ] Realized P&L
- [ ] Unrealized P&L
- [ ] Mark-to-market
- [ ] Valuation
- [ ] P&L explain
- [ ] P&L attribution
- [ ] Price impact
- [ ] Rate impact
- [ ] FX impact
- [ ] Carry
- [ ] Accrual
- [ ] P&L reporting
- [ ] P&L reconciliation

---

# 14 — Back Office

- [ ] Confirmation
- [ ] Settlement
- [ ] Settlement instructions
- [ ] Payment
- [ ] Cash flow
- [ ] Netting
- [ ] Settlement status
- [ ] Failed settlement
- [ ] Reconciliation
- [ ] Back-office reporting

---

# 15 — Settlement

- [ ] Settlement lifecycle
- [ ] Cash flows
- [ ] Payment instructions
- [ ] Settlement instructions
- [ ] Counterparty SSI
- [ ] Settlement dates
- [ ] Payment dates
- [ ] Netting
- [ ] Settlement status
- [ ] Failed settlement
- [ ] Settlement reconciliation

---

# 16 — Accounting

- [ ] Accounting concepts
- [ ] Accounting events
- [ ] Accounting rules
- [ ] Accounting entries
- [ ] Debit
- [ ] Credit
- [ ] GL
- [ ] Accounting books
- [ ] Posting
- [ ] Accounting date
- [ ] Value date
- [ ] Accruals
- [ ] Revaluation
- [ ] P&L accounting
- [ ] Accounting reconciliation
- [ ] Accounting troubleshooting

---

# PART E — MUREX TECHNICAL FOUNDATION

# 17 — Murex Technical Architecture

- [ ] Murex architecture
- [ ] Application components
- [ ] Client/server concepts
- [ ] Application servers
- [ ] Database
- [ ] Oracle
- [ ] Batch servers
- [ ] Integration layer
- [ ] Messaging
- [ ] File-based integration
- [ ] Network connectivity
- [ ] Environment architecture

---

# 18 — Murex Data Model Concepts

- [ ] Murex data concepts
- [ ] Trade data
- [ ] Static data
- [ ] Market data
- [ ] Position data
- [ ] Risk data
- [ ] Accounting data
- [ ] Reference data
- [ ] Relationships
- [ ] Data dependencies
- [ ] Data lineage

---

# 19 — Oracle and Murex

- [ ] Oracle architecture basics
- [ ] Murex database concepts
- [ ] Tables
- [ ] Views
- [ ] Indexes
- [ ] Stored procedures concepts
- [ ] SQL querying
- [ ] Joins
- [ ] Aggregation
- [ ] Data validation
- [ ] Transaction concepts
- [ ] Performance concepts
- [ ] Database troubleshooting

---

# 20 — Datamart

- [ ] Datamart concepts
- [ ] Reporting data
- [ ] Data extraction
- [ ] Data transformation
- [ ] Data loading
- [ ] Datamart structure
- [ ] Reporting queries
- [ ] Data reconciliation
- [ ] Datamart batch
- [ ] Datamart troubleshooting

---

# 21 — Murex Batch

- [ ] Batch concepts
- [ ] Batch scheduling
- [ ] Batch chains
- [ ] Dependencies
- [ ] Batch parameters
- [ ] Batch execution
- [ ] Batch monitoring
- [ ] Batch logs
- [ ] Failed batch
- [ ] Restart
- [ ] Recovery
- [ ] Rerun
- [ ] Batch reconciliation

---

# 22 — Workflow

- [ ] Workflow concepts
- [ ] Workflow states
- [ ] Workflow transitions
- [ ] Workflow events
- [ ] Workflow rules
- [ ] Approval workflow
- [ ] Exception workflow
- [ ] Trade workflow
- [ ] Workflow troubleshooting

---

# 23 — Murex Events

- [ ] Event concepts
- [ ] Trade events
- [ ] Lifecycle events
- [ ] Settlement events
- [ ] Accounting events
- [ ] Risk events
- [ ] Event processing
- [ ] Event dependencies
- [ ] Event failure
- [ ] Event troubleshooting

---

# PART F — MUREX INTEGRATION

# 24 — Integration Fundamentals

- [ ] Integration concepts
- [ ] Inbound interface
- [ ] Outbound interface
- [ ] Synchronous integration
- [ ] Asynchronous integration
- [ ] File-based integration
- [ ] API integration
- [ ] Messaging
- [ ] Batch integration
- [ ] Real-time integration

---

# 25 — XML Integration

- [ ] XML fundamentals
- [ ] XML structure
- [ ] XML schema
- [ ] XML validation
- [ ] XML messages
- [ ] XML transformation
- [ ] XML inbound interface
- [ ] XML outbound interface
- [ ] XML error handling
- [ ] XML troubleshooting

---

# 26 — MXML

- [ ] MXML concepts
- [ ] MXML structure
- [ ] MXML messages
- [ ] MXML integration
- [ ] MXML request
- [ ] MXML response
- [ ] MXML validation
- [ ] MXML processing
- [ ] MXML errors
- [ ] MXML troubleshooting
- [ ] MXML interface design

---

# 27 — File-Based Integration

- [ ] Input files
- [ ] Output files
- [ ] File naming
- [ ] File format
- [ ] File validation
- [ ] File availability
- [ ] File transfer
- [ ] SFTP
- [ ] File processing
- [ ] Archive
- [ ] Error directory
- [ ] Duplicate handling
- [ ] Reprocessing
- [ ] Reconciliation

---

# 28 — API Integration

- [ ] API concepts
- [ ] REST
- [ ] HTTP
- [ ] JSON
- [ ] Authentication
- [ ] Request
- [ ] Response
- [ ] Error handling
- [ ] Timeout
- [ ] Retry
- [ ] Integration monitoring

---

# 29 — Messaging

- [ ] Messaging concepts
- [ ] Producer
- [ ] Consumer
- [ ] Queue
- [ ] Message
- [ ] Asynchronous processing
- [ ] Message failure
- [ ] Retry
- [ ] Duplicate messages
- [ ] Message monitoring

---

# PART G — UNIX / SHELL / PYTHON WITH MUREX

# 30 — Unix and Murex

- [ ] Linux server concepts
- [ ] Murex application processes
- [ ] Process monitoring
- [ ] Log analysis
- [ ] File management
- [ ] Permissions
- [ ] Environment variables
- [ ] Shell commands
- [ ] Batch monitoring
- [ ] Production troubleshooting

---

# 31 — Shell Scripting and Murex

- [ ] Controller scripts
- [ ] Batch scripts
- [ ] Job execution
- [ ] Exit codes
- [ ] Error handling
- [ ] Logging
- [ ] File validation
- [ ] Process validation
- [ ] Database validation
- [ ] Retry
- [ ] Recovery
- [ ] Restart automation

---

# 32 — Python and Murex

- [ ] Python integration concepts
- [ ] File processing
- [ ] XML processing
- [ ] JSON processing
- [ ] Oracle connectivity
- [ ] API integration
- [ ] Log analysis
- [ ] Reconciliation
- [ ] Validation utilities
- [ ] Automation utilities
- [ ] Production support utilities

---

# PART H — PRODUCTION SUPPORT

# 33 — Murex Production Support

- [ ] Incident management
- [ ] Severity
- [ ] Priority
- [ ] Incident triage
- [ ] Log analysis
- [ ] Batch monitoring
- [ ] Interface monitoring
- [ ] Trade investigation
- [ ] Database investigation
- [ ] Network investigation
- [ ] Application investigation
- [ ] Root cause analysis
- [ ] Workaround
- [ ] Permanent fix
- [ ] Recovery
- [ ] Reconciliation
- [ ] Incident documentation

---

# 34 — Batch Failure Troubleshooting

- [ ] Identify failed batch
- [ ] Check batch status
- [ ] Check logs
- [ ] Check parameters
- [ ] Check dependencies
- [ ] Check database
- [ ] Check filesystem
- [ ] Check network
- [ ] Check input files
- [ ] Identify failure point
- [ ] Correct issue
- [ ] Restart
- [ ] Validate output
- [ ] Reconcile results

---

# 35 — Interface Failure Troubleshooting

- [ ] Interface not triggered
- [ ] File not received
- [ ] File incomplete
- [ ] Invalid message
- [ ] XML validation failure
- [ ] MXML failure
- [ ] Network failure
- [ ] SFTP failure
- [ ] Database failure
- [ ] Processing failure
- [ ] Output not generated
- [ ] Duplicate message
- [ ] Reprocessing
- [ ] Reconciliation

---

# 36 — Trade Troubleshooting

- [ ] Trade not captured
- [ ] Trade validation failure
- [ ] Incorrect static data
- [ ] Incorrect market data
- [ ] Incorrect counterparty
- [ ] Incorrect book
- [ ] Incorrect valuation
- [ ] Incorrect P&L
- [ ] Settlement failure
- [ ] Accounting issue
- [ ] Risk issue
- [ ] Interface issue
- [ ] Trade reconciliation

---

# PART I — CONFIGURATION CONCEPTS

# 37 — Murex Configuration Concepts

- [ ] Static data configuration
- [ ] Product configuration
- [ ] Book configuration
- [ ] Portfolio configuration
- [ ] Counterparty configuration
- [ ] Market data configuration
- [ ] Workflow configuration
- [ ] Event configuration
- [ ] Accounting configuration
- [ ] Settlement configuration
- [ ] Interface configuration
- [ ] Batch configuration
- [ ] Reporting configuration

---

# 38 — Environment and Release Management

- [ ] Configuration migration
- [ ] Development
- [ ] SIT
- [ ] UAT
- [ ] Production
- [ ] Release management
- [ ] Deployment
- [ ] Rollback
- [ ] Version control
- [ ] Change management
- [ ] Production validation

---

# PART J — REPORTING AND RECONCILIATION

# 39 — Reporting

- [ ] Operational reports
- [ ] Trade reports
- [ ] Position reports
- [ ] P&L reports
- [ ] Risk reports
- [ ] Accounting reports
- [ ] Settlement reports
- [ ] Regulatory reporting concepts
- [ ] Report validation
- [ ] Report reconciliation

---

# 40 — Reconciliation

- [ ] Trade reconciliation
- [ ] Position reconciliation
- [ ] Cash reconciliation
- [ ] Settlement reconciliation
- [ ] Accounting reconciliation
- [ ] Interface reconciliation
- [ ] Source vs target
- [ ] Missing records
- [ ] Duplicate records
- [ ] Amount mismatch
- [ ] Date mismatch
- [ ] Root-cause analysis

---

# PART K — TECHNO-FUNCTIONAL SCENARIOS

# 41 — End-to-End Scenario 1

Trade Capture
→ Validation
→ Enrichment
→ Market Data
→ Valuation
→ Risk
→ P&L
→ Confirmation
→ Settlement
→ Accounting
→ Reporting

- [ ] Understand business flow
- [ ] Identify Murex components
- [ ] Identify technical dependencies
- [ ] Identify database dependencies
- [ ] Identify interfaces
- [ ] Identify batch processing
- [ ] Identify troubleshooting points

---

# 42 — End-to-End Scenario 2

External System
→ SFTP
→ Linux
→ Shell Controller
→ Python
→ MXML
→ Murex
→ Oracle
→ Processing
→ Output
→ Archive
→ Reconciliation

- [ ] Requirement
- [ ] Interface design
- [ ] File validation
- [ ] MXML construction
- [ ] Processing
- [ ] Error handling
- [ ] Logging
- [ ] Recovery
- [ ] Reconciliation

---

# 43 — Interview Preparation

## Functional Questions

- [ ] Trade lifecycle
- [ ] FX
- [ ] Interest rates
- [ ] Derivatives
- [ ] Market data
- [ ] Static data
- [ ] Risk
- [ ] P&L
- [ ] Settlement
- [ ] Accounting
- [ ] Reconciliation

## Technical Questions

- [ ] Murex architecture
- [ ] Oracle
- [ ] Datamart
- [ ] Batch
- [ ] Workflow
- [ ] Events
- [ ] Interfaces
- [ ] XML
- [ ] MXML
- [ ] Linux
- [ ] Shell scripting
- [ ] Python
- [ ] SFTP
- [ ] Networking

## Scenario Questions

- [ ] Trade failed
- [ ] Trade not visible
- [ ] Incorrect P&L
- [ ] Incorrect risk
- [ ] Market data missing
- [ ] Batch failed
- [ ] Interface failed
- [ ] MXML rejected
- [ ] File missing
- [ ] SFTP failed
- [ ] Database unavailable
- [ ] Settlement failed
- [ ] Accounting mismatch
- [ ] Reconciliation mismatch
- [ ] Production incident

---

# 44 — Practical Labs

## Lab 01 — Trade Lifecycle

Trade
→ Validation
→ Enrichment
→ Risk
→ P&L
→ Settlement
→ Accounting

- [ ] Document the flow
- [ ] Identify each component
- [ ] Identify dependencies
- [ ] Create troubleshooting scenarios

---

## Lab 02 — MXML Integration

External Input
→ XML/MXML
→ Validation
→ Murex Interface
→ Processing
→ Response
→ Logging

- [ ] Design message
- [ ] Validate message
- [ ] Process success case
- [ ] Process failure case
- [ ] Reprocess

---

## Lab 03 — Linux + Python + Oracle

Shell Controller
→ Python
→ Oracle
→ Validation
→ Output

- [ ] Shell script
- [ ] Python program
- [ ] Oracle tables
- [ ] SQL
- [ ] Logging
- [ ] Error handling
- [ ] Exit codes

---

## Lab 04 — Complete Integration Lab

External System
        ↓
     SFTP
        ↓
     Linux
        ↓
 Shell Controller
        ↓
     Python
        ↓
     MXML
        ↓
      Murex
        ↓
     Oracle
        ↓
 Risk / P&L
        ↓
 Settlement
        ↓
 Accounting
        ↓
 Reporting
        ↓
 Reconciliation

- [ ] Requirement
- [ ] Architecture
- [ ] Database design
- [ ] Interface design
- [ ] Python implementation
- [ ] Shell implementation
- [ ] MXML
- [ ] Logging
- [ ] Error handling
- [ ] Recovery
- [ ] Reconciliation
- [ ] Production support scenarios

---

# Completion Criteria

A topic is COMPLETE only when:

- [ ] Concept understood
- [ ] Business meaning understood
- [ ] Murex relevance understood
- [ ] Technical dependency understood
- [ ] Example discussed
- [ ] Troubleshooting scenario understood
- [ ] Notes prepared
- [ ] Glossary updated
- [ ] Interview questions answered
- [ ] Practical scenario completed

---

# Final Goal

Be able to explain:

> What happens to a trade from capture to settlement?

and then go one level deeper:

> Which Murex functional component is involved?

and then deeper:

> What technical component supports it?

and finally:

> If it fails in production, how would I investigate it using
> Murex + Oracle + Linux + Shell + Python + Networking + Interfaces?
