
# Master Career Strategy

```text
Existing Skills
SQL + PL/SQL + Linux + Shell + Control-M + ETL + UAT
        ↓
Phase 1: Murex Production Support L2/L3 Foundation
        ↓
Phase 2: Murex Datamart / Reporting
        ↓
Phase 3: Murex MxML / Integration
        ↓
Phase 4: Murex Techno-Functional Consultant
        ↓
Phase 5: Murex DevOps / Cloud / Automation
        ↓
Phase 6: AI-Augmented Murex Specialist
```

Do **not** study all modules equally. Your immediate objective is a job-ready support/reporting/integration profile; advanced risk, cloud, and AI come after the core becomes strong.

## Role Order

| Order | Role | Why it fits you | Apply when |
|---:|---|---|---|
| 1 | Murex Production Support L2/L3 | Closest to Linux, Control-M, SQL, ETL, RCA, UAT | After Phase 2 foundation |
| 2 | Murex Datamart/Reporting | Closest to reporting, reconciliation, SQL, ETL | After Phase 3 basics |
| 3 | Murex MxML Integration | Uses XML/XSLT, workflow, interfaces, troubleshooting | After Phase 4 basics |
| 4 | Murex Techno-Functional | Requires deeper business + technical understanding | After working knowledge of the first three |
| 5 | Murex DevOps/Cloud | Adds automation, CI/CD, observability, resilience | After Murex core/support depth |
| 6 | AI-augmented Murex specialist | Improves analysis, automation, documentation, monitoring | Continuous, safely and responsibly |

A current senior MxML role expects trade lifecycle, static data, Murex data model, SQL, integration/post-trade workflows, troubleshooting, and stakeholder communication—this confirms why functional basics must be learned before advanced integration.[3]

# Phase 0: Orientation

**Goal:** Understand the whole Murex ecosystem before going deep.

## Learn

- What Murex MX.3 is.
- Why banks use it.
- Front office, middle office, back office.
- Treasury, trading, risk, operations, finance.
- Cross-asset concept.
- Core Murex architecture.
- Trade lifecycle overview.
- Static data versus market data.
- Product, trade, contract, event, cash flow.
- Book, portfolio, position.
- Counterparty and legal entity.
- Datamart, MxML, workflow, MSL, batch, report.
- DEV, SIT, UAT, pre-production, production.

## Outcome

You must explain this flow from memory:

```text
Trade
→ Validation
→ Booking
→ Valuation
→ Position/P&L/Risk
→ Confirmation
→ Settlement
→ Accounting
→ Datamart
→ Reporting
→ Reconciliation
```

## Print checklist

```text
[ ] Murex overview
[ ] FO/MO/BO
[ ] Trade lifecycle
[ ] Trade/contract/event/cash flow
[ ] Book/portfolio/position
[ ] Counterparty/legal entity
[ ] Static data
[ ] Market data
[ ] Workflow
[ ] Datamart
[ ] MxML
[ ] Batch/EOD
[ ] Environments
```

# Phase 1: Functional Foundation

**Goal:** Become strong enough to understand a support ticket, report issue, trade issue, or integration issue in business terms.

## Capital-markets foundation

### FX

- FX spot.
- FX forward.
- FX swap.
- FX option basics.
- Currency pair.
- Buy/sell direction.
- Notional.
- Trade date.
- Value date.
- Forward rate.
- Settlement.

### Rates and fixed income

- Bonds.
- Coupon.
- Yield.
- Clean and dirty price.
- Accrued interest.
- Interest-rate swap.
- Fixed leg.
- Floating leg.
- Reset.
- Fixing.
- Day-count convention.
- Business-day convention.

### Other awareness

- Equity.
- Equity derivatives.
- Credit products.
- Commodity products.
- Repo/reverse repo.
- Securities lending.

## Trade lifecycle

- Trade capture.
- Manual booking.
- Interface booking.
- Trade validation.
- Enrichment.
- Booking.
- Amendment.
- Cancellation.
- Rebooking.
- Unwind.
- Partial termination.
- Novation.
- Confirmation.
- Affirmation.
- Settlement.
- Accounting.
- Reporting.
- Reconciliation.

## Static data

- Counterparty.
- Legal entity.
- Book.
- Portfolio.
- Trader.
- Organization hierarchy.
- Currency.
- Country.
- Calendar.
- Business center.
- Settlement instructions.
- Confirmation instructions.
- Nostro account.
- Netting agreement.
- Collateral agreement.
- User roles and access.

## Market data

- FX spot.
- Forward points.
- Yield curve.
- Discount curve.
- Forward curve.
- Volatility.
- Credit spread.
- Fixings.
- Market-data source.
- Timestamp.
- Missing data.
- Stale data.
- Market-data validation.

## Valuation and P&L

- Mark-to-market.
- Present value.
- Discounting.
- Cash flows.
- Pricing model awareness.
- Revaluation.
- Realized P&L.
- Unrealized P&L.
- Accruals.
- Valuation date.

## Workflow and MSL concepts

- Workflow state.
- Transition.
- Trigger.
- Event.
- Manual task.
- Automatic task.
- Pre-trade workflow.
- Post-trade workflow.
- Exception handling.
- Retry/reprocessing.
- MSL validation.
- MSL defaulting.
- MSL enrichment.
- MSL lookup.
- MSL routing.
- Date/calendar logic.
- Error/warning/manual-review decision.

## Phase-1 job readiness

You should be able to answer:

- What happens after a trade is booked?
- Static data vs market data?
- Why can a trade be rejected?
- Why can valuation be wrong?
- Why can a trade be missing from a report?
- Difference between workflow and MSL?
- Difference between book, portfolio, and position?

# Phase 2: Production Support L2/L3

**Goal:** This is your earliest job-entry route. Start applying once you complete this phase and can handle support scenarios verbally.

## L2/L3 operational concepts

### Service management

- Incident management.
- Problem management.
- Change management.
- Service request.
- SLA.
- Severity.
- Priority.
- Escalation.
- RCA.
- Workaround.
- Permanent fix.
- Knowledge article.
- Runbook.
- Post-incident review.

### Monitoring and logs

- Application logs.
- Interface logs.
- Workflow logs.
- Batch logs.
- Database logs.
- Error codes.
- Timestamps.
- Correlation IDs.
- Message IDs.
- Trace IDs.
- Health checks.
- Alerts.
- Dashboards.

### Linux/Unix support

- File system.
- Permissions.
- Process monitoring.
- Disk/memory/CPU checks.
- `grep`.
- `tail`.
- `less`.
- `find`.
- `awk`.
- `sed`.
- `sort`.
- `uniq`.
- `diff`.
- `ps`.
- `kill`.
- `df`.
- `du`.
- `chmod`.
- `cron` awareness.
- SFTP/file-transfer checks.

### Batch and scheduler support

- Batch.
- EOD.
- Intraday.
- Launcher.
- Scheduler.
- Job dependency.
- Predecessor.
- Successor.
- Sequential batch.
- Parallel batch.
- Job restart.
- Rerun.
- Partial failure.
- EOD cutoff.
- Business-date rollover.
- Control-M scheduling.
- SLA monitoring.

### Database and reconciliation support

- SQL queries.
- Joins.
- Aggregations.
- Missing records.
- Duplicate records.
- Status checks.
- Source-to-target reconciliation.
- Count reconciliation.
- Notional reconciliation.
- Currency-level reconciliation.
- Counterparty-level reconciliation.
- Data-quality validation.

## L2/L3 issue runbooks

Master these scenarios:

1. Trade not received from upstream.
2. Trade rejected at booking.
3. Trade stuck in workflow.
4. Trade booked but not in Datamart.
5. Trade in Datamart but missing from report.
6. Incorrect report total.
7. Batch/feeder failed.
8. EOD batch delayed.
9. Market data missing or stale.
10. Valuation differs unexpectedly.
11. Duplicate trade/interface message.
12. Settlement instruction missing.
13. Outbound confirmation not generated.
14. SFTP/MQ/API connection failure.
15. Database query slow or timed out.

## L2/L3 investigation framework

```text
Business impact
→ Ticket and timeline
→ Trade/message/report ID
→ Source status
→ Interface status
→ Workflow status
→ Trade status
→ Market/static data
→ Batch/feeder status
→ Datamart/report status
→ SQL reconciliation
→ Logs
→ Root cause
→ Workaround
→ Permanent fix
→ Documentation
```

## When to begin L2/L3 interviews

Start applying and interviewing for **Murex Production Support L2/L3, Reporting Support, or Risk Systems Support** when you can do all of the following:

- Explain an FX forward lifecycle end to end.
- Explain static versus market data.
- Read and filter a Linux log.
- Write SQL joins and reconciliation queries.
- Explain Control-M batch dependencies.
- Create an incident ticket update.
- Explain one missing-trade investigation.
- Explain one failed batch investigation.
- Write UAT test cases.
- Explain Murex Datamart at a basic level.
- Speak honestly: “I have production support experience in ETL/regulatory reporting; Murex exposure is structured training/practice until I get a live Murex project.”

**Practical readiness target:** 10–12 weeks of focused study plus documented case studies. Do not wait for total mastery; apply while progressing.

# Phase 3: Murex Datamart and Reporting

**Goal:** Your strongest development specialization because of your SQL, reporting, ETL, and reconciliation background.

## Datamart foundation

- Murex data model awareness.
- Trade data.
- Position data.
- Market value.
- Cash flows.
- Risk results.
- Counterparty data.
- Book/portfolio data.
- Static/market-data dependencies.
- Datamart purpose.
- Data lineage.
- Reporting lifecycle.

## Datamart objects

- Dynamic tables.
- Dynamic-table fields.
- Table joins.
- Filters.
- Pre-filters.
- Post-filters.
- Feeders.
- Batch feeders.
- Scanner templates.
- Extractions.
- Reporting tables.
- Processing scripts.
- Simulation views.
- Viewer reports.
- Risk-matrix reports.
- Simulation-based reports.
- Regulatory reports.
- Historization.
- Incremental loads.
- Full loads.
- Scheduling.

## Datamart workflow

```text
Trade
→ Valuation/risk result
→ Feeder
→ Dynamic/reporting table
→ Extraction/report
→ Downstream file/system
→ Reconciliation
```

## Datamart performance

- Efficient filters.
- Avoid redundant objects.
- Join design.
- Index awareness.
- Query performance.
- Batch duration.
- Incremental versus full loads.
- Execution-time monitoring.
- Redundant object analysis.
- Report-performance tuning.

## Datamart support scenarios

- Feeder failed.
- Batch feeder failed.
- Dynamic table has no data.
- Wrong report filter.
- Report duplicated records.
- Missing trades.
- Incorrect aggregation.
- Incorrect historic data.
- Extraction incomplete.
- Slow report.
- Source-to-report mismatch.

## Deliverables

1. Exposure report design.
2. Regulatory-report reconciliation document.
3. SQL reconciliation pack.
4. Feeder failure runbook.
5. Datamart performance checklist.

# Phase 4: MxML and Integration

**Goal:** Build from Datamart/support to Murex integration developer or techno-functional integration consultant.

## Message and interface foundation

- Inbound interface.
- Outbound interface.
- Real-time interface.
- Batch interface.
- File interface.
- API interface.
- Request-response.
- Asynchronous messaging.
- Message queue.
- Acknowledgement.
- Rejection.
- Retry.
- Reprocessing.
- Duplicate handling.
- Idempotency.
- Correlation ID.
- Error queue/dead-letter queue awareness.

## MxML

- MxML Exchange.
- Trade import.
- Trade export.
- Static-data import/export.
- Market-data messages.
- Confirmation messages.
- Settlement messages.
- Accounting messages.
- Regulatory-report messages.
- MxML templates.
- MxML formulas awareness.
- Message mapping.
- Message routing.
- Message monitoring.
- MxML error analysis.

## XML and transformation

- XML element.
- Attribute.
- Namespace.
- XSD.
- Data type.
- Mandatory field.
- Optional field.
- Repeating element.
- XPath.
- XSLT template.
- XSLT variable.
- XSLT condition.
- XSLT loop.
- Date transformation.
- Number transformation.
- XML validation.

## Integration architecture

```text
Source system
→ File/API/MQ/FIX
→ Transport channel
→ MxML Exchange
→ XML/XSD validation
→ Transformation/mapping
→ MSL/business validation
→ Murex workflow
→ Trade/static-data object
→ Acknowledgement
→ Downstream interface
→ Reconciliation
```

## Supporting technologies

- JSON.
- REST APIs.
- HTTP methods.
- Headers.
- Authentication.
- TLS certificates.
- SFTP.
- FIX awareness.
- FpML awareness.
- SWIFT awareness.
- MQ/JMS awareness.
- Kafka awareness.
- Middleware/ESB awareness.
- API logging.
- API timeouts.

## MxML support scenarios

- Invalid XML.
- XSD/schema error.
- Namespace error.
- Missing mandatory field.
- Mapping error.
- XSLT transformation error.
- Unknown counterparty/book.
- MSL validation rejection.
- Duplicate message.
- Interface timeout.
- Target system unavailable.
- Acknowledgement not received.
- Message stuck in queue.
- Wrong outbound mapping.

## Deliverables

1. FX inbound interface design.
2. Field-mapping document.
3. XML/XSD/XSLT practice pack.
4. MxML failure runbook.
5. UAT suite for inbound/outbound integration.
6. Source-target reconciliation design.

# Phase 5: Murex Techno-Functional

**Goal:** Become capable of translating business requirements into Murex configuration, integration, reporting, testing, and support tasks.

## Business-analysis skills

- Requirement gathering.
- Stakeholder management.
- As-is analysis.
- To-be process.
- Gap analysis.
- Functional specification.
- Technical specification.
- Mapping document.
- Data dictionary.
- Process diagram.
- User story.
- Acceptance criteria.
- Change impact analysis.
- Traceability matrix.

## Configuration awareness

- Product configuration.
- Static-data configuration.
- Market-data setup.
- Workflow setup.
- Business rules.
- MSL.
- Reports.
- Datamart objects.
- Interface configuration.
- Permissions.
- Batch setup.
- Environment configuration.
- Release/migration awareness.

## Testing and delivery

- Unit testing.
- SIT.
- UAT.
- Regression testing.
- Negative testing.
- Boundary testing.
- Integration testing.
- Batch testing.
- Performance testing awareness.
- Defect lifecycle.
- Severity/priority.
- Test evidence.
- Sign-off.
- Cutover.
- Hypercare.

## Advanced business domains

- Market risk.
- Sensitivities.
- VaR.
- Stress testing.
- P&L explain.
- Credit exposure.
- PFE/EPE.
- Netting.
- Collateral.
- Margin.
- CVA/DVA/FVA awareness.
- Accounting.
- Treasury.
- Liquidity.
- Regulatory reporting.
- Clearing.
- Securities finance awareness.

# Phase 6: Murex DevOps and Cloud

**Goal:** Become durable and future-ready. Add this after the support/Datamart/MxML core is functioning.

## DevOps core

- Git.
- Branching.
- Pull request.
- Code review.
- Release management.
- CI/CD.
- Build.
- Artifact.
- Deployment.
- Rollback.
- Environment promotion.
- Configuration versioning.
- Secret management.
- Monitoring.
- Alerting.
- Incident response.
- Infrastructure as Code.

## Tools and practices

- Git/GitHub/GitLab.
- Jenkins or GitHub Actions.
- Maven awareness.
- Docker.
- Container registry.
- Kubernetes awareness.
- Terraform.
- Ansible awareness.
- Jira.
- Confluence.
- ServiceNow awareness.
- SonarQube awareness.
- Dependency/image scanning.

## Cloud concepts

- AWS or GCP basics.
- IAM/service accounts.
- Virtual machines.
- Object storage.
- VPC/networking.
- Security groups/firewalls.
- Container services.
- Managed databases.
- Monitoring/logging.
- Secrets management.
- Cloud cost controls.
- High availability.
- Disaster recovery.

## Murex DevOps use cases

- Version-control MxML/XSLT/configuration packages.
- Automate promotion across DEV/SIT/UAT/PROD.
- CI checks for XML validity and XSLT transformation.
- Automated reconciliation tests.
- Containerized supporting integration services.
- Monitoring dashboards for interfaces and batches.
- Alerting for failed EOD/Datamart feeder runs.
- Automated log parsing and incident summaries.

Murex itself highlights continuous integration, production management, testing automation, managed services, cloud, and AI research across the capital-markets value chain.[4][5][6]

# Phase 7: AI Leverage for Murex

**Goal:** Use AI as a force multiplier, not as a substitute for understanding or access to confidential data.

## AI use cases you can do safely

### Learning and documentation

- Explain product concepts.
- Generate study notes.
- Create glossary flashcards.
- Convert requirements into draft test cases.
- Draft runbooks.
- Create process diagrams.
- Generate interview questions.
- Summarize public job descriptions.
- Compare two generic XML structures.
- Create generic SQL-practice tasks.

### Development and support

- Draft shell scripts using dummy data.
- Generate SQL skeletons for reconciliation.
- Generate Python scripts for log parsing.
- Explain errors from **sanitized** logs.
- Create regex patterns using non-sensitive examples.
- Draft RCA templates.
- Produce ticket-update drafts.
- Generate test-data ideas.
- Create XML/XSLT illustrative examples.
- Suggest monitoring metrics and alerts.

### AI-enhanced Murex operational ideas

- Log anomaly detection.
- Batch duration anomaly analysis.
- Reconciliation-break classification.
- Incident ticket summarization.
- Knowledge-base search.
- Root-cause suggestion from known patterns.
- Data-quality exception grouping.
- Test-case generation from requirements.

## AI safety rules

Never paste into a public AI tool:

- Client trade data.
- Counterparty names.
- Account numbers.
- Production logs with identifiers.
- Source code.
- Credentials.
- Certificates.
- Internal architecture.
- Regulatory reports.
- Confidential job or client documents.

Use redacted/synthetic examples only. Murex’s AI research work spans modelling, pricing, risk, operations, post-trade, and finance, but financial AI requires strong governance, security, validation, and human review.[5]

## AI skills to learn

- Prompt engineering for analysts.
- Python for automation.
- Pandas for CSV/report reconciliation.
- Regex for log analysis.
- API basics.
- LLM safety and privacy.
- Retrieval-Augmented Generation concepts.
- Vector-search awareness.
- Agent workflow awareness.
- Evaluation and hallucination checks.
- Human-in-the-loop review.
- AI audit trail awareness.

# Complete Syllabus Checklist

## Functional Core

```text
[ ] Capital markets
[ ] FX
[ ] Bonds
[ ] Interest-rate swaps
[ ] Trade lifecycle
[ ] Trade/contract/event/cash flow
[ ] Book/portfolio/position
[ ] Counterparty/legal entity
[ ] Static data
[ ] Market data
[ ] Pricing/valuation
[ ] P&L
[ ] Workflow
[ ] MSL concepts
[ ] Confirmation
[ ] Settlement
[ ] Accounting
[ ] Risk basics
[ ] Credit exposure basics
[ ] Collateral basics
[ ] Regulatory reporting
```

## Support Core

```text
[ ] Incident/problem/change
[ ] SLA/severity/priority
[ ] Logs and monitoring
[ ] Unix troubleshooting
[ ] SQL troubleshooting
[ ] Batch/EOD
[ ] Control-M
[ ] Reconciliation
[ ] RCA
[ ] Runbooks
[ ] Ticket communication
[ ] UAT/regression
```

## Datamart Core

```text
[ ] Murex data model awareness
[ ] Datamart
[ ] Dynamic tables
[ ] Filters
[ ] Feeders
[ ] Batch feeders
[ ] Scanner templates
[ ] Extractions
[ ] Reporting tables
[ ] Simulation views
[ ] Risk reports
[ ] Regulatory reports
[ ] Data lineage
[ ] Historization
[ ] Performance tuning
[ ] SQL reconciliation
```

## MxML Core

```text
[ ] MxML Exchange
[ ] Inbound/outbound
[ ] Trade/static/market-data interfaces
[ ] XML
[ ] XSD
[ ] XPath
[ ] XSLT
[ ] JSON
[ ] REST
[ ] SFTP
[ ] MQ/JMS
[ ] Mapping
[ ] Transformation
[ ] Validation
[ ] Acknowledgement
[ ] Retry
[ ] Idempotency
[ ] Monitoring
[ ] Interface reconciliation
```

## Techno-Functional Core

```text
[ ] Requirements
[ ] Functional specs
[ ] Technical specs
[ ] Mapping documents
[ ] Process mapping
[ ] Test strategy
[ ] SIT/UAT
[ ] Regression
[ ] Defects
[ ] Release/cutover
[ ] Stakeholder management
[ ] Production support
```

## DevOps/AI Core

```text
[ ] Git
[ ] CI/CD
[ ] Docker
[ ] Terraform
[ ] Cloud fundamentals
[ ] Monitoring/alerting
[ ] Security/secrets
[ ] Automation
[ ] Python
[ ] AI-safe support automation
[ ] AI-assisted documentation
[ ] AI-assisted reconciliation/log analysis
```

# The Exact Apply Strategy

## Start applying first

Start with **Production Support L2/L3, Datamart Reporting Support, Risk Reporting Support, and Technical Support Analyst** roles.

Your resume positioning:

> SQL/PLSQL, Linux Shell, Control-M, ETL, regulatory reporting, reconciliation, UAT, and production-support professional transitioning into Murex Datamart, reporting, integration, and techno-functional support.

## Apply next

Once you can explain Datamart objects, feeders, SQL reconciliation, MxML flows, XML/XSLT, and support scenarios:

- Murex Datamart Developer.
- Murex Reporting Consultant.
- Murex Regulatory Reporting Analyst.
- Murex MxML Support Analyst.
- Murex Integration Analyst.
- Murex Technical Business Analyst.

## Apply later

Once you have real Murex project exposure:

- Murex Integration Developer.
- Murex Techno-Functional Consultant.
- Murex Market Risk/MLC Support.
- Murex DevOps/Technical Services.
- Overseas Singapore/Dubai roles.

# Non-Negotiable Rules

1. **Do not wait until you know everything to start interviews.**
2. **Do not claim production Murex experience unless it is real.**
3. **Do not learn advanced Cloud/AI before core Murex support.**
4. **Learn one end-to-end use case deeply**: FX forward → MxML → workflow → Datamart → report → reconciliation → incident.
5. **Create evidence:** notes, mapping docs, SQL packs, UAT pack, runbooks, and case studies.
6. **Use AI carefully:** dummy/redacted data only, validate every output.
7. **Apply continuously once Phase 2 is complete.**

## Your first interview target

You can start interview preparation for Murex Production Support L2/L3 **after completing Phase 2**, not after the entire roadmap. That is the smart time-bound decision:

```text
Phase 0 + Phase 1 + Phase 2
= first interview readiness

Phase 3
= Datamart job readiness

Phase 4
= MxML integration readiness

Phase 5 + Phase 6 + Phase 7
= senior, durable, AI-enabled Murex career
```
# Murex Complete Syllabus — Phase-wise Learning Plan

This syllabus covers Murex MX.3 from basic orientation to advanced
Production Support, Datamart/Reporting, MxML Integration, Risk, and
Techno-Functional specialization.

The plan is designed for professionals with experience in SQL/PLSQL,
Linux/Shell, Control-M, ETL, reconciliation, regulatory reporting,
and UAT who want to move into Murex support and techno-functional roles.

---

# Complete Murex Syllabus

| Phase | Module No. | Chapter / Topic | Learning Objective | Level | Approx. Pages |
|---|---:|---|---|---|---:|
| Phase 0 | 0.1 | What is Murex MX.3? | Understand Murex purpose, users, modules, and business value | Basic | 5–6 |
| Phase 0 | 0.2 | Capital Markets and Bank Functions | Understand FO, MO, BO, Risk, Finance, Operations, Technology | Basic | 5–6 |
| Phase 0 | 0.3 | Murex MX.3 Architecture Overview | Understand presentation, business, orchestration, technical, data, integration layers | Basic | 6–8 |
| Phase 0 | 0.4 | Trade Lifecycle Overview | Understand trade to confirmation, settlement, accounting, reporting | Basic | 7–8 |
| Phase 0 | 0.5 | Core Murex Terminology | Learn trade, contract, event, cash flow, book, portfolio, position | Basic | 8–10 |
| Phase 0 | 0.6 | Environments, Access, and Audit | Understand DEV, SIT, UAT, PROD, access, audit, releases | Basic | 5–6 |
| Phase 0 | 0.7 | Murex User Roles and Responsibilities | Understand trader, operations, risk, finance, IT/support responsibilities | Basic | 4–6 |
| Phase 0 | 0.8 | Murex Support Ecosystem | Understand upstream/downstream systems, interfaces, batch, reporting | Basic | 5–7 |
| Phase 1 | 1.1 | Capital Markets Products | Understand FX, bonds, IRS, options, repo | Basic | 10–12 |
| Phase 1 | 1.2 | FX Forward Deep Dive | Master FX Forward terms, lifecycle, settlement, valuation | Basic | 10–12 |
| Phase 1 | 1.3 | FX Spot and FX Swap Basics | Understand currency pairs, spot, near/far legs, settlement | Basic | 6–8 |
| Phase 1 | 1.4 | Interest Rate Swap Basics | Understand fixed/floating legs, reset, fixing, valuation | Basic | 9–11 |
| Phase 1 | 1.5 | Bonds and Fixed Income Basics | Understand coupon, maturity, clean/dirty price, accrued interest | Basic | 7–9 |
| Phase 1 | 1.6 | Options Basics | Understand strike, expiry, premium, exercise, valuation inputs | Basic | 6–8 |
| Phase 1 | 1.7 | Trade, Contract, Event, Cash Flow | Understand core Murex business-object relationships | Basic | 8–10 |
| Phase 1 | 1.8 | Book, Portfolio, Position | Understand ownership, aggregation, P&L, reporting | Basic | 7–9 |
| Phase 1 | 1.9 | Counterparty and Legal Entity | Understand parties, hierarchy, agreements, exposure | Basic | 7–9 |
| Phase 1 | 1.10 | Static Data | Understand calendars, currencies, SSI, books, controls | Intermediate | 11–14 |
| Phase 1 | 1.11 | Market Data | Understand FX, curves, fixings, volatility, data quality | Intermediate | 11–14 |
| Phase 1 | 1.12 | Trade Capture, Validation, Enrichment | Understand booking, validation, defaulting, amendment | Intermediate | 10–12 |
| Phase 1 | 1.13 | Pricing, Valuation, and P&L | Understand MTM, PV, discounting, realized/unrealized P&L | Intermediate | 10–12 |
| Phase 1 | 1.14 | Workflow, Pre-Trade, Post-Trade | Understand states, transitions, exceptions, reprocessing | Intermediate | 9–11 |
| Phase 1 | 1.15 | MSL Business Rules | Understand validation, defaulting, lookup, routing, dates | Intermediate | 10–12 |
| Phase 1 | 1.16 | Confirmation, Settlement, Accounting | Understand confirmations, payments, SSI, accounting events | Intermediate | 9–11 |
| Phase 1 | 1.17 | Risk Basics for Murex | Understand market risk, credit risk, limits, exposure, VaR concepts | Intermediate | 8–10 |
| Phase 1 | 1.18 | Collateral and Margin Basics | Understand collateral agreements, margin calls, exposure | Intermediate | 6–8 |
| Phase 1 | 1.19 | Functional Testing and UAT | Understand SIT, UAT, test cases, defects, evidence | Intermediate | 10–12 |
| Phase 2 | 2.1 | L1, L2, L3 Support Model | Understand support roles, ownership, escalation | Intermediate | 6–8 |
| Phase 2 | 2.2 | Incident, Problem, Change Management | Understand SLA, severity, priority, RCA, workaround | Intermediate | 8–10 |
| Phase 2 | 2.3 | Murex Logs and Monitoring | Understand logs, message IDs, alerts, health checks | Intermediate | 8–10 |
| Phase 2 | 2.4 | Linux/Unix for Murex Support | Use logs, processes, permissions, files, commands | Intermediate | 10–12 |
| Phase 2 | 2.5 | Batch, EOD, and Control-M | Understand dependencies, reruns, restarts, EOD sequence | Intermediate | 10–12 |
| Phase 2 | 2.6 | SQL for Murex Support | Use joins, duplicate checks, missing records, reconciliation | Intermediate | 12–15 |
| Phase 2 | 2.7 | Reconciliation and Data Quality | Understand counts, notionals, breaks, exception reports | Intermediate | 10–12 |
| Phase 2 | 2.8 | Datamart/Reporting Lineage | Understand trade to feeder to Datamart to report | Intermediate | 10–12 |
| Phase 2 | 2.9 | Common Production Incidents | Investigate missing trade, failed batch, bad data, report breaks | Advanced | 12–15 |
| Phase 2 | 2.10 | RCA, Runbooks, Ticket Communication | Learn RCA, documentation, ticket updates, PIR | Advanced | 9–11 |
| Phase 2 | 2.11 | Support UAT and Regression | Validate fixes, controlled reruns, regression testing | Advanced | 8–10 |
| Phase 2 | 2.12 | L2/L3 Interview Preparation | Prepare support scenarios, answers, project stories | Advanced | 12–15 |
| Phase 3 | 3.1 | Murex Data Model Overview | Understand business objects, relationships, reference data, transactions | Advanced | 10–14 |
| Phase 3 | 3.2 | Murex Datamart Concepts | Understand reporting structures, feeders, extracts, aggregation | Advanced | 12–15 |
| Phase 3 | 3.3 | Datamart Feeders and Extracts | Understand feeder configuration, extract logic, scheduling | Advanced | 12–15 |
| Phase 3 | 3.4 | Reporting and BI Integration | Understand report generation, BI tools, downstream reporting | Advanced | 10–12 |
| Phase 3 | 3.5 | Regulatory Reporting Concepts | Understand regulatory data needs, controls, reconciliation, audit | Advanced | 10–12 |
| Phase 3 | 3.6 | Data Quality and Reconciliation Framework | Build data-quality checks, break analysis, exception handling | Advanced | 10–12 |
| Phase 3 | 3.7 | MxML Integration Overview | Understand MxML purpose, XML messages, integration patterns | Advanced | 10–12 |
| Phase 3 | 3.8 | MxML Message Flow | Understand inbound/outbound messages, mapping, enrichment, routing | Advanced | 12–15 |
| Phase 3 | 3.9 | MxML Mapping and Transformation | Understand field mapping, transformation, lookup, validation | Advanced | 12–15 |
| Phase 3 | 3.10 | MxML Error Handling and Reprocessing | Understand message failure, recovery, resubmission, audit | Advanced | 10–12 |
| Phase 3 | 3.11 | Murex Interfaces and Connectivity | Understand files, APIs, messaging, middleware, upstream/downstream systems | Advanced | 10–12 |
| Phase 3 | 3.12 | Murex Batch and Job Orchestration | Understand complex dependencies, parallel jobs, restart strategy | Advanced | 10–12 |
| Phase 3 | 3.13 | Murex Performance and Capacity Basics | Understand slow reports, batch performance, data volume, tuning awareness | Advanced | 8–10 |
| Phase 3 | 3.14 | Murex Security and Access Control | Understand roles, permissions, segregation of duties, audit | Advanced | 8–10 |
| Phase 3 | 3.15 | Murex Release and Deployment Support | Understand releases, configuration promotion, rollback, regression | Advanced | 8–10 |
| Phase 4 | 4.1 | Advanced Trade Lifecycle Scenarios | Handle amendments, cancellations, novations, backdating, corrections | Advanced | 10–12 |
| Phase 4 | 4.2 | Advanced Valuation and P&L Scenarios | Investigate valuation differences, curve impact, P&L attribution | Advanced | 10–12 |
| Phase 4 | 4.3 | Advanced Risk and Limit Scenarios | Investigate exposure, limit breaches, risk data issues | Advanced | 10–12 |
| Phase 4 | 4.4 | Advanced Collateral Scenarios | Investigate collateral calls, eligibility, margin, exposure mismatch | Advanced | 8–10 |
| Phase 4 | 4.5 | Advanced Datamart Reporting Scenarios | Investigate missing data, wrong totals, duplicates, late data | Advanced | 12–15 |
| Phase 4 | 4.6 | Advanced MxML Integration Scenarios | Investigate schema, mapping, enrichment, routing, acknowledgement failures | Advanced | 12–15 |
| Phase 4 | 4.7 | Advanced EOD and Batch Failure Scenarios | Handle partial failures, dependency breaks, rerun strategy | Advanced | 10–12 |
| Phase 4 | 4.8 | Advanced Reconciliation Scenarios | Investigate source vs Murex vs report vs downstream differences | Advanced | 10–12 |
| Phase 4 | 4.9 | Advanced UAT and Regression Strategy | Design end-to-end regression and release validation | Advanced | 8–10 |
| Phase 4 | 4.10 | Advanced RCA and Problem Management | Perform deep RCA, trend analysis, prevention, knowledge base creation | Advanced | 10–12 |
| Phase 4 | 4.11 | Techno-Functional Consulting Skills | Translate business requirements into technical solutions | Advanced | 8–10 |
| Phase 4 | 4.12 | Murex Interview Mastery | Prepare senior support, Datamart, MxML, techno-functional interviews | Advanced | 15–20 |

---

# Phase-wise Learning Goals

| Phase | Goal | Expected Outcome |
|---|---|---|
| Phase 0 | Orientation | Explain Murex ecosystem, architecture, lifecycle, and terminology |
| Phase 1 | Functional Foundation | Explain trade lifecycle, products, static/market data, workflow, UAT |
| Phase 2 | Production Support L2/L3 | Investigate incidents, batches, logs, SQL, reconciliation, reports |
| Phase 3 | Advanced Technical Specialization | Work on Datamart, MxML, interfaces, data quality, performance |
| Phase 4 | Advanced Scenario Mastery | Handle complex production issues and techno-functional requirements |

---

# Suggested Learning Timeline

| Phase | Duration | Focus |
|---|---:|---|
| Phase 0 | 1–2 weeks | Orientation and foundation |
| Phase 1 | 4–6 weeks | Functional and business knowledge |
| Phase 2 | 4–5 weeks | Support readiness and interview preparation |
| Phase 3 | 6–8 weeks | Datamart, MxML, integration, advanced support |
| Phase 4 | Ongoing | Advanced scenarios, RCA, consulting, interview mastery |

---

# Recommended Study Sequence

```text
Phase 0: Orientation
↓
Phase 1: Functional Foundation
↓
Phase 2: Production Support L2/L3
↓
Phase 3: Datamart, MxML, Integration
↓
Phase 4: Advanced Scenarios and Techno-Functional Mastery
Your current stack is not a weakness—it is exactly the support/data/automation foundation from which a Murex techno-functional career can be built.

Citations:
[1] Application Support Engineer - Accenture https://www.accenture.com/gr-en/careers/jobdetails?id=ATCI-5453645-S1986380_en
[2] Murex Datamart Developer & Production Support Specialist https://www.professionalpyramid.com/jobs/welstu7p2p2ug396lwnpdbaw
[3] Murex MxML Developer Job Chennai | Career at DXC Luxoft https://career.luxoft.com/jobs/murex-mxml-developer-26656
[4] About us - Murex https://www.murex.com/en/who-we-are/about-us
[5] Murex AI Research Artificial Intelligence MX.3 https://www.murex.com/en/news/murex-ai-research-launches-shape-explore-evolution-artificial-intelligence-capital-markets
[6] MX.3 is a Prime SaaS, Cloud Capital Markets Platform - Murex https://www.murex.com/en/insights/video/cloud-and-saas-mx3
[7] Murex Support Jobs in India (97 Open Roles) - LinkedIn https://in.linkedin.com/jobs/murex-support-jobs
[8] 18 Murex Datamart Jobs and Vacancies - 8 October 2026 | Indeed https://in.indeed.com/q-murex-datamart-l-anywhere-jobs.html
[9] How AI and Digital Banking Are Increasing the Demand for Murex ... https://www.multisoftsystems.com/blog/how-ai-and-digital-banking-are-increasing-the-demand-for-murex-professionals
[10] How AI and Automation are Revolutionizing Murex - LinkedIn https://www.linkedin.com/posts/subrato-gupta-285bab48_murex-ai-automation-activity-7305879763259150339-kNlA
