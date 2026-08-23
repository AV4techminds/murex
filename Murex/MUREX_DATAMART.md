# Murex Datamart — Topics Checklist

## 01 — Datamart Fundamentals

- [ ] What is a Datamart
- [ ] Purpose of Datamart
- [ ] Operational data vs reporting data
- [ ] Source data
- [ ] Target data
- [ ] Data extraction
- [ ] Data transformation
- [ ] Data loading
- [ ] Reporting layer
- [ ] Data consumption
- [ ] Data lineage

---

## 02 — Murex Datamart Architecture

- [ ] Murex source systems
- [ ] Transactional data
- [ ] Risk data
- [ ] Market data
- [ ] Reference data
- [ ] Datamart processing
- [ ] Datamart storage
- [ ] Reporting
- [ ] Batch processing
- [ ] Data flow
- [ ] Dependencies
- [ ] Monitoring

---

## 03 — Datamart Data Concepts

- [ ] Trade data
- [ ] Position data
- [ ] P&L data
- [ ] Risk data
- [ ] Market data
- [ ] Static data
- [ ] Counterparty data
- [ ] Product data
- [ ] Settlement data
- [ ] Accounting data
- [ ] Reference data

---

## 04 — Datamart Data Model

- [ ] Tables
- [ ] Columns
- [ ] Keys
- [ ] Primary keys
- [ ] Foreign keys
- [ ] Relationships
- [ ] Reference data
- [ ] Transaction data
- [ ] Dimensions
- [ ] Measures
- [ ] Facts
- [ ] Data relationships
- [ ] Data dependencies

---

## 05 — Trade Data in Datamart

- [ ] Trade identification
- [ ] Trade attributes
- [ ] Product
- [ ] Counterparty
- [ ] Book
- [ ] Portfolio
- [ ] Trader
- [ ] Currency
- [ ] Notional
- [ ] Price
- [ ] Trade date
- [ ] Value date
- [ ] Maturity date
- [ ] Trade status
- [ ] Lifecycle events

---

## 06 — Position Data

- [ ] Position concept
- [ ] Position by book
- [ ] Position by portfolio
- [ ] Position by product
- [ ] Position by currency
- [ ] Position aggregation
- [ ] Position snapshots
- [ ] Position reconciliation

---

## 07 — P&L Data

- [ ] P&L concepts
- [ ] Realized P&L
- [ ] Unrealized P&L
- [ ] Mark-to-market
- [ ] Valuation
- [ ] P&L components
- [ ] P&L attribution
- [ ] P&L aggregation
- [ ] P&L reporting
- [ ] P&L reconciliation

---

## 08 — Risk Data

- [ ] Risk data concepts
- [ ] Market risk
- [ ] Credit risk
- [ ] Exposure
- [ ] Sensitivities
- [ ] Greeks
- [ ] VaR concepts
- [ ] Stress testing
- [ ] Scenario analysis
- [ ] Risk aggregation
- [ ] Risk reporting
- [ ] Risk reconciliation

---

## 09 — Market Data in Datamart

- [ ] FX rates
- [ ] Interest rates
- [ ] Yield curves
- [ ] Volatility
- [ ] Credit spreads
- [ ] Prices
- [ ] Fixings
- [ ] Market data timestamps
- [ ] Market data validation
- [ ] Market data reconciliation

---

## 10 — Static Data in Datamart

- [ ] Counterparties
- [ ] Legal entities
- [ ] Books
- [ ] Portfolios
- [ ] Products
- [ ] Currencies
- [ ] Calendars
- [ ] Business centers
- [ ] Settlement instructions
- [ ] Reference data

---

## 11 — Datamart ETL Concepts

- [ ] Extract
- [ ] Transform
- [ ] Load
- [ ] Source extraction
- [ ] Transformation
- [ ] Data cleansing
- [ ] Validation
- [ ] Loading
- [ ] Incremental loading
- [ ] Full loading
- [ ] Error handling
- [ ] Reprocessing

---

## 12 — Datamart Batch Processing

- [ ] Datamart batch
- [ ] Batch scheduling
- [ ] Batch dependencies
- [ ] Batch parameters
- [ ] Batch execution
- [ ] Batch monitoring
- [ ] Batch logs
- [ ] Failed batch
- [ ] Restart
- [ ] Rerun
- [ ] Recovery
- [ ] Batch reconciliation

---

## 13 — Oracle and Datamart

- [ ] Oracle basics
- [ ] Datamart database
- [ ] Tables
- [ ] Views
- [ ] Indexes
- [ ] SQL queries
- [ ] Joins
- [ ] Aggregations
- [ ] Grouping
- [ ] Filtering
- [ ] Subqueries
- [ ] Data validation
- [ ] Query performance
- [ ] Database troubleshooting

---

## 14 — Datamart SQL Practice

- [ ] SELECT
- [ ] WHERE
- [ ] ORDER BY
- [ ] GROUP BY
- [ ] HAVING
- [ ] JOIN
- [ ] INNER JOIN
- [ ] LEFT JOIN
- [ ] UNION
- [ ] CASE
- [ ] Aggregate functions
- [ ] Date functions
- [ ] String functions
- [ ] Subqueries
- [ ] CTE concepts
- [ ] Analytical functions

---

## 15 — Reporting

- [ ] Trade reports
- [ ] Position reports
- [ ] P&L reports
- [ ] Risk reports
- [ ] Market data reports
- [ ] Accounting reports
- [ ] Settlement reports
- [ ] Regulatory reporting concepts
- [ ] Report validation
- [ ] Report reconciliation

---

## 16 — Datamart Reconciliation

- [ ] Source vs Datamart
- [ ] Record count reconciliation
- [ ] Amount reconciliation
- [ ] Position reconciliation
- [ ] P&L reconciliation
- [ ] Risk reconciliation
- [ ] Missing records
- [ ] Duplicate records
- [ ] Data mismatch
- [ ] Date mismatch
- [ ] Currency mismatch
- [ ] Root-cause analysis

---

## 17 — Datamart Data Quality

- [ ] Completeness
- [ ] Accuracy
- [ ] Consistency
- [ ] Uniqueness
- [ ] Validity
- [ ] Timeliness
- [ ] Duplicate detection
- [ ] Missing data
- [ ] Invalid data
- [ ] Data quality checks

---

## 18 — Datamart Performance

- [ ] Query performance
- [ ] Indexing concepts
- [ ] Large data volumes
- [ ] Batch performance
- [ ] Long-running queries
- [ ] Resource utilization
- [ ] SQL optimization concepts
- [ ] Monitoring
- [ ] Performance troubleshooting

---

## 19 — Linux + Datamart

- [ ] Datamart server
- [ ] Batch execution
- [ ] Shell scripts
- [ ] Log monitoring
- [ ] File management
- [ ] Disk monitoring
- [ ] Process monitoring
- [ ] Cron concepts
- [ ] Error handling
- [ ] Recovery

---

## 20 — Python + Datamart

- [ ] Oracle connectivity
- [ ] Data extraction
- [ ] Data validation
- [ ] Data comparison
- [ ] Reconciliation scripts
- [ ] Report generation
- [ ] CSV processing
- [ ] XML processing
- [ ] JSON processing
- [ ] Logging
- [ ] Error handling

---

## 21 — Datamart Troubleshooting

- [ ] Datamart batch failed
- [ ] Data missing
- [ ] Data delayed
- [ ] Incorrect trade count
- [ ] Incorrect position
- [ ] Incorrect P&L
- [ ] Incorrect risk
- [ ] Source/target mismatch
- [ ] Database issue
- [ ] SQL issue
- [ ] Performance issue
- [ ] Dependency failure
- [ ] Recovery
- [ ] Reconciliation

---

## 22 — End-to-End Datamart Flow

Murex Transaction Data
        ↓
Extraction
        ↓
Transformation
        ↓
Validation
        ↓
Datamart Load
        ↓
Oracle
        ↓
Reporting
        ↓
Reconciliation

- [ ] Understand complete flow
- [ ] Identify each component
- [ ] Identify dependencies
- [ ] Identify batch
- [ ] Identify database
- [ ] Identify failure points
- [ ] Identify recovery process

---

## 23 — Datamart Interview Preparation

- [ ] What is Datamart?
- [ ] Why Datamart?
- [ ] Datamart architecture
- [ ] Datamart data flow
- [ ] Trade data
- [ ] Position data
- [ ] P&L data
- [ ] Risk data
- [ ] Market data
- [ ] Static data
- [ ] ETL
- [ ] Batch
- [ ] Oracle
- [ ] SQL
- [ ] Reconciliation
- [ ] Performance
- [ ] Production support

---

## 24 — Practical Labs

### Lab 01 — Trade Datamart

Trade
→ Extraction
→ Transformation
→ Datamart
→ Oracle
→ Report
→ Reconciliation

- [ ] Design data flow
- [ ] Create sample tables
- [ ] Load sample trades
- [ ] Query data
- [ ] Reconcile results

### Lab 02 — P&L Datamart

Trade
→ Valuation
→ P&L
→ Datamart
→ Report
→ Reconciliation

- [ ] Create sample data
- [ ] Load data
- [ ] Query P&L
- [ ] Validate totals

### Lab 03 — Risk Datamart

Trade
→ Risk Calculation
→ Risk Data
→ Datamart
→ Report

- [ ] Create sample risk data
- [ ] Load data
- [ ] Aggregate risk
- [ ] Validate results

### Lab 04 — Production Troubleshooting

- [ ] Simulate failed batch
- [ ] Investigate logs
- [ ] Identify missing data
- [ ] Query Oracle
- [ ] Find root cause
- [ ] Correct issue
- [ ] Rerun
- [ ] Reconcile

---

# Completion Criteria

- [ ] Concept understood
- [ ] Business purpose understood
- [ ] Data flow understood
- [ ] Technical flow understood
- [ ] SQL practiced
- [ ] Troubleshooting practiced
- [ ] Reconciliation practiced
- [ ] Notes prepared
- [ ] Glossary updated
- [ ] Interview questions answered
- [ ] Git commit completed
