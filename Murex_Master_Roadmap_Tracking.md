# Murex Master Roadmap — Concepts & Tracking

> Goal: Build job-ready capability in Murex Datamart, MxML/Integration, and Technical Services/DevOps, supported by Capital Markets, Functional, Production Support, SQL/Linux/Control-M/Python/AWS.
>
> Learning method: Concept → Why → Architecture → Example → Banking Scenario → Murex Scenario → Hands-on Lab → Production Issue → Interview Questions.
>
> Tracking: Change `[ ]` to `[x]` only after the topic is understood and practiced.

---

## 0. Foundation — Capital Markets

### F0.1 Capital Markets Fundamentals
- [ ] Investment Banking
- [ ] Capital Markets
- [ ] Buy Side vs Sell Side
- [ ] Trading Desk
- [ ] Front Office (FO)
- [ ] Middle Office (MO)
- [ ] Back Office (BO)
- [ ] Operations
- [ ] Finance
- [ ] Risk
- [ ] Treasury
- [ ] Trade
- [ ] Position
- [ ] Portfolio
- [ ] Book
- [ ] Counterparty
- [ ] Market Data
- [ ] Reference / Static Data
- [ ] Settlement
- [ ] Clearing
- [ ] Collateral
- [ ] Accounting
- [ ] Regulatory Reporting

### F0.2 Financial Products
- [ ] Cash Products
- [ ] FX
- [ ] FX Spot
- [ ] FX Forward
- [ ] FX Swap
- [ ] FX Options
- [ ] Interest Rate Products
- [ ] Deposits
- [ ] Loans
- [ ] Bonds
- [ ] Money Market Products
- [ ] Interest Rate Swaps (IRS)
- [ ] Futures
- [ ] Options
- [ ] Swaptions
- [ ] Credit Products
- [ ] Equity Products
- [ ] Commodity Products
- [ ] Derivatives
- [ ] OTC vs Exchange-Traded Products

---

# 1. Murex Functional Foundation

### F1.1 Murex / MX.3 Fundamentals
- [ ] What is Murex?
- [ ] What is MX.3?
- [ ] Murex scope in Capital Markets
- [ ] Front-to-Back Architecture
- [ ] Trade Lifecycle
- [ ] Trade Capture
- [ ] Trade Validation
- [ ] Trade Enrichment
- [ ] Trade Confirmation
- [ ] Position Management
- [ ] Risk Management
- [ ] P&L
- [ ] Settlement
- [ ] Accounting
- [ ] Reporting
- [ ] Regulatory Reporting
- [ ] Datamart

### F1.2 Murex Functional Areas
- [ ] Front Office
- [ ] Static Data
- [ ] Market Data
- [ ] Trade Management
- [ ] Position Management
- [ ] Risk
- [ ] Simulation
- [ ] P&L
- [ ] Back Office
- [ ] Settlement
- [ ] Accounting
- [ ] Collateral
- [ ] Treasury
- [ ] Regulatory Reporting
- [ ] Datamart

---

# 2. Murex Datamart & Reporting — Deep Specialization

## DM-1 Datamart Fundamentals
- [ ] What is Murex Datamart?
- [ ] Why Datamart is required
- [ ] Operational Database vs Datamart
- [ ] Datamart Architecture
- [ ] Source → Datamart → Report Flow
- [ ] Real-Time vs Batch
- [ ] Data Lineage
- [ ] Datamart Data Flow

## DM-2 Datamart Data Model
- [ ] Entities
- [ ] Attributes
- [ ] Measures
- [ ] Dimensions
- [ ] Fact Tables
- [ ] Reference Data
- [ ] Trade Data
- [ ] Position Data
- [ ] Market Data
- [ ] Risk Data
- [ ] P&L Data
- [ ] Accounting Data
- [ ] Counterparty Data
- [ ] Product Data
- [ ] Currency Data
- [ ] Date / Time Data

## DM-3 Datamart Objects & Configuration
- [ ] Datamart Objects
- [ ] Datamart Structures
- [ ] Extraction
- [ ] Selection
- [ ] Filtering
- [ ] Measures
- [ ] Aggregation
- [ ] Grouping
- [ ] Hierarchies
- [ ] Calculated Fields
- [ ] Rules
- [ ] Mapping
- [ ] Transformation
- [ ] Output Configuration

## DM-4 Feeders & Loading
- [ ] Feeder Concepts
- [ ] Source Systems
- [ ] Data Ingestion
- [ ] Trade Feeders
- [ ] Market Data Feeders
- [ ] Static Data Feeders
- [ ] Risk Feeders
- [ ] Accounting Feeders
- [ ] Batch Loading
- [ ] Incremental Loading
- [ ] Full Loading
- [ ] Refresh
- [ ] Dependencies
- [ ] Failed Feeder Handling

## DM-5 Reporting
- [ ] Trade Reports
- [ ] Position Reports
- [ ] P&L Reports
- [ ] Risk Reports
- [ ] Market Valuation Reports
- [ ] Accounting Reports
- [ ] Regulatory Reports
- [ ] Operational Reports
- [ ] Management Reports
- [ ] Historical Reports
- [ ] Aggregated Reports
- [ ] Drilldown
- [ ] Filters
- [ ] Scheduling
- [ ] Report Distribution

## DM-6 Datamart + SQL
- [ ] SQL Joins
- [ ] Aggregations
- [ ] Analytical Functions
- [ ] Subqueries
- [ ] CTEs
- [ ] Query Optimization
- [ ] Execution Plans
- [ ] Indexing
- [ ] Partitioning
- [ ] Large-Volume Queries
- [ ] Reconciliation SQL
- [ ] Duplicate Detection
- [ ] Missing Data Detection

## DM-7 Reconciliation
- [ ] Source vs Datamart Reconciliation
- [ ] Datamart vs Report Reconciliation
- [ ] Trade Count Reconciliation
- [ ] Amount Reconciliation
- [ ] Position Reconciliation
- [ ] P&L Reconciliation
- [ ] Risk Reconciliation
- [ ] Currency Reconciliation
- [ ] Break Identification
- [ ] Break Classification
- [ ] Root Cause Analysis
- [ ] Tolerance
- [ ] Exception Reporting

## DM-8 Datamart Performance
- [ ] Large Dataset Handling
- [ ] Slow Extraction Analysis
- [ ] Slow Report Analysis
- [ ] DB Bottlenecks
- [ ] CPU Bottlenecks
- [ ] Memory Bottlenecks
- [ ] I/O Bottlenecks
- [ ] Batch Duration
- [ ] Parallel Processing
- [ ] Monitoring
- [ ] Optimization

## DM-9 Datamart Production Support
- [ ] Missing Report
- [ ] Missing Trade
- [ ] Duplicate Trade
- [ ] Wrong Amount
- [ ] Wrong Currency
- [ ] Wrong Valuation
- [ ] Incomplete Report
- [ ] Feeder Failure
- [ ] Extraction Failure
- [ ] Batch Failure
- [ ] Database Issue
- [ ] Reconciliation Failure
- [ ] EOD Issue
- [ ] Report Performance Issue
- [ ] RCA
- [ ] Incident Communication
- [ ] Preventive Action

## DM-10 Advanced Datamart
- [ ] Historical Data
- [ ] Data Retention
- [ ] Archival
- [ ] Data Migration
- [ ] Data Masking
- [ ] Non-Production Data
- [ ] Data Sampling
- [ ] Environment Refresh
- [ ] Regulatory Data Lineage
- [ ] Auditability
- [ ] Data Quality
- [ ] Data Governance
- [ ] Automation

---

# 3. Murex MxML + Integration — Deep Specialization

## MXML-1 XML Fundamentals
- [ ] XML Declaration
- [ ] Elements
- [ ] Attributes
- [ ] Hierarchy
- [ ] Root Element
- [ ] Namespaces
- [ ] XPath
- [ ] XSD
- [ ] XML Validation
- [ ] XML Parsing
- [ ] Transformation
- [ ] XSLT Concepts
- [ ] XML Errors

## MXML-2 MxML Foundation
- [ ] What is MxML?
- [ ] Why MxML is Used
- [ ] MxML Architecture
- [ ] MxML Messages
- [ ] MxML Exchange
- [ ] Message Lifecycle
- [ ] Inbound Messages
- [ ] Outbound Messages
- [ ] Validation
- [ ] Processing
- [ ] Acknowledgement
- [ ] Errors
- [ ] Logs
- [ ] Monitoring

## MXML-3 Trade Integration
- [ ] Trade Capture Integration
- [ ] Booking
- [ ] Enrichment
- [ ] Confirmation
- [ ] Amendment
- [ ] Cancellation
- [ ] Lifecycle Messages
- [ ] Message Status
- [ ] STP
- [ ] Pre-Trade Integration
- [ ] Post-Trade Integration

## MXML-4 Static / Reference Data Integration
- [ ] Counterparty
- [ ] Product
- [ ] Instrument
- [ ] Account
- [ ] Settlement Data
- [ ] Currency
- [ ] Legal Entity
- [ ] Synchronization
- [ ] Static Data Interfaces

## MXML-5 Market Data Integration
- [ ] Market Data Sources
- [ ] Prices
- [ ] FX Rates
- [ ] Interest Rates
- [ ] Curves
- [ ] Volatility
- [ ] Market Data Ingestion
- [ ] Market Data Validation
- [ ] Missing Market Data
- [ ] Stale Market Data
- [ ] Interface Failure

## MXML-6 Integration Architecture
- [ ] Upstream Systems
- [ ] Murex
- [ ] Downstream Systems
- [ ] Inbound Interfaces
- [ ] Outbound Interfaces
- [ ] Synchronous Integration
- [ ] Asynchronous Integration
- [ ] Batch Integration
- [ ] Real-Time Integration
- [ ] File-Based Integration
- [ ] Message-Based Integration
- [ ] API-Based Integration
- [ ] Event-Driven Concepts

## MXML-7 Integration Troubleshooting
- [ ] Invalid XML
- [ ] Schema Failure
- [ ] Missing Field
- [ ] Invalid Value
- [ ] Mapping Issue
- [ ] Transformation Issue
- [ ] Interface Unavailable
- [ ] Timeout
- [ ] Authentication Failure
- [ ] Authorization Failure
- [ ] Duplicate Message
- [ ] Stuck Message
- [ ] Rejected Message
- [ ] Retry
- [ ] Reprocessing
- [ ] Dead-Letter / Error Concepts
- [ ] Log Analysis
- [ ] RCA

## MXML-8 APIs
- [ ] REST
- [ ] HTTP
- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] DELETE
- [ ] JSON
- [ ] HTTP Headers
- [ ] HTTP Status Codes
- [ ] Authentication
- [ ] OAuth2
- [ ] TLS
- [ ] Authorization
- [ ] API Errors
- [ ] Postman
- [ ] OpenAPI
- [ ] Python API Client

## MXML-9 Integration Security
- [ ] TLS
- [ ] Certificates
- [ ] Keys
- [ ] Authentication
- [ ] Authorization
- [ ] OAuth2
- [ ] Service Accounts
- [ ] Secrets
- [ ] Credentials
- [ ] Network Access
- [ ] Firewall
- [ ] Proxy

## MXML-10 Integration Production Support
- [ ] Integration Monitoring
- [ ] Failed Messages
- [ ] Retry / Reprocessing
- [ ] Duplicate Detection
- [ ] Reconciliation
- [ ] SLA
- [ ] Tracing
- [ ] Upstream Coordination
- [ ] Downstream Coordination
- [ ] Incident Handling
- [ ] RCA
- [ ] Preventive Automation

---

# 4. Murex Technical Services + DevOps

## TS-1 MX.3 Architecture
- [ ] MX.3 Architecture Overview
- [ ] Presentation Layer
- [ ] Business Layer
- [ ] Orchestration Layer
- [ ] Technical Layer
- [ ] Storage Layer
- [ ] Infrastructure Layer
- [ ] Application Services
- [ ] Business Services
- [ ] Orchestration Services
- [ ] Technical Services
- [ ] Database
- [ ] Datamart Database
- [ ] Cloud Concepts
- [ ] Grid Concepts
- [ ] Containers
- [ ] Kubernetes

## TS-2 Environments
- [ ] Development
- [ ] SIT
- [ ] UAT
- [ ] Pre-Production
- [ ] Production
- [ ] Environment Isolation
- [ ] Configuration Management
- [ ] Environment Variables
- [ ] Dependencies
- [ ] Environment Refresh
- [ ] Data Masking
- [ ] Provisioning
- [ ] Cloning
- [ ] Decommissioning

## TS-3 Installation & Deployment
- [ ] Prerequisites
- [ ] Server Requirements
- [ ] Database Requirements
- [ ] Application Deployment
- [ ] Configuration
- [ ] Validation
- [ ] Smoke Testing
- [ ] Rollback
- [ ] Release Management
- [ ] Version Management
- [ ] Patch Management
- [ ] Upgrades
- [ ] Migration
- [ ] Conversion
- [ ] Post-Upgrade Validation

## TS-4 Linux / Unix
- [ ] Filesystem
- [ ] File Permissions
- [ ] Users
- [ ] Groups
- [ ] Processes
- [ ] Services
- [ ] CPU
- [ ] Memory
- [ ] Disk
- [ ] Files
- [ ] Logs
- [ ] Environment Variables
- [ ] SSH
- [ ] SCP
- [ ] `ls`
- [ ] `cd`
- [ ] `cp`
- [ ] `mv`
- [ ] `rm`
- [ ] `find`
- [ ] `grep`
- [ ] `awk`
- [ ] `sed`
- [ ] `cut`
- [ ] `sort`
- [ ] `uniq`
- [ ] `head`
- [ ] `tail`
- [ ] `less`
- [ ] `xargs`
- [ ] `ps`
- [ ] `top`
- [ ] `df`
- [ ] `du`
- [ ] `free`
- [ ] `ss`
- [ ] `curl`
- [ ] `ping`
- [ ] `traceroute`
- [ ] `nslookup`
- [ ] `dig`
- [ ] `nc`

## TS-5 Shell / Bash
- [ ] Variables
- [ ] Arguments
- [ ] Conditions
- [ ] Loops
- [ ] Functions
- [ ] Arrays
- [ ] Exit Codes
- [ ] Return Codes
- [ ] Pipes
- [ ] Redirection
- [ ] Command Substitution
- [ ] File Validation
- [ ] Process Validation
- [ ] Log Processing
- [ ] Error Handling
- [ ] Logging
- [ ] Alerts
- [ ] Scheduling
- [ ] Automation

## TS-6 Control-M / Batch
- [ ] Control-M Jobs
- [ ] Folders
- [ ] Workflows
- [ ] Dependencies
- [ ] Conditions
- [ ] Calendars
- [ ] SLA
- [ ] Hold
- [ ] Release
- [ ] Rerun
- [ ] Restart
- [ ] Failures
- [ ] Alerts
- [ ] Batch Monitoring
- [ ] SOD
- [ ] EOD
- [ ] Reconciliation
- [ ] Batch Troubleshooting

## TS-7 Git
- [ ] Repository
- [ ] Clone
- [ ] Branch
- [ ] Commit
- [ ] Push
- [ ] Pull
- [ ] Fetch
- [ ] Merge
- [ ] Rebase
- [ ] Stash
- [ ] Tag
- [ ] Reset
- [ ] Revert
- [ ] Diff
- [ ] Pull Request
- [ ] Code Review
- [ ] Branching Strategy
- [ ] Git Troubleshooting

## TS-8 Jenkins / CI-CD
- [ ] CI
- [ ] CD
- [ ] Jenkins Architecture
- [ ] Controller
- [ ] Agent
- [ ] Pipeline
- [ ] Jenkinsfile
- [ ] Stages
- [ ] Steps
- [ ] Parameters
- [ ] Credentials
- [ ] Environment Variables
- [ ] Webhooks
- [ ] Triggers
- [ ] Artifacts
- [ ] Unit Tests
- [ ] Integration Tests
- [ ] Deployment
- [ ] Smoke Test
- [ ] Rollback
- [ ] Notifications
- [ ] Failure Handling

## TS-9 Python Automation
- [ ] Files
- [ ] pathlib
- [ ] os
- [ ] subprocess
- [ ] JSON
- [ ] XML
- [ ] CSV
- [ ] Regex
- [ ] Logging
- [ ] Exceptions
- [ ] argparse
- [ ] requests
- [ ] API Automation
- [ ] SQL Connectivity
- [ ] DB Validation
- [ ] Reconciliation Automation
- [ ] Log Analysis
- [ ] Batch Monitoring
- [ ] Alerting
- [ ] Deployment Automation

## TS-10 Networking
- [ ] OSI Model
- [ ] TCP/IP Model
- [ ] IP Addressing
- [ ] IPv4
- [ ] Subnet
- [ ] Gateway
- [ ] DNS
- [ ] DHCP
- [ ] TCP
- [ ] UDP
- [ ] Ports
- [ ] HTTP
- [ ] HTTPS
- [ ] SSH
- [ ] TLS
- [ ] Firewall
- [ ] Proxy
- [ ] Load Balancer
- [ ] Routing
- [ ] NAT
- [ ] Network Troubleshooting

## TS-11 Database for Technical Services
- [ ] Oracle Architecture Basics
- [ ] Connectivity
- [ ] Listener
- [ ] Sessions
- [ ] Locks
- [ ] Blocking
- [ ] Transactions
- [ ] Tablespaces
- [ ] Storage
- [ ] Indexes
- [ ] Execution Plans
- [ ] Query Performance
- [ ] Database Health
- [ ] Connection Failures
- [ ] SQL Troubleshooting

## TS-12 Docker
- [ ] Docker Fundamentals
- [ ] Images
- [ ] Containers
- [ ] Dockerfile
- [ ] Registry
- [ ] Volumes
- [ ] Networks
- [ ] Environment Variables
- [ ] Docker Compose
- [ ] Logs
- [ ] Container Troubleshooting

## TS-13 Kubernetes
- [ ] Kubernetes Fundamentals
- [ ] Cluster
- [ ] Node
- [ ] Pod
- [ ] Deployment
- [ ] ReplicaSet
- [ ] Service
- [ ] ConfigMap
- [ ] Secret
- [ ] Namespace
- [ ] Ingress
- [ ] Health Checks
- [ ] Scaling
- [ ] Logs
- [ ] Rolling Deployment

## TS-14 Ansible
- [ ] Inventory
- [ ] Playbook
- [ ] Tasks
- [ ] Modules
- [ ] Variables
- [ ] Handlers
- [ ] Roles
- [ ] Templates
- [ ] Idempotency
- [ ] Deployment Automation

## TS-15 Terraform / IaC
- [ ] Infrastructure as Code
- [ ] Provider
- [ ] Resource
- [ ] Variables
- [ ] Outputs
- [ ] State
- [ ] Modules
- [ ] Plan
- [ ] Apply
- [ ] Destroy
- [ ] Remote State
- [ ] Lifecycle

## TS-16 AWS / Cloud
- [ ] AWS Regions
- [ ] Availability Zones
- [ ] IAM
- [ ] EC2
- [ ] S3
- [ ] VPC
- [ ] Subnets
- [ ] Route Tables
- [ ] Internet Gateway
- [ ] NAT Gateway
- [ ] Security Groups
- [ ] RDS
- [ ] Load Balancer
- [ ] CloudWatch
- [ ] Secrets Manager
- [ ] Cloud Deployment

## TS-17 Observability
- [ ] Logs
- [ ] Metrics
- [ ] Traces
- [ ] Alerts
- [ ] Dashboards
- [ ] Health Checks
- [ ] Availability
- [ ] SLA
- [ ] SLO
- [ ] Error Rate
- [ ] Latency
- [ ] Throughput
- [ ] Capacity
- [ ] OpenTelemetry Concepts
- [ ] Splunk Concepts
- [ ] CloudWatch
- [ ] Grafana Concepts
- [ ] Prometheus Concepts

## TS-18 Security
- [ ] Authentication
- [ ] Authorization
- [ ] IAM
- [ ] RBAC
- [ ] Least Privilege
- [ ] SSH
- [ ] TLS
- [ ] Certificates
- [ ] Secrets
- [ ] Credentials
- [ ] Vault Concepts
- [ ] Security Groups
- [ ] Firewall
- [ ] Network Security
- [ ] Audit
- [ ] Data Masking

## TS-19 Production Engineering
- [ ] Incident Management
- [ ] Problem Management
- [ ] Change Management
- [ ] Release Management
- [ ] RCA
- [ ] Severity
- [ ] SLA
- [ ] SLO
- [ ] Escalation
- [ ] On-Call
- [ ] Monitoring
- [ ] Alerting
- [ ] Runbooks
- [ ] Knowledge Base
- [ ] Preventive Actions
- [ ] Capacity Planning
- [ ] Reliability
- [ ] Availability
- [ ] Disaster Recovery
- [ ] Backup
- [ ] Recovery
- [ ] Business Continuity / BCP

## TS-20 Performance Engineering
- [ ] CPU Analysis
- [ ] Memory Analysis
- [ ] Disk Analysis
- [ ] Network Analysis
- [ ] Database Performance
- [ ] Application Response Time
- [ ] Batch Duration
- [ ] Throughput
- [ ] Latency
- [ ] Bottleneck Identification
- [ ] Baseline
- [ ] Capacity
- [ ] Load Testing
- [ ] Stress Testing

## TS-21 Murex Troubleshooting
- [ ] Application Unavailable
- [ ] Login Issue
- [ ] Authentication Issue
- [ ] Authorization Issue
- [ ] Server Issue
- [ ] Process Issue
- [ ] CPU Issue
- [ ] Memory Issue
- [ ] Disk Issue
- [ ] Database Issue
- [ ] Network Issue
- [ ] Port Issue
- [ ] DNS Issue
- [ ] Interface Issue
- [ ] MxML Issue
- [ ] Datamart Issue
- [ ] Feeder Issue
- [ ] Market Data Issue
- [ ] Static Data Issue
- [ ] Batch Issue
- [ ] EOD Issue
- [ ] SOD Issue
- [ ] Report Issue
- [ ] Missing Trade Issue
- [ ] Reconciliation Issue
- [ ] Performance Issue
- [ ] Deployment Issue
- [ ] Upgrade Issue
- [ ] Configuration Issue

---

# 5. Integrated End-to-End Scenarios

## Scenario 1 — Trade Booked but Missing from Datamart
- [ ] Trade Capture
- [ ] MxML Integration
- [ ] Trade Processing
- [ ] Feeder
- [ ] Datamart
- [ ] Report
- [ ] Trace Data Lineage
- [ ] Identify Break
- [ ] RCA
- [ ] Fix / Reprocess
- [ ] Validate

## Scenario 2 — MxML Message Rejected
- [ ] XML Creation
- [ ] XML Validation
- [ ] MxML Processing
- [ ] Interface
- [ ] Logs
- [ ] Error Identification
- [ ] RCA
- [ ] Retry / Reprocess
- [ ] Validation

## Scenario 3 — EOD Failed
- [ ] Control-M
- [ ] Job Dependency
- [ ] Linux
- [ ] Murex Process
- [ ] Database
- [ ] Logs
- [ ] Root Cause
- [ ] Restart / Rerun
- [ ] Reconciliation
- [ ] EOD Validation

## Scenario 4 — Regulatory Report Mismatch
- [ ] Source Data
- [ ] Trade Data
- [ ] Datamart
- [ ] SQL
- [ ] Report
- [ ] Reconciliation
- [ ] Break Identification
- [ ] RCA
- [ ] Corrective Action
- [ ] Validation

## Scenario 5 — Deployment Failed
- [ ] Git
- [ ] Jenkins
- [ ] Build
- [ ] Artifact
- [ ] Deployment
- [ ] Environment
- [ ] Logs
- [ ] Failure Analysis
- [ ] Rollback
- [ ] Smoke Test
- [ ] Validation

## Scenario 6 — Murex Application Slow
- [ ] Application Layer
- [ ] CPU
- [ ] Memory
- [ ] Network
- [ ] Database
- [ ] Logs
- [ ] Monitoring
- [ ] Bottleneck Identification
- [ ] RCA
- [ ] Performance Fix
- [ ] Validation

---

# 6. Professional & Client Skills

- [ ] Incident Communication
- [ ] Technical Documentation
- [ ] Runbook Writing
- [ ] RCA Writing
- [ ] Change Request
- [ ] Release Notes
- [ ] Deployment Plan
- [ ] Rollback Plan
- [ ] Client Communication
- [ ] Requirement Understanding
- [ ] Technical Discussions
- [ ] Stakeholder Management
- [ ] Incident Calls
- [ ] Status Updates
- [ ] Handover
- [ ] Knowledge Transfer (KT)
- [ ] Interview Communication
- [ ] Professional English

---

# 7. Practical Project Tracking

## Project 1 — Murex Datamart / Reporting
- [ ] Design source-to-report data flow
- [ ] Create sample trade dataset
- [ ] Create reference/static data
- [ ] Create fact/dimension model
- [ ] Write SQL extraction
- [ ] Build reconciliation queries
- [ ] Simulate missing trade
- [ ] Simulate duplicate trade
- [ ] Simulate wrong amount/currency
- [ ] Generate exception report
- [ ] Document RCA
- [ ] Create production runbook

## Project 2 — MxML / Integration
- [ ] Create sample XML
- [ ] Validate XML
- [ ] Work with namespaces
- [ ] Write XPath examples
- [ ] Understand XSD
- [ ] Simulate valid message
- [ ] Simulate invalid message
- [ ] Build REST API test
- [ ] Test with Postman
- [ ] Build Python API client
- [ ] Simulate retry/reprocessing
- [ ] Create integration troubleshooting runbook

## Project 3 — Technical Services / DevOps
- [ ] Linux troubleshooting lab
- [ ] Shell automation script
- [ ] Control-M-style batch workflow
- [ ] Git repository
- [ ] Branching workflow
- [ ] Jenkins pipeline
- [ ] Build/test/deploy pipeline
- [ ] Dockerize sample application
- [ ] Kubernetes fundamentals lab
- [ ] Ansible deployment lab
- [ ] Terraform IaC lab
- [ ] AWS deployment lab
- [ ] Monitoring / logging lab
- [ ] Incident simulation
- [ ] RCA document
- [ ] Rollback exercise

---

# 8. Interview Readiness Tracking

## Murex Functional
- [ ] Explain Murex end-to-end
- [ ] Explain trade lifecycle
- [ ] Explain FO/MO/BO
- [ ] Explain risk and P&L
- [ ] Explain settlement
- [ ] Explain accounting
- [ ] Explain regulatory reporting
- [ ] Explain Datamart

## Datamart
- [ ] Explain Datamart architecture
- [ ] Explain data model
- [ ] Explain feeders
- [ ] Explain extraction
- [ ] Explain measures/dimensions
- [ ] Explain reconciliation
- [ ] Solve SQL scenarios
- [ ] Troubleshoot missing data
- [ ] Troubleshoot report mismatch
- [ ] Explain performance tuning

## MxML / Integration
- [ ] Explain XML
- [ ] Explain XSD/XPath
- [ ] Explain MxML
- [ ] Explain inbound/outbound
- [ ] Explain STP
- [ ] Explain integration architecture
- [ ] Troubleshoot rejected messages
- [ ] Explain REST APIs
- [ ] Explain OAuth2/TLS
- [ ] Explain retry/reprocessing

## Technical Services / DevOps
- [ ] Explain MX.3 architecture
- [ ] Explain environments
- [ ] Explain deployment lifecycle
- [ ] Linux troubleshooting
- [ ] Shell scripting
- [ ] Control-M
- [ ] Git
- [ ] Jenkins
- [ ] Python automation
- [ ] Networking
- [ ] Oracle troubleshooting
- [ ] Docker
- [ ] Kubernetes
- [ ] Ansible
- [ ] Terraform
- [ ] AWS
- [ ] Monitoring
- [ ] Security
- [ ] Production engineering
- [ ] Performance troubleshooting

## Scenario-Based Interviews
- [ ] Missing trade
- [ ] Missing Datamart data
- [ ] Report mismatch
- [ ] MxML rejection
- [ ] Interface failure
- [ ] Market data failure
- [ ] Static data failure
- [ ] EOD failure
- [ ] Batch failure
- [ ] DB issue
- [ ] Network issue
- [ ] Deployment failure
- [ ] Performance issue
- [ ] Production incident
- [ ] RCA explanation

---

# 9. Six-Month Progress Tracker

| Month | Focus | Status |
|---|---|---|
| Month 1 | Capital Markets + Murex Functional + MX.3 Architecture + Datamart Fundamentals | [ ] |
| Month 2 | Datamart Deep Dive + MxML Basics + Integration Fundamentals | [ ] |
| Month 3 | MxML Deep Dive + Integration + EOD/SOD + Batch + Production Support | [ ] |
| Month 4 | Integrated Murex-Style Project + Git/Jenkins/Python Automation | [ ] |
| Month 5 | Applications + Mock Interviews + Datamart/MxML/Technical Services Interview Prep | [ ] |
| Month 6 | Interview Mode + Gap Fixing + Advanced Scenarios | [ ] |

---

# 10. Weekly Tracking Template

## Week __
**Dates:** YYYY-MM-DD → YYYY-MM-DD

### Topics
- [ ] Topic 1
- [ ] Topic 2
- [ ] Topic 3
- [ ] Topic 4

### Practice
- [ ] Hands-on Lab
- [ ] SQL Practice
- [ ] Linux/Shell Practice
- [ ] Murex Scenario
- [ ] Production Troubleshooting

### Interview
- [ ] 10 Concept Questions
- [ ] 5 Scenario Questions
- [ ] Explain One Topic Without Notes
- [ ] Mock Interview

### Evidence
**Notes / Git path:**
- `docs/`
- `labs/`
- `scripts/`
- `sql/`
- `scenarios/`
- `runbooks/`

### Weekly Review
- What I learned:
- What I can explain:
- What I practiced:
- What I struggled with:
- What needs revision:
- Next week's focus:

---

# 11. Master Progress Dashboard

| Area | Status | Practical Done | Interview Ready |
|---|---|---|---|
| Capital Markets | [ ] | [ ] | [ ] |
| Murex Functional | [ ] | [ ] | [ ] |
| Datamart | [ ] | [ ] | [ ] |
| Reporting | [ ] | [ ] | [ ] |
| MxML | [ ] | [ ] | [ ] |
| Integration | [ ] | [ ] | [ ] |
| Technical Services | [ ] | [ ] | [ ] |
| Linux/Unix | [ ] | [ ] | [ ] |
| Shell/Bash | [ ] | [ ] | [ ] |
| Control-M/Batch | [ ] | [ ] | [ ] |
| Oracle/SQL | [ ] | [ ] | [ ] |
| Git | [ ] | [ ] | [ ] |
| Jenkins/CI-CD | [ ] | [ ] | [ ] |
| Python Automation | [ ] | [ ] | [ ] |
| Networking | [ ] | [ ] | [ ] |
| Docker | [ ] | [ ] | [ ] |
| Kubernetes | [ ] | [ ] | [ ] |
| Ansible | [ ] | [ ] | [ ] |
| Terraform | [ ] | [ ] | [ ] |
| AWS/Cloud | [ ] | [ ] | [ ] |
| Observability | [ ] | [ ] | [ ] |
| Security | [ ] | [ ] | [ ] |
| Production Engineering | [ ] | [ ] | [ ] |
| Performance | [ ] | [ ] | [ ] |
| Integrated Scenarios | [ ] | [ ] | [ ] |
| Interview Readiness | [ ] | [ ] | [ ] |

---

# 12. Git Repository Structure

```text
murex-career-roadmap/
├── README.md
├── ROADMAP.md
├── TRACKING.md
├── 01-capital-markets/
├── 02-murex-functional/
├── 03-datamart/
│   ├── notes/
│   ├── sql/
│   ├── labs/
│   ├── reconciliation/
│   └── runbooks/
├── 04-mxml-integration/
│   ├── notes/
│   ├── xml/
│   ├── api/
│   ├── labs/
│   └── runbooks/
├── 05-technical-services/
│   ├── linux/
│   ├── shell/
│   ├── control-m/
│   ├── networking/
│   ├── oracle/
│   └── troubleshooting/
├── 06-devops/
│   ├── git/
│   ├── jenkins/
│   ├── docker/
│   ├── kubernetes/
│   ├── ansible/
│   └── terraform/
├── 07-cloud/
│   └── aws/
├── 08-python-automation/
│   ├── scripts/
│   ├── api/
│   ├── database/
│   └── monitoring/
├── 09-projects/
│   ├── datamart-project/
│   ├── integration-project/
│   └── devops-project/
├── 10-production-support/
│   ├── incidents/
│   ├── rca/
│   ├── runbooks/
│   └── scenarios/
└── 11-interview-prep/
    ├── functional/
    ├── datamart/
    ├── mxml/
    ├── technical/
    └── scenarios/
```

---

# Definition of Done

A topic should be marked `[x]` only when all applicable items below are true:

- [ ] I understand the concept.
- [ ] I can explain **why** it is used.
- [ ] I can explain the basic architecture/flow.
- [ ] I can give a banking example.
- [ ] I can connect it to Murex.
- [ ] I completed a practical exercise where applicable.
- [ ] I can troubleshoot at least one realistic issue.
- [ ] I can answer basic interview questions.
- [ ] I have saved useful notes/code/lab evidence in Git.

> Important: Do not chase completion percentage alone. The target is demonstrable, practical, interview-ready capability.
