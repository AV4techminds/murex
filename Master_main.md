This roadmap follows a strict subject-by-subject approach.

### For every subject:

1. Fundamentals
2. Complete basic concepts
3. Intermediate concepts
4. Hands-on practice
5. Troubleshooting
6. Real-world scenarios
7. Murex/Banking application
8. Interview preparation
9. Mini projects
10. Review and revision

### Important Rules

- Do not skip important fundamentals.
- Do not jump randomly between technologies.
- Complete one subject before moving to the next major subject.
- Use hands-on practice wherever possible.
- Use Pluralsight for structured learning and sandbox practice.
- Maintain notes and exercises in Git.
- Connect technical concepts to Banking/Murex only after understanding the concept itself.
- Do not claim simulated Murex work as real MX.3 production experience.
- Build genuine technical and domain knowledge that can support real Murex opportunities.

---

# 🗺️ Overall Roadmap

```text
Python
   ↓
Linux / Unix
   ↓
Shell Scripting / Bash
   ↓
Networking
   ↓
DevOps
   ↓
Cloud
   ↓
Banking & Capital Markets
   ↓
Murex Functional
   ↓
Murex Technical
   ↓
Murex Production Support
   ↓
Automation / DevOps / Troubleshooting
   ↓
Strong Banking Technology Profile
````

---

# 🐍 01. Python

## A. Python Fundamentals

* [ ] Python installation & execution
* [ ] Interpreter vs compiler concepts
* [ ] Python syntax
* [ ] Indentation
* [ ] Comments
* [ ] Variables
* [ ] Constants and naming conventions
* [ ] Keywords
* [ ] Identifiers
* [ ] Dynamic typing
* [ ] Mutable vs immutable objects
* [ ] Memory/reference basics

---

## B. Python Data Types

* [ ] `int`
* [ ] `float`
* [ ] `complex`
* [ ] `bool`
* [ ] `str`
* [ ] `None`
* [ ] Type conversion
* [ ] `type()`
* [ ] `isinstance()`

---

## C. Operators

* [ ] Arithmetic operators
* [ ] Comparison operators
* [ ] Logical operators
* [ ] Assignment operators
* [ ] Bitwise operators
* [ ] Membership operators
* [ ] Identity operators
* [ ] Operator precedence

---

## D. Strings

* [ ] String creation
* [ ] Indexing
* [ ] Slicing
* [ ] String methods
* [ ] String formatting
* [ ] f-strings
* [ ] Escape sequences
* [ ] Unicode basics

---

## E. Control Flow

* [ ] `if`
* [ ] `elif`
* [ ] `else`
* [ ] Nested conditions
* [ ] `for`
* [ ] `while`
* [ ] `range()`
* [ ] `break`
* [ ] `continue`
* [ ] `pass`

---

## F. Data Structures

### Lists

* [ ] Creating lists
* [ ] Indexing
* [ ] Slicing
* [ ] List methods
* [ ] Nested lists

### Tuples

* [ ] Creating tuples
* [ ] Indexing
* [ ] Slicing
* [ ] Tuple methods
* [ ] Tuple unpacking

### Sets

* [ ] Creating sets
* [ ] Adding/removing elements
* [ ] Set operations
* [ ] Union
* [ ] Intersection
* [ ] Difference

### Dictionaries

* [ ] Keys and values
* [ ] Creating dictionaries
* [ ] Accessing values
* [ ] Updating dictionaries
* [ ] Dictionary methods
* [ ] Nested dictionaries

### General

* [ ] Mutability
* [ ] References
* [ ] Copy vs reference
* [ ] Shallow copy
* [ ] Deep copy

---

## G. Comprehensions

* [ ] List comprehensions
* [ ] Dictionary comprehensions
* [ ] Set comprehensions
* [ ] Generator expressions

---

## H. Functions

* [ ] Defining functions
* [ ] Calling functions
* [ ] Parameters
* [ ] Arguments
* [ ] Return values
* [ ] Default arguments
* [ ] Keyword arguments
* [ ] Positional arguments
* [ ] `*args`
* [ ] `**kwargs`
* [ ] Scope
* [ ] LEGB rule
* [ ] `global`
* [ ] `nonlocal`
* [ ] Lambda functions
* [ ] Recursion

---

## I. Modules and Packages

* [ ] `import`
* [ ] `from ... import`
* [ ] Standard library
* [ ] Custom modules
* [ ] Packages
* [ ] `__name__`
* [ ] `__main__`
* [ ] Virtual environments
* [ ] `pip`
* [ ] Package installation
* [ ] `requirements.txt`

---

## J. Exception Handling

* [ ] Exceptions vs errors
* [ ] `try`
* [ ] `except`
* [ ] `else`
* [ ] `finally`
* [ ] Multiple exceptions
* [ ] Custom exceptions
* [ ] `raise`

---

## K. File Handling

* [ ] Reading files
* [ ] Writing files
* [ ] Appending files
* [ ] Text files
* [ ] Binary files
* [ ] File modes
* [ ] Context managers
* [ ] `with`
* [ ] `pathlib`

---

## L. Object-Oriented Programming

* [ ] Classes
* [ ] Objects
* [ ] Attributes
* [ ] Methods
* [ ] Constructor
* [ ] Instance methods
* [ ] Class methods
* [ ] Static methods
* [ ] Instance variables
* [ ] Class variables
* [ ] Encapsulation
* [ ] Inheritance
* [ ] Polymorphism
* [ ] Abstraction
* [ ] Composition
* [ ] Special methods / magic methods

---

## M. Advanced Core Python

* [ ] Iterators
* [ ] Generators
* [ ] Decorators
* [ ] Closures
* [ ] Context managers
* [ ] `dataclasses`
* [ ] Type hints
* [ ] `typing`

---

## N. Practical Python

* [ ] CSV
* [ ] JSON
* [ ] Regular expressions
* [ ] `datetime`
* [ ] `os`
* [ ] `sys`
* [ ] `subprocess`
* [ ] Logging
* [ ] Debugging
* [ ] Unit testing
* [ ] API/HTTP basics
* [ ] Automation

---

## Python → Murex Connection

```text
Python
   ↓
File Processing
   ↓
Trade/Input File Validation
   ↓
Log Parsing
   ↓
Exception Detection
   ↓
Report Generation
   ↓
API/Interface Automation
   ↓
Monitoring
   ↓
Production Support Automation
```

---

# 🐧 02. Linux / Unix

## A. Linux Fundamentals

* [ ] What is an Operating System?
* [ ] Kernel
* [ ] Shell
* [ ] Linux distributions
* [ ] Processes
* [ ] Users
* [ ] Filesystem
* [ ] Linux architecture basics

---

## B. Linux Filesystem

* [ ] Root `/`
* [ ] `/home`
* [ ] `/etc`
* [ ] `/var`
* [ ] `/tmp`
* [ ] `/usr`
* [ ] `/opt`
* [ ] `/bin`
* [ ] `/sbin`
* [ ] Absolute paths
* [ ] Relative paths

---

## C. Basic Linux Commands

* [ ] `ls`
* [ ] `cd`
* [ ] `pwd`
* [ ] `cp`
* [ ] `mv`
* [ ] `rm`
* [ ] `mkdir`
* [ ] `touch`
* [ ] `cat`
* [ ] `less`
* [ ] `head`
* [ ] `tail`
* [ ] `wc`
* [ ] `sort`
* [ ] `uniq`

---

## D. Linux Permissions

* [ ] Read permission
* [ ] Write permission
* [ ] Execute permission
* [ ] `chmod`
* [ ] `chown`
* [ ] `chgrp`
* [ ] Numeric permissions
* [ ] Symbolic permissions
* [ ] ACL basics
* [ ] `umask`

---

## E. Users and Groups

* [ ] User management
* [ ] Groups
* [ ] `/etc/passwd`
* [ ] `/etc/group`
* [ ] `/etc/shadow`
* [ ] `sudo`
* [ ] SSH authentication

---

## F. Processes

* [ ] Process vs thread
* [ ] PID
* [ ] PPID
* [ ] Foreground processes
* [ ] Background processes
* [ ] `ps`
* [ ] `top`
* [ ] `htop`
* [ ] `kill`
* [ ] Signals
* [ ] `jobs`
* [ ] `bg`
* [ ] `fg`

---

## G. Services

* [ ] systemd
* [ ] `systemctl`
* [ ] Service lifecycle
* [ ] Starting services
* [ ] Stopping services
* [ ] Restarting services
* [ ] Service status
* [ ] Startup configuration

---

## H. Storage

* [ ] Disk
* [ ] Partition
* [ ] Filesystem
* [ ] Mounting
* [ ] `df`
* [ ] `du`
* [ ] `lsblk`
* [ ] Disk utilization
* [ ] Inodes

---

## I. Logs

* [ ] `/var/log`
* [ ] System logs
* [ ] Application logs
* [ ] `journalctl`
* [ ] Log rotation
* [ ] Log analysis basics

---

## J. Linux Networking

* [ ] `ip`
* [ ] `ping`
* [ ] `ss`
* [ ] `netstat` basics
* [ ] `traceroute`
* [ ] `curl`
* [ ] `wget`
* [ ] DNS utilities

---

## K. Scheduling

* [ ] `cron`
* [ ] `crontab`
* [ ] `at`

---

## L. Linux Security

* [ ] File permissions
* [ ] SSH
* [ ] sudo
* [ ] Firewall basics
* [ ] Process security
* [ ] Environment variables
* [ ] Secure file handling

---

## M. Linux Troubleshooting

* [ ] CPU troubleshooting
* [ ] Memory troubleshooting
* [ ] Disk troubleshooting
* [ ] Process troubleshooting
* [ ] Service troubleshooting
* [ ] Network troubleshooting
* [ ] Log troubleshooting

---

## Linux → Murex Connection

```text
Murex Application
       ↓
Linux Server
       ↓
Processes
       ↓
Services
       ↓
CPU / Memory / Disk
       ↓
Application Logs
       ↓
Troubleshooting
```

---

# 💻 03. Shell Scripting / Bash

## A. Shell Fundamentals

* [ ] Shell types
* [ ] Bash
* [ ] Shell execution
* [ ] Shebang
* [ ] Variables
* [ ] Environment variables
* [ ] Command substitution
* [ ] Exit status

---

## B. Input / Output

* [ ] `echo`
* [ ] `read`
* [ ] stdin
* [ ] stdout
* [ ] stderr
* [ ] Redirection
* [ ] Pipes

---

## C. Conditional Logic

* [ ] `if`
* [ ] `elif`
* [ ] `else`
* [ ] `case`

---

## D. Loops

* [ ] `for`
* [ ] `while`
* [ ] `until`

---

## E. Functions

* [ ] Functions
* [ ] Parameters
* [ ] Return status
* [ ] Local variables

---

## F. Text Processing

* [ ] `grep`
* [ ] `sed`
* [ ] `awk`
* [ ] `cut`
* [ ] `tr`
* [ ] `sort`
* [ ] `uniq`
* [ ] `xargs`

---

## G. File Operations

* [ ] File tests
* [ ] Directory tests
* [ ] Finding files
* [ ] File manipulation
* [ ] Wildcards

---

## H. Advanced Shell Basics

* [ ] Arrays
* [ ] Quoting
* [ ] Command substitution
* [ ] Regular expressions
* [ ] Exit codes
* [ ] Signals
* [ ] `trap`
* [ ] Error handling
* [ ] Logging

---

## I. Automation

* [ ] Cron
* [ ] Batch scripts
* [ ] Monitoring scripts
* [ ] Backup scripts
* [ ] Validation scripts
* [ ] Operational scripts

---

## Shell → Murex Connection

```text
Murex Batch
    ↓
Shell Script
    ↓
Start / Stop / Validate
    ↓
Check Processes
    ↓
Check Logs
    ↓
Check Output
    ↓
Generate Operational Status
```

---

# 🌐 04. Networking

## A. Networking Fundamentals

* [ ] What is networking?
* [ ] Network types
* [ ] LAN
* [ ] WAN
* [ ] Network devices
* [ ] Client/server
* [ ] OSI model
* [ ] TCP/IP model

---

## B. Ethernet

* [ ] MAC addresses
* [ ] Frames
* [ ] Switches
* [ ] ARP

---

## C. IP Networking

* [ ] IPv4
* [ ] IPv6 basics
* [ ] Public IP
* [ ] Private IP
* [ ] Subnet masks
* [ ] CIDR
* [ ] Subnetting

---

## D. Transport Layer

* [ ] TCP
* [ ] UDP
* [ ] Ports
* [ ] Sockets
* [ ] TCP three-way handshake
* [ ] TCP states

---

## E. Network Services

* [ ] DNS
* [ ] DHCP
* [ ] NTP

---

## F. Routing

* [ ] Routing basics
* [ ] Default gateway
* [ ] Static routing
* [ ] NAT

---

## G. Application Protocols

* [ ] HTTP
* [ ] HTTPS
* [ ] FTP basics
* [ ] SFTP
* [ ] SSH
* [ ] SMTP basics

---

## H. Network Security

* [ ] Firewall
* [ ] Proxy
* [ ] VPN
* [ ] TLS
* [ ] SSL concepts
* [ ] Certificates
* [ ] Load balancer basics

---

## I. Network Troubleshooting

* [ ] `ping`
* [ ] `traceroute`
* [ ] `nslookup`
* [ ] `dig`
* [ ] `curl`
* [ ] Telnet concepts
* [ ] Netcat concepts
* [ ] `ss`
* [ ] Wireshark basics

---

## Networking → Murex Connection

```text
Upstream System
      ↓
Network
      ↓
Firewall
      ↓
Load Balancer / Proxy
      ↓
Murex
      ↓
Database
      ↓
Downstream Systems
```

---

# ⚙️ 05. DevOps

## A. DevOps Fundamentals

* [ ] DevOps philosophy
* [ ] DevOps culture
* [ ] SDLC
* [ ] Agile basics
* [ ] Continuous Integration
* [ ] Continuous Delivery
* [ ] Continuous Deployment
* [ ] Infrastructure
* [ ] Automation

---

## B. Git

* [ ] Repository
* [ ] Working tree
* [ ] Staging
* [ ] Commit
* [ ] Branch
* [ ] Merge
* [ ] Rebase
* [ ] Pull
* [ ] Push
* [ ] Tag
* [ ] Conflict resolution
* [ ] `.gitignore`
* [ ] Git workflows

---

## C. CI/CD

* [ ] Pipeline
* [ ] Build
* [ ] Test
* [ ] Artifact
* [ ] Deployment
* [ ] Environments
* [ ] Approval
* [ ] Rollback

---

## D. CI/CD Tools

* [ ] Jenkins
* [ ] GitHub Actions
* [ ] GitLab CI concepts

---

## E. Docker

* [ ] Containers
* [ ] Images
* [ ] Dockerfile
* [ ] Registry
* [ ] Volumes
* [ ] Networks
* [ ] Container lifecycle
* [ ] Docker Compose basics

---

## F. Configuration

* [ ] Environment variables
* [ ] Configuration files
* [ ] Secrets
* [ ] Configuration management concepts

---

## G. Monitoring

* [ ] Metrics
* [ ] Logs
* [ ] Alerts
* [ ] Health checks
* [ ] Observability basics

---

## H. Deployment

* [ ] Deployment strategies
* [ ] Blue/green deployment
* [ ] Rolling deployment
* [ ] Rollback
* [ ] Release management

---

## I. DevSecOps Basics

* [ ] Security in CI/CD
* [ ] Dependency scanning concepts
* [ ] Secret scanning concepts
* [ ] Image scanning concepts
* [ ] Secure deployment concepts

---

## DevOps → Murex Connection

```text
Developer
   ↓
Git
   ↓
CI
   ↓
Testing
   ↓
Build
   ↓
Artifact
   ↓
Deployment
   ↓
DEV / TEST / UAT / PROD
   ↓
Monitoring
   ↓
Rollback / Support
```

---

# ☁️ 06. Cloud

## A. Cloud Fundamentals

* [ ] Cloud computing
* [ ] Regions
* [ ] Availability Zones
* [ ] IaaS
* [ ] PaaS
* [ ] SaaS
* [ ] Public cloud
* [ ] Private cloud
* [ ] Hybrid cloud

---

## B. Compute

* [ ] Virtual machines
* [ ] Virtualization concepts
* [ ] Containers
* [ ] Serverless concepts

---

## C. Storage

* [ ] Object storage
* [ ] Block storage
* [ ] File storage

---

## D. Cloud Networking

* [ ] VPC / VNet
* [ ] Subnets
* [ ] Routing
* [ ] Security groups
* [ ] Load balancers
* [ ] DNS

---

## E. IAM

* [ ] Users
* [ ] Groups
* [ ] Roles
* [ ] Policies
* [ ] Least privilege

---

## F. Databases

* [ ] Relational databases
* [ ] NoSQL concepts
* [ ] Managed databases

---

## G. Reliability

* [ ] High availability
* [ ] Scalability
* [ ] Auto-scaling
* [ ] Backup
* [ ] Disaster recovery

---

## H. Cloud Security

* [ ] IAM
* [ ] Encryption
* [ ] Network security
* [ ] Secrets management
* [ ] Security logging

---

## I. Cloud Monitoring

* [ ] Metrics
* [ ] Logs
* [ ] Alerts
* [ ] Health monitoring

---

## J. Cloud Architecture

* [ ] Basic cloud architecture
* [ ] Application architecture
* [ ] Network architecture
* [ ] High availability architecture
* [ ] Basic disaster recovery architecture

---

## Cloud Strategy

> Learn cloud fundamentals first and then choose **one major cloud platform** for practical learning instead of trying to master AWS, Azure and GCP simultaneously.

---

# 🏦 07. Banking & Capital Markets

## A. Banking Fundamentals

* [ ] Commercial banking
* [ ] Investment banking
* [ ] Central banking
* [ ] Financial institutions
* [ ] Banks and financial markets

---

## B. Investment Banking

* [ ] Front Office
* [ ] Middle Office
* [ ] Back Office
* [ ] Trading
* [ ] Sales
* [ ] Operations

---

## C. Capital Markets

* [ ] Equity markets
* [ ] Fixed Income markets
* [ ] Foreign Exchange
* [ ] Money Markets
* [ ] Commodities
* [ ] Derivatives

---

# 📈 Financial Products

## FX

* [ ] FX Spot
* [ ] FX Forward
* [ ] FX Swap
* [ ] FX Options

## Fixed Income

* [ ] Bonds
* [ ] Coupon
* [ ] Yield
* [ ] Bond pricing
* [ ] Duration

## Derivatives

* [ ] Futures
* [ ] Options
* [ ] Swaps
* [ ] Forwards

---

# 🔄 Trade Lifecycle

```text
Order
  ↓
Execution
  ↓
Trade Capture
  ↓
Confirmation
  ↓
Settlement
  ↓
Accounting
  ↓
Reporting
```

Concepts:

* [ ] Order
* [ ] Execution
* [ ] Trade capture
* [ ] Confirmation
* [ ] Settlement
* [ ] Accounting
* [ ] Reporting

---

# ⚠️ Risk Management

* [ ] Market risk
* [ ] Credit risk
* [ ] Counterparty risk
* [ ] Liquidity risk
* [ ] Operational risk
* [ ] Value at Risk
* [ ] Stress testing

---

# 📊 Other Banking Concepts

* [ ] Market data
* [ ] Pricing
* [ ] Valuation
* [ ] P&L
* [ ] Positions
* [ ] Collateral
* [ ] Settlement
* [ ] Accounting
* [ ] Regulatory reporting
* [ ] Corporate actions
* [ ] End-of-Day processing

---

# 🏦 08. Murex Functional

## A. MX.3 Fundamentals

* [ ] What is Murex?
* [ ] What is MX.3?
* [ ] MX.3 architecture overview
* [ ] Murex ecosystem
* [ ] Murex users
* [ ] Murex modules
* [ ] Murex environments

---

## B. Trade Management

* [ ] Trade capture
* [ ] Trade lifecycle
* [ ] Trade events
* [ ] Trade amendments
* [ ] Trade cancellation
* [ ] Trade confirmation

---

## C. Products

* [ ] FX
* [ ] Money Market
* [ ] Fixed Income
* [ ] Equities
* [ ] Derivatives
* [ ] Rates
* [ ] Credit
* [ ] Commodities

---

## D. Static / Reference Data

* [ ] Static data concepts
* [ ] Reference data
* [ ] Counterparties
* [ ] Legal entities
* [ ] Instruments
* [ ] Settlement information
* [ ] Business calendars

---

## E. Market Data

* [ ] Market data concepts
* [ ] Curves
* [ ] Rates
* [ ] Prices
* [ ] Volatility
* [ ] Fixings
* [ ] Market data lifecycle

---

## F. Pricing & Valuation

* [ ] Pricing
* [ ] Valuation
* [ ] Pricing models
* [ ] Valuation concepts
* [ ] P&L
* [ ] Sensitivities

---

## G. Position Management

* [ ] Position management
* [ ] Netting
* [ ] Aggregation
* [ ] Position reporting
* [ ] P&L attribution

---

## H. Risk Management

* [ ] Market risk
* [ ] Credit risk
* [ ] Counterparty risk
* [ ] VaR
* [ ] Sensitivities
* [ ] Stress testing

---

## I. Workflow

* [ ] Trade workflow
* [ ] Approval
* [ ] Validation
* [ ] Events
* [ ] States
* [ ] Actions
* [ ] Conditions
* [ ] Workflow lifecycle

---

## J. Settlement

* [ ] Settlement instructions
* [ ] Payments
* [ ] Confirmations
* [ ] Matching
* [ ] Settlement lifecycle

---

## K. Accounting

* [ ] Accounting events
* [ ] Accounting rules
* [ ] Ledger concepts
* [ ] GL integration

---

## L. Datamart

* [ ] Datamart concepts
* [ ] Data extraction
* [ ] Reporting
* [ ] Aggregation
* [ ] Datamart architecture
* [ ] Reports

---

## M. End-of-Day

* [ ] End-of-Day concepts
* [ ] Batch processing
* [ ] Batch dependencies
* [ ] Reconciliation
* [ ] EOD monitoring
* [ ] EOD validation

---

# 🛠️ 09. Murex Technical

## A. Technical Architecture

* [ ] MX.3 technical architecture
* [ ] Application components
* [ ] Servers
* [ ] Databases
* [ ] Environments
* [ ] DEV
* [ ] TEST
* [ ] UAT
* [ ] PROD

---

## B. Configuration

* [ ] Static data configuration concepts
* [ ] Reference data configuration
* [ ] Product configuration concepts
* [ ] Business rules
* [ ] Parameters
* [ ] Environment configuration
* [ ] Configuration dependencies

---

## C. Workflow Technical Concepts

* [ ] Workflow architecture
* [ ] Events
* [ ] States
* [ ] Actions
* [ ] Conditions
* [ ] Workflow configuration
* [ ] Workflow troubleshooting

---

## D. MxML

* [ ] MxML concepts
* [ ] XML fundamentals
* [ ] MxML messages
* [ ] Trade interfaces
* [ ] Message processing
* [ ] Message validation
* [ ] Error handling
* [ ] Message reprocessing

---

## E. Interfaces

* [ ] Inbound interfaces
* [ ] Outbound interfaces
* [ ] File-based interfaces
* [ ] API-based interfaces
* [ ] Message-based interfaces
* [ ] Data mapping
* [ ] Data transformation
* [ ] Interface validation
* [ ] Interface error handling
* [ ] Interface reprocessing

---

## F. Datamart Technical

* [ ] Datamart architecture
* [ ] Data extraction
* [ ] Queries
* [ ] Reports
* [ ] Aggregation
* [ ] Scheduling
* [ ] Performance concepts
* [ ] Datamart troubleshooting

---

## G. Batch / EOD Technical

* [ ] Batch architecture
* [ ] Batch scheduling
* [ ] Dependencies
* [ ] Processing
* [ ] Monitoring
* [ ] Failure recovery
* [ ] EOD troubleshooting

---

## H. Deployment

* [ ] Release process
* [ ] Configuration promotion
* [ ] Versioning
* [ ] Change management
* [ ] Deployment validation
* [ ] Rollback

---

## I. Monitoring

* [ ] Application monitoring
* [ ] Process monitoring
* [ ] Batch monitoring
* [ ] Interface monitoring
* [ ] Log monitoring
* [ ] Health checks
* [ ] Alerts

---

## J. Logging

* [ ] Application logs
* [ ] Interface logs
* [ ] Batch logs
* [ ] Error logs
* [ ] Log analysis
* [ ] Log correlation
* [ ] Troubleshooting from logs

---

## K. Performance

* [ ] Application performance basics
* [ ] Database performance basics
* [ ] Network performance basics
* [ ] Resource utilization
* [ ] Bottleneck identification
* [ ] Performance troubleshooting

---

## L. Production Support

* [ ] Monitoring
* [ ] Incident management
* [ ] Problem management
* [ ] Root Cause Analysis
* [ ] Performance troubleshooting
* [ ] Data issues
* [ ] Interface issues
* [ ] Batch failures
* [ ] Application failures
* [ ] Incident documentation
* [ ] Recovery procedures
* [ ] Production validation

---

# 🧪 10. Testing & Production Engineering

## A. Testing Fundamentals

* [ ] SDLC testing concepts
* [ ] Unit testing
* [ ] Integration testing
* [ ] System testing
* [ ] Regression testing
* [ ] UAT
* [ ] Smoke testing

---

## B. Test Management

* [ ] Test cases
* [ ] Test scenarios
* [ ] Test data
* [ ] Defect lifecycle
* [ ] Defect reporting
* [ ] Test execution
* [ ] Test evidence

---

## C. Production Validation

* [ ] Deployment validation
* [ ] Smoke validation
* [ ] Production verification
* [ ] Reconciliation
* [ ] Post-deployment checks

---

# 🚨 11. Murex Production Support / Incident Lab

This will combine all previous subjects.

---

## Incident 001 — Trade Interface Failure

Scenario:

```text
Upstream System
      ↓
Interface
      ↓
Murex
```

Investigation:

* [ ] Networking
* [ ] DNS
* [ ] Connectivity
* [ ] Ports
* [ ] Firewall concepts
* [ ] Linux process
* [ ] Application logs
* [ ] MxML/message
* [ ] Interface validation
* [ ] SQL/data validation
* [ ] Root Cause Analysis

---

## Incident 002 — Murex Batch Failure

Investigation:

* [ ] Linux
* [ ] Shell
* [ ] Process status
* [ ] Batch logs
* [ ] Disk space
* [ ] Memory/CPU
* [ ] Dependencies
* [ ] Scheduling
* [ ] Output validation
* [ ] Recovery
* [ ] EOD concepts

---

## Incident 003 — Datamart Report Missing Trades

Investigation:

```text
Upstream
   ↓
Trade
   ↓
Processing
   ↓
Database
   ↓
Datamart
   ↓
Report
```

Skills:

* [ ] SQL
* [ ] Data validation
* [ ] Datamart concepts
* [ ] Report validation
* [ ] Murex trade lifecycle
* [ ] Troubleshooting

---

## Incident 004 — Murex Application Unavailable

Investigation:

* [ ] Network
* [ ] DNS
* [ ] Port
* [ ] Firewall
* [ ] Linux process
* [ ] Service
* [ ] CPU
* [ ] Memory
* [ ] Disk
* [ ] Application logs
* [ ] Deployment
* [ ] Configuration
* [ ] Recovery

---

## Incident 005 — Incorrect P&L

Investigation:

```text
Trade
  ↓
Market Data
  ↓
Pricing
  ↓
Valuation
  ↓
Position
  ↓
Risk
  ↓
P&L
```

Skills:

* [ ] Trade validation
* [ ] Market data
* [ ] Pricing
* [ ] Valuation
* [ ] Position
* [ ] Risk
* [ ] P&L
* [ ] Data validation

---

# 🔗 12. Integrated Banking Technology Project

The final training project will combine:

```text
Python
   +
Linux
   +
Shell
   +
SQL
   +
Networking
   +
Git
   +
DevOps
   +
Cloud
   +
Banking
   +
Murex Concepts
```

---

## Project Architecture

```text
                    BANKING / CAPITAL MARKETS
                             │
                             ▼
                       Trading System
                             │
                             ▼
                    ┌─────────────────┐
                    │ MUREX / MX.3    │
                    │ Training Model  │
                    └─────────────────┘
                       │      │      │
              ┌────────┘      │      └────────┐
              ▼               ▼               ▼
        Market Data         Risk/P&L       Settlement
              │               │               │
              └───────────────┼───────────────┘
                              ▼
                           Datamart
                              │
                              ▼
                       Reports / BI

Supporting Technology
──────────────────────────────────────────
Linux
Shell
Python
SQL
Networking
Git
CI/CD
Docker
Cloud
Monitoring
```

---

# 🐍 Python Project Components

* [ ] File processing
* [ ] Trade file validation
* [ ] CSV processing
* [ ] JSON processing
* [ ] Log parsing
* [ ] Error detection
* [ ] Exception reporting
* [ ] Report generation
* [ ] API integration
* [ ] Monitoring automation
* [ ] Production support automation

---

# 🐧 Linux Project Components

* [ ] Application directories
* [ ] Configuration directories
* [ ] Log directories
* [ ] Process monitoring
* [ ] Service monitoring
* [ ] Disk monitoring
* [ ] CPU monitoring
* [ ] Memory monitoring
* [ ] Log investigation
* [ ] SSH
* [ ] Permissions

---

# 💻 Shell Project Components

* [ ] Start script
* [ ] Stop script
* [ ] Process check
* [ ] Disk check
* [ ] Log check
* [ ] Batch validation
* [ ] File validation
* [ ] Backup script
* [ ] Cron scheduling
* [ ] Error handling
* [ ] Logging

---

# 🌐 Networking Project Components

* [ ] Client/server communication
* [ ] DNS
* [ ] IP addressing
* [ ] Ports
* [ ] TCP
* [ ] HTTP/HTTPS
* [ ] SSH
* [ ] Firewall concepts
* [ ] Connectivity testing
* [ ] Network troubleshooting

---

# ⚙️ DevOps Project Components

* [ ] Git repository
* [ ] Branching
* [ ] Pull/merge workflow
* [ ] CI pipeline
* [ ] Testing
* [ ] Build
* [ ] Artifact
* [ ] Deployment
* [ ] Environment management
* [ ] Docker
* [ ] Monitoring
* [ ] Rollback

---

# ☁️ Cloud Project Components

* [ ] Compute
* [ ] Storage
* [ ] Network
* [ ] IAM
* [ ] Database
* [ ] Load balancing
* [ ] Monitoring
* [ ] Security
* [ ] High availability basics

---

# 🏦 Banking Project Components

* [ ] Trade capture
* [ ] Trade lifecycle
* [ ] Market data
* [ ] Pricing
* [ ] Valuation
* [ ] Position
* [ ] Risk
* [ ] P&L
* [ ] Settlement
* [ ] Accounting
* [ ] Reporting
* [ ] EOD

---

# 🏦 Murex Project Components

* [ ] MX.3 architecture concepts
* [ ] Environments
* [ ] Configuration concepts
* [ ] Trade management
* [ ] Products
* [ ] Market data
* [ ] Pricing
* [ ] Valuation
* [ ] Position
* [ ] Risk
* [ ] Workflow
* [ ] MxML
* [ ] Interfaces
* [ ] Datamart
* [ ] Batch
* [ ] EOD
* [ ] Deployment
* [ ] Monitoring
* [ ] Troubleshooting
* [ ] Production support

---

# 📚 Learning Method

For each technical subject:

```text
1. Learn the concept
        ↓
2. Understand WHY it exists
        ↓
3. Practice it
        ↓
4. Solve exercises
        ↓
5. Troubleshoot scenarios
        ↓
6. Build a small project
        ↓
7. Understand Murex/Banking relevance
        ↓
8. Prepare interview questions
        ↓
9. Mark concept complete
```

---

# 🏆 Completion Levels

Each concept should eventually move through:

```text
⬜ Not Started
   ↓
🟡 Learning
   ↓
🟠 Practiced
   ↓
🔵 Strong
   ↓
🟢 Interview Ready
   ↓
✅ Completed
```

---

# 📌 Final Career Profile Target

The objective is to eventually build a profile around:

```text
                 BANKING DOMAIN
                       │
                       ▼
                    MUREX
                ┌──────┴──────┐
                │             │
           Functional      Technical
                              │
       ┌────────┬─────────────┼────────┐
       │        │             │        │
     Linux     SQL         Networking DevOps
       │        │             │        │
     Shell   Database      Interfaces CI/CD
       │        │             │        │
       └────────┴──────┬──────┴────────┘
                       │
                    Python
                       │
                   Automation
                       │
                    Cloud
                       │
                       ▼
              Production Support
                       │
                       ▼
             Banking Technology
```

---

# 🎯 Current Priority

## Phase 1 — Python

> **Current focus: Python**

Alongside Python:

> **15 minutes/day — Banking & Capital Markets**

Do not move to the next major technical subject until the current subject has been sufficiently covered at the planned level.

---

# 🔒 Core Principle

> **Learn the subject properly first.
> Understand the fundamentals.
> Practice it hands-on.
> Then understand where it fits into Banking and Murex.**

The final goal is not to memorize technologies.

The goal is to become capable of understanding, developing, automating, troubleshooting and supporting enterprise banking technology systems.

---

# 🚀 End Goal

```text
Strong Technical Foundation
        +
Strong Banking Knowledge
        +
Murex Functional Knowledge
        +
Murex Technical Knowledge
        +
Production Troubleshooting
        +
Automation
        +
DevOps / Cloud
        ↓
Strong Banking Technology Profile
        ↓
Murex / Banking Technology Opportunities
        ↓
Long-Term Career Flexibility
```

---

```
```
