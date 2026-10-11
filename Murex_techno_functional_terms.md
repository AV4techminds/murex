
# Murex Techno-Functional Glossary

This glossary covers the core terminology needed for Murex Functional, Techno-Functional,
Production Support, Datamart, and MXML Integration roles.

## 1. Murex Platform

| Term | Meaning |
|---|---|
| **Murex** | A financial-technology company that provides capital-markets and treasury software. |
| **MX.3** | Murex’s integrated capital-markets platform used for trading, risk, treasury, operations, and finance. |
| **MXJ** | Murex Java-based integration/technical layer used for custom development and integrations. |
| **MSL** | Murex Scripting Language, used for business rules, calculations, workflows, and customizations. |
| **MXML** | Murex XML-based message/data format used to exchange data between MX.3 and external systems. |
| **Datamart** | Reporting/data layer in MX.3 used for analytics, dashboards, risk, P&L, and regulatory reporting. |
| **Murex Desktop** | Traditional Murex user interface used by traders, operations, risk, and support teams. |
| **MXJ Web** | Web-based Murex user interface. |
| **Murex MCP** | Murex Command/Control or platform-management capability used for environment, deployment, and operational administration. |

MX.3 APIs expose the trade lifecycle—from pricing and booking to risk analytics and settlement—through a REST API layer. [173]

## 2. Capital Markets Basics

| Term | Meaning |
|---|---|
| **Capital Markets** | Markets where financial instruments such as equities, bonds, currencies, and derivatives are traded. |
| **Buy-side** | Firms that invest money, such as asset managers, pension funds, and hedge funds. |
| **Sell-side** | Firms that provide trading, research, and market-making services, such as investment banks. |
| **Trading Desk** | Team that executes and manages trades for a product or asset class. |
| **Front Office (FO)** | Team that prices, books, executes, and manages client/trading activity. |
| **Middle Office (MO)** | Team that validates trades, monitors risk, calculates P&L, and manages workflows. |
| **Back Office (BO)** | Team that handles confirmation, settlement, payments, reconciliation, and accounting. |
| **Counterparty** | The other party in a financial transaction. |
| **Legal Entity** | A legally recognized organization, such as a bank, fund, or company. |
| **Book** | A logical grouping used to track trades, positions, P&L, and risk. |
| **Portfolio** | A collection of trades/positions managed together. |
| **Position** | Net holding or exposure in an instrument or portfolio. |
| **Asset Class** | Category of financial product, such as FX, equity, fixed income, credit, or commodity. |
| **Instrument** | A tradable financial product, such as an FX forward, bond, swap, or option. |
| **Trade** | A financial transaction between two parties. |
| **Trade Lifecycle** | The complete journey of a trade from execution to settlement, accounting, and reporting. |

## 3. Financial Products

| Term | Meaning |
|---|---|
| **FX Spot** | Agreement to exchange two currencies at the current market rate, usually settled within two business days. |
| **FX Forward** | Agreement to exchange currencies at a fixed rate on a future date. |
| **FX Swap** | Combination of spot and forward FX transactions. |
| **Equity** | Ownership interest in a company, commonly called a share or stock. |
| **Bond** | Debt instrument where the issuer borrows money from investors and pays interest. |
| **Fixed Income** | Investments that provide periodic interest payments, such as bonds. |
| **Interest Rate Swap (IRS)** | Agreement to exchange fixed and floating interest-rate payments. |
| **Credit Default Swap (CDS)** | Contract that protects against a borrower’s default risk. |
| **Option** | Right, but not obligation, to buy or sell an underlying asset at a fixed price. |
| **Future** | Standardized contract to buy/sell an asset at a future date. |
| **Forward** | Customized agreement to buy/sell an asset at a future date. |
| **Derivative** | Financial contract whose value depends on an underlying asset, rate, or index. |
| **Underlying** | Asset, rate, index, or security on which a derivative is based. |
| **Commodity** | Physical or financial product such as oil, gas, gold, or power. |
| **Structured Product** | Complex financial product built using derivatives and custom payoff rules. |

## 4. Trade Lifecycle

| Term | Meaning |
|---|---|
| **Trade Execution** | Agreement between buyer and seller to transact. |
| **Trade Capture / Booking** | Entering trade details into Murex. |
| **Trade Enrichment** | Adding required data such as counterparty, settlement details, and market data. |
| **Trade Validation** | Checking whether a trade meets business and system rules. |
| **Trade Amendment** | Modifying an existing trade. |
| **Trade Cancellation** | Cancelling a trade before it completes its lifecycle. |
| **Trade Reversal** | Reversing the accounting or business effect of a trade/event. |
| **Novation** | Replacing one counterparty with another in an existing trade. |
| **Trade Termination** | Ending a trade before its original maturity date. |
| **Trade Closure** | Final completion of a trade lifecycle. |
| **Backloading** | Entering historical or already-executed trades into the system. |
| **Trade Status** | Current stage of a trade, such as captured, validated, confirmed, settled, or cancelled. |

## 5. Market and Reference Data

| Term | Meaning |
|---|---|
| **Market Data** | Real-time or historical market information used for pricing and valuation. |
| **Reference Data** | Master data used to identify and process trades. |
| **Static Data** | Relatively stable master data, such as counterparty, legal entity, currency, and instrument details. |
| **Price** | Market value of an instrument at a given time. |
| **Quote** | Bid/ask price provided by a market participant. |
| **Bid** | Price at which a buyer is willing to buy. |
| **Ask / Offer** | Price at which a seller is willing to sell. |
| **Spread** | Difference between bid and ask price. |
| **Yield Curve** | Relationship between interest rates and maturities. |
| **Volatility** | Measure of price movement or uncertainty. |
| **Volatility Surface** | Set of implied volatilities across strikes and maturities. |
| **Fixing** | Official rate published at a specific time, often used for FX or interest-rate settlements. |
| **Corporate Action** | Event affecting a security, such as dividend, split, merger, or rights issue. |
| **Market Data Snapshot** | Saved set of market data used for valuation or historical analysis. |
| **Pricing Curve** | Set of market-data points used to value instruments. |

## 6. Risk and P&L

| Term | Meaning |
|---|---|
| **Risk** | Possibility of financial loss due to market, credit, operational, or liquidity factors. |
| **Market Risk** | Risk of loss due to changes in market prices, rates, FX, or volatility. |
| **Credit Risk** | Risk that a counterparty fails to meet its obligations. |
| **Counterparty Credit Risk** | Risk that a trading counterparty defaults before settlement. |
| **Exposure** | Amount at risk with a counterparty or in a position. |
| **Limit** | Maximum permitted risk, exposure, or trading amount. |
| **Limit Breach** | Situation where exposure exceeds an approved limit. |
| **VaR** | Value at Risk; estimated potential loss over a given time period at a confidence level. |
| **Sensitivity** | Change in portfolio value due to a change in a risk factor. |
| **Greeks** | Sensitivities of option value to factors such as delta, gamma, vega, and theta. |
| **Stress Testing** | Testing portfolio impact under extreme market scenarios. |
| **Scenario Analysis** | Evaluating P&L or risk under hypothetical market conditions. |
| **P&L** | Profit and Loss. |
| **Realized P&L** | Profit/loss from completed or closed trades. |
| **Unrealized P&L** | Profit/loss from open positions based on current valuation. |
| **Valuation** | Process of calculating the current value of a trade or portfolio. |
| **Mark-to-Market** | Valuing a position using current market prices. |
| **Fair Value** | Estimated value of an asset or liability under market conditions. |
| **Accrual** | Income or expense recognized over time rather than only at settlement. |
| **XVA** | Family of valuation adjustments, including CVA, DVA, FVA, and MVA. |
| **CVA** | Credit Valuation Adjustment; adjustment for counterparty default risk. |
| **DVA** | Debit Valuation Adjustment; adjustment for own default risk. |
| **FVA** | Funding Valuation Adjustment. |
| **Collateral** | Asset pledged to reduce credit risk. |
| **Margin** | Collateral posted to cover potential future exposure. |
| **Initial Margin** | Collateral posted at trade inception to cover potential future exposure. |
| **Variation Margin** | Collateral exchanged to cover changes in current exposure. |

## 7. Middle Office and Workflows

| Term | Meaning |
|---|---|
| **Workflow** | Controlled sequence of steps for processing a trade or event. |
| **Workflow Status** | Current stage of a trade, such as pending, validated, rejected, or completed. |
| **Task** | Action assigned to a user or team in a workflow. |
| **Exception** | Trade or event that failed validation or requires manual attention. |
| **Exception Queue** | List of failed or pending items requiring investigation. |
| **Trade Validation** | Checking trade data against business, market, and regulatory rules. |
| **Enrichment** | Adding missing required information to a trade. |
| **Approval** | Authorization required before a trade or event can proceed. |
| **STP** | Straight-Through Processing; automated processing without manual intervention. |
| **Break** | Mismatch between expected and actual data, cash, position, or settlement. |
| **Compliance** | Adherence to internal policies and external regulations. |
| **Regulatory Reporting** | Sending required trade/risk data to regulators. |
| **Pre-Trade Check** | Checks performed before executing a trade, such as limits or compliance. |
| **Post-Trade Check** | Checks performed after execution, such as validation and settlement checks. |

## 8. Back Office, Settlement, and Accounting

| Term | Meaning |
|---|---|
| **Confirmation** | Agreement between counterparties on trade details. |
| **Affirmation** | Institutional investor’s agreement to trade details before settlement. |
| **Matching** | Comparing trade details between counterparties or systems. |
| **Settlement** | Exchange of cash and/or securities between parties. |
| **Settlement Date** | Date on which cash or securities are exchanged. |
| **Settlement Instruction** | Instruction describing how a payment or security transfer should occur. |
| **Settlement Status** | Current state of a settlement, such as pending, released, settled, or failed. |
| **Cash Settlement** | Settlement involving money transfer. |
| **Securities Settlement** | Transfer of securities between parties. |
| **Payment** | Transfer of money between accounts or entities. |
| **Payment Message** | Structured message used to initiate or process a payment. |
| **SWIFT** | Global messaging network used for financial transactions and payments. |
| **Nostro Account** | Bank’s account held with another bank in a foreign currency. |
| **Vostro Account** | Account held by a bank on behalf of a foreign bank. |
| **Reconciliation** | Comparing two sets of records to identify mismatches. |
| **Break** | Mismatch found during reconciliation. |
| **Cash Flow** | Expected or actual movement of cash. |
| **Accounting Event** | Business event that generates accounting entries. |
| **Accounting Entry** | Debit/credit record created for an accounting event. |
| **General Ledger (GL)** | Central accounting record of financial transactions. |
| **Sub-Ledger** | Detailed accounting records supporting the general ledger. |
| **Multi-GAAP** | Ability to produce accounting results under multiple accounting standards. |
| **IFRS** | International Financial Reporting Standards. |
| **Hedge Accounting** | Accounting treatment used to align hedging instruments with hedged risks. |

## 9. Treasury

| Term | Meaning |
|---|---|
| **Treasury** | Function managing cash, liquidity, funding, investments, and financial risk. |
| **Liquidity** | Availability of cash or assets that can be converted into cash. |
| **Liquidity Risk** | Risk of not having enough cash to meet obligations. |
| **Funding** | Obtaining cash or capital to support business activities. |
| **Funding Requirement** | Cash needed to support positions, settlements, or operations. |
| **Cash Flow Forecast** | Estimate of future cash inflows and outflows. |
| **Cash Management** | Monitoring and controlling cash balances and payments. |
| **Banking Book** | Portfolio of assets/liabilities held for banking rather than trading purposes. |
| **Trading Book** | Portfolio of instruments held for trading purposes. |
| **Hedge** | Transaction used to reduce risk from another exposure. |
| **Hedged Item** | Exposure being protected by a hedge. |
| **Hedging Instrument** | Trade used to reduce risk of the hedged item. |

## 10. MXML and Integration

| Term | Meaning |
|---|---|
| **Integration** | Connecting MX.3 with external systems to exchange data or trigger processes. |
| **External System** | Any system outside MX.3, such as a payment system, market-data provider, GL, or regulator. |
| **Upstream System** | System that sends data into MX.3. |
| **Downstream System** | System that receives data from MX.3. |
| **Interface** | Defined connection through which systems exchange data. |
| **Inbound Interface** | Interface that brings data into MX.3. |
| **Outbound Interface** | Interface that sends data from MX.3 to another system. |
| **MXML Message** | XML-based message used to exchange business data with MX.3. |
| **MXML Schema** | Structure/rules defining valid MXML message content. |
| **Field Mapping** | Mapping a source-system field to a target-system field. |
| **Transformation** | Converting data from one format or structure to another. |
| **Message Validation** | Checking whether a message meets required structure and business rules. |
| **Rejection** | Message or event that failed validation and cannot proceed. |
| **Exception Handling** | Process of identifying, logging, correcting, and reprocessing failed messages. |
| **Reprocessing** | Sending a corrected failed message again. |
| **Acknowledgement** | Confirmation that a message was received or processed. |
| **API** | Application Programming Interface; allows systems to communicate programmatically. |
| **REST API** | API style using HTTP methods such as GET, POST, PUT, and DELETE. |
| **JSON** | Lightweight data format commonly used in APIs. |
| **XML** | Structured markup format commonly used for MXML messages. |
| **Queue** | Storage area where messages wait for processing. |
| **Message Queue** | System that holds and delivers messages between applications. |
| **Kafka** | Distributed event-streaming platform often used for high-volume integration. |
| **MQ** | Message Queue middleware used for reliable system-to-system messaging. |
| **SFTP** | Secure File Transfer Protocol, often used for file-based interfaces. |
| **Batch Interface** | Interface that processes data in scheduled groups rather than real time. |
| **Real-Time Interface** | Interface that processes messages immediately as they arrive. |

MX.3 APIs provide secure, real-time access to trading, risk, and post-trade capabilities across the trade lifecycle. [173]

## 11. Datamart and Reporting

| Term | Meaning |
|---|---|
| **Datamart** | Reporting/data layer that stores and organizes data for analysis and reporting. |
| **Data Feed** | Data sent from a source system into the Datamart. |
| **ETL** | Extract, Transform, Load; process of moving and preparing data for reporting. |
| **Extract** | Reading data from a source system. |
| **Transform** | Cleaning, converting, or mapping data into the required format. |
| **Load** | Writing processed data into a target table or reporting system. |
| **Fact Table** | Table containing measurable business events, such as trades or cash flows. |
| **Dimension Table** | Table containing descriptive attributes, such as counterparty, currency, or product. |
| **Report** | Structured output showing business or risk information. |
| **Dashboard** | Visual interface showing KPIs, exposures, P&L, or operational metrics. |
| **KPI** | Key Performance Indicator. |
| **Data Quality Check** | Validation to ensure data is complete, accurate, and consistent. |
| **Data Reconciliation** | Comparing source and target data to identify differences. |
| **Report Failure** | Situation where a report does not generate, contains incorrect data, or misses expected records. |
| **Regulatory Report** | Report submitted to a regulator to meet legal requirements. |
| **Management Report** | Internal report used by management for decision-making. |

## 12. EOD, Batch, and Scheduling

| Term | Meaning |
|---|---|
| **EOD** | End of Day; daily batch process for valuation, risk, P&L, accounting, and reporting. |
| **SOD** | Start of Day; beginning-of-day processes and checks. |
| **Batch Job** | Scheduled task that processes data or performs a business function. |
| **Batch Window** | Time period allocated for nightly batch processing. |
| **Job Dependency** | Condition where one job must complete before another starts. |
| **Job Failure** | Batch job that did not complete successfully. |
| **Job Restart** | Restarting a failed job from a defined point. |
| **Job Rerun** | Running a job again after correction or failure. |
| **Scheduler** | Tool used to schedule and monitor batch jobs, such as Control-M, Autosys, or Tidal. |
| **Control-M** | Enterprise workload automation/scheduling tool. |
| **Cron** | Unix/Linux time-based job scheduler. |
| **Dependency** | Condition that must be satisfied before a job can run. |
| **Critical Job** | Job whose failure impacts business-critical processing. |
| **SLA** | Service Level Agreement; agreed response or resolution time. |

## 13. Production Support and ITIL

| Term | Meaning |
|---|---|
| **Production Support** | Monitoring, troubleshooting, and resolving issues in live systems. |
| **Incident** | Unplanned interruption or reduction in quality of an IT service. |
| **Incident Management** | Process to restore normal service as quickly as possible. |
| **Problem** | Underlying cause of one or more incidents. |
| **Problem Management** | Finding and removing the root cause of recurring incidents. |
| **Root Cause Analysis (RCA)** | Investigation to identify why an issue occurred. |
| **Known Error** | Problem with a documented workaround or permanent fix. |
| **Change** | Modification to a system, configuration, code, or infrastructure. |
| **Change Management** | Controlled process for approving and deploying changes. |
| **Change Request (CR)** | Formal request to make a change. |
| **Rollback** | Returning a system to its previous stable state. |
| **Deployment** | Moving code/configuration into an environment. |
| **Release** | Set of changes deployed together. |
| **Environment** | System setup used for development, testing, or production. |
| **DEV** | Development environment. |
| **SIT** | System Integration Testing environment. |
| **UAT** | User Acceptance Testing environment. |
| **PROD** | Production/live environment. |
| **Priority** | Urgency of an incident, often P1 to P4. |
| **Severity** | Business/technical impact of an incident. |
| **P1 Incident** | Critical incident with major business impact. |
| **Escalation** | Raising an issue to a higher support level or management. |
| **L1 Support** | First-line support; initial triage and basic troubleshooting. |
| **L2 Support** | Second-line support; deeper technical investigation. |
| **L3 Support** | Specialist support; complex/root-cause resolution. |
| **Runbook** | Step-by-step operational guide for handling a known task or issue. |
| **Monitoring** | Observing system health, jobs, logs, and performance. |
| **Alert** | Notification triggered by a monitoring condition. |
| **Log** | System-generated record of events, errors, and processing activity. |
| **Log Analysis** | Reviewing logs to identify errors and root causes. |
| **Performance Tuning** | Improving system or query performance. |
| **Root Cause** | Fundamental reason an issue occurred. |
| **Workaround** | Temporary solution that restores service before a permanent fix. |
| **Permanent Fix** | Solution that removes the root cause. |
| **Continual Improvement** | Ongoing process of improving services and support quality. |

## 14. SQL and Data Terms

| Term | Meaning |
|---|---|
| **Database** | Organized storage for structured data. |
| **Schema** | Logical grouping of database objects. |
| **Table** | Structured storage of rows and columns. |
| **Row / Record** | One data entry in a table. |
| **Column / Field** | Attribute of a record. |
| **Primary Key** | Unique identifier for a table row. |
| **Foreign Key** | Column linking one table to another. |
| **Join** | Combining data from multiple tables. |
| **Inner Join** | Returns only matching records. |
| **Left Join** | Returns all records from the left table and matching records from the right. |
| **Index** | Database structure used to speed up data retrieval. |
| **Query** | SQL statement used to retrieve or manipulate data. |
| **Execution Plan** | Database’s plan for executing a SQL query. |
| **Query Performance Tuning** | Improving SQL query speed and resource usage. |
| **Data Reconciliation** | Comparing datasets to identify missing, duplicate, or mismatched records. |
| **Data Quality** | Accuracy, completeness, consistency, and validity of data. |
| **Duplicate Record** | Same business record appearing more than once. |
| **Missing Record** | Expected record not present in target data. |
| **Data Mismatch** | Same record exists but values differ between systems. |

## 15. DevOps and Cloud Terms

| Term | Meaning |
|---|---|
| **DevOps** | Practice combining development and operations to deliver software faster and reliably. |
| **CI** | Continuous Integration; automatically building and testing code changes. |
| **CD** | Continuous Delivery/Deployment; automating release of validated changes. |
| **Pipeline** | Automated sequence of build, test, and deployment steps. |
| **Git** | Distributed version-control system. |
| **GitHub** | Cloud platform for Git repositories and collaboration. |
| **Branch** | Separate line of development in Git. |
| **Merge Request / Pull Request** | Request to merge code changes into another branch. |
| **Docker** | Platform for building and running containers. |
| **Container** | Lightweight package containing an application and its dependencies. |
| **Image** | Template used to create a container. |
| **Kubernetes** | Platform for deploying, scaling, and managing containers. |
| **Terraform** | Infrastructure-as-Code tool used to provision cloud resources. |
| **IaC** | Infrastructure as Code. |
| **AWS** | Amazon Web Services cloud platform. |
| **EC2** | AWS virtual server service. |
| **S3** | AWS object-storage service. |
| **RDS** | AWS managed relational database service. |
| **IAM** | AWS identity and access-management service. |
| **VPC** | Virtual Private Cloud; isolated cloud network. |
| **CloudWatch** | AWS monitoring and observability service. |
| **Observability** | Ability to understand system health through logs, metrics, and traces. |

## 16. AI Terms

| Term | Meaning |
|---|---|
| **AI** | Artificial Intelligence; systems that perform tasks requiring human-like intelligence. |
| **ML** | Machine Learning; systems that learn patterns from data. |
| **LLM** | Large Language Model; AI model trained to understand and generate text. |
| **Prompt** | Instruction given to an AI model. |
| **Prompt Engineering** | Designing effective instructions for AI models. |
| **Generative AI** | AI that creates text, code, images, or other content. |
| **RAG** | Retrieval-Augmented Generation; AI answers questions using retrieved documents. |
| **Embedding** | Numerical representation of text used for search and similarity. |
| **Vector Database** | Database used to store and search embeddings. |
| **AI Agent** | AI system that can use tools and perform multi-step tasks. |
| **Hallucination** | Incorrect or fabricated AI-generated information. |
| **Human-in-the-Loop** | Human review/approval before AI-driven action is executed. |

## 17. Interview Quick Answers

**What is Murex?**  
Murex is a financial-technology company, and MX.3 is its integrated capital-markets platform used for trading, risk, treasury, operations, and finance.

**What is MXML?**  
MXML is Murex’s XML-based data/message format used to exchange information between MX.3 and external systems.

**What is Datamart?**  
Datamart is MX.3’s reporting and analytics layer used for risk, P&L, valuation, accounting, regulatory, and management reporting.

**What is the difference between incident and problem?**  
An incident is an issue affecting service that must be restored quickly. A problem is the underlying cause that must be investigated to prevent recurrence.

**What is RCA?**  
RCA means Root Cause Analysis. It identifies the fundamental reason an issue occurred and helps prevent it from recurring.

**What is EOD?**  
EOD means End of Day. It is the nightly batch process for valuation, risk, P&L, accounting, reporting, and other daily business activities.

**What is STP?**  
STP means Straight-Through Processing. It automates trade processing with minimal manual intervention.

**What is reconciliation?**  
Reconciliation compares two data sets to identify missing, duplicate, or mismatched records.

**What is an inbound interface?**  
An inbound interface receives data from an external system into MX.3.

**What is an outbound interface?**  
An outbound interface sends data from MX.3 to an external system.

## 18. Daily Revision Checklist

- [ ] Explain trade lifecycle end-to-end  
- [ ] Explain FO, MO, BO differences  
- [ ] Explain market data vs reference data  
- [ ] Explain MXML inbound and outbound flow  
- [ ] Explain Datamart architecture and reporting flow  
- [ ] Explain EOD batch flow  
- [ ] Explain incident, problem, change, RCA, SLA  
- [ ] Explain SQL reconciliation approach  
- [ ] Explain Python/API automation use case  
- [ ] Explain DevOps/Cloud role in Murex environment  
```

## How to use it

- Read **10–15 terms per day**; do not try to memorize all at once.
- For every term, write one real Murex example in your own words.
- Tag each term as `Basic`, `Medium`, or `Advanced`.
- Use this glossary before Murex interviews and while doing RCA.
- Keep it in GitHub and update it whenever you learn a new term.

This glossary covers the terminology across Murex functional, trade lifecycle, risk/P&L, settlement/accounting, MXML, Datamart, SQL, DevOps, cloud, AI, and production support—matching the skills you want to build. Murex APIs, for example, expose the full trade lifecycle from pricing and booking through risk analytics and settlement, so these terms connect directly to real MX.3 workflows.[1][2][3]

Citations:
[1] www.murex.com › en › mx3-apisMX.3 next-generation APIs accelerate innovation | Murex https://www.murex.com/en/mx3-apis
[2] www.murex.com › en › securities-finance-andSecurities Finance Solution | Murex https://www.murex.com/en/securities-finance-and-collateral-management
[3] www.multisoftsystems.com › img › course_content_PDFMurex (MX.3) Training Mur - multisoftsystems.com https://www.multisoftsystems.com/img/course_content_PDF/Murex%20(MX.3)%20-%20MS%20Course%20Content.pdf
[4] github.com › AV4techminds › murexmurex/learning/Murex/README.md at main · AV4techminds/murex https://github.com/AV4techminds/murex/blob/main/learning/Murex/README.md
[5] www.linkedin.com › posts › kishoremamilla_murex-mx3#murex #mx3 #murexba #businessanalyst #capitalmarkets # ... https://www.linkedin.com/posts/kishoremamilla_murex-mx3-murexba-activity-7496023278973702144-J9bE
[6] www.linkedin.com › pulse › murex-apis-poweringMurex APIs: Powering Digital Back-Office Operations in ... https://www.linkedin.com/pulse/murex-apis-powering-digital-back-office-operations-kumar-mba-0a5uc
[7] ascenteum.org › a-complete-guide-to-murex-mx-3A Complete Guide to Murex MX.3 Implementation for Investment ... https://ascenteum.org/a-complete-guide-to-murex-mx-3-implementation-for-investment-banks/
[8] valkeris.com › murexMurex Transformation – VALKERIS https://valkeris.com/murex/
Add production support troubleshooting terms

Avunu—nee glossary lo idi **Section 19: Production Support & Troubleshooting Terms** ga add cheyyi. Idi Murex Production Support, Datamart Support, MXML Integration Support, and Technical Services interviews kosam chala important.

```markdown
# 19. Production Support & Troubleshooting Glossary

This section covers the terms used in Murex Production Support, application support,
incident management, troubleshooting, RCA, monitoring, and operational support.

## 19.1 Incident Management Terms

| Term | Meaning | Murex Example |
|---|---|---|
| **Incident** | Unplanned interruption or degradation of an IT service. | Murex EOD job failed, so risk/P&L reports are not generated. |
| **Incident Management** | Process to restore normal service as quickly as possible. | Investigate failed EOD job and restart it after validation. |
| **Incident Ticket** | Formal record of an issue, its impact, actions, and resolution. | INC123456 created for failed Datamart report. |
| **Incident Triage** | Initial assessment of issue, impact, urgency, and correct support team. | Check whether issue is Murex, database, network, scheduler, or downstream system. |
| **Incident Categorization** | Classifying issue by type, such as batch, interface, database, or application. | Categorize issue as “Murex Datamart Batch Failure.” |
| **Incident Prioritization** | Deciding how urgently an issue must be handled. | P1 for EOD failure affecting regulatory reporting. |
| **Impact** | Extent of business disruption or number of users/processes affected. | Multiple regions cannot receive risk reports. |
| **Urgency** | How quickly the issue must be resolved. | Issue must be fixed before regulatory submission deadline. |
| **Priority** | Combined result of impact and urgency. | High impact + high urgency = P1. |
| **Severity** | Technical/business seriousness of an issue. | Critical Datamart job failure is high severity. |
| **P1 Incident** | Critical incident with severe business impact. | Production Murex is down; trading/settlement is blocked. |
| **P2 Incident** | High-impact issue requiring urgent resolution. | Important report failed but workaround exists. |
| **P3 Incident** | Medium-impact issue with limited business effect. | Non-critical report formatting issue. |
| **P4 Incident** | Low-impact issue or general request. | Minor UI display issue. |
| **Major Incident** | High-impact, high-urgency issue affecting critical business services. | Complete Murex outage affecting multiple regions. |
| **Business Impact** | Effect of issue on users, processes, revenue, clients, or regulatory obligations. | Regulatory reports cannot be submitted. |
| **Affected Service** | System or business function impacted by an issue. | Murex Datamart reporting service. |
| **Affected Users** | Users experiencing the issue. | Risk, Finance, Operations, and Reporting teams. |
| **Service Restoration** | Returning the service to normal working condition. | EOD job completed successfully after restart. |
| **Resolution** | Action that resolves the incident. | Corrected reference data and reran the job. |
| **Incident Closure** | Confirming service restoration and documenting resolution. | Validated reports and closed ticket with RCA summary. |

An incident is an unplanned interruption or degradation requiring restoration; priority is generally determined from business impact and urgency. [184][186]

## 19.2 RCA and Problem Management

| Term | Meaning | Murex Example |
|---|---|---|
| **RCA** | Root Cause Analysis; structured investigation to find why an issue occurred. | Investigate why a Datamart job failed every Friday. |
| **Root Cause** | Fundamental reason behind an incident or problem. | Missing reference data caused valuation calculation failure. |
| **Symptom** | Visible effect of an issue. | Report shows missing P&L values. |
| **Problem** | Underlying cause or potential cause of one or more incidents. | Bad reference-data load causes repeated report failures. |
| **Problem Management** | Process to identify and eliminate the root cause of recurring incidents. | Analyze repeated MXML failures and implement permanent fix. |
| **Root Cause** | Original reason that led to the failure. | Incorrect mapping caused invalid trade data. |
| **Contributing Cause** | Additional factor that made the issue more likely or more severe. | Missing monitoring alert delayed detection. |
| **5 Whys** | RCA technique asking “why” repeatedly to reach the root cause. | Job failed → file missing → upstream job failed → scheduler issue. |
| **Timeline Reconstruction** | Building a time-based sequence of events before and during an incident. | 22:00 job started, 22:15 file arrived, 22:20 job failed. |
| **Change Analysis** | Checking whether a recent change caused the issue. | New MXML mapping deployed before the failure. |
| **Known Error** | Problem with documented root cause and workaround. | Known issue where a specific report fails after a market-data update. |
| **Known Error Database (KEDB)** | Repository of known problems, root causes, and workarounds. | Search KEDB before troubleshooting a repeated issue. |
| **Workaround** | Temporary solution that restores service but does not remove root cause. | Manually rerun failed job after correcting input file. |
| **Permanent Fix** | Solution that removes the root cause. | Fix upstream data validation to prevent bad file generation. |
| **Preventive Action** | Action taken to stop the issue from happening again. | Add file-arrival and data-quality checks before EOD. |
| **Corrective Action** | Action taken to fix the current issue. | Correct bad reference data and rerun job. |
| **Recurrence** | Same or similar issue happening again. | Same Datamart job fails again next week. |
| **Problem Closure** | Closing a problem after permanent fix and validation. | Permanent fix deployed and no recurrence observed. |

Problem management identifies and resolves underlying causes of incidents to prevent recurrence; a known error is a problem with a documented root cause and workaround. [181][182][183]

## 19.3 Change, Release, and Deployment

| Term | Meaning | Murex Example |
|---|---|---|
| **Change** | Modification to application, configuration, code, infrastructure, or data. | Deploying a new MXML mapping or Datamart report change. |
| **Change Management** | Controlled process to assess, approve, implement, and review changes. | Murex configuration change approved before PROD deployment. |
| **Change Request (CR)** | Formal request to make a change. | CR raised to modify Datamart report logic. |
| **Change Advisory Board (CAB)** | Group that reviews and approves significant/high-risk changes. | CAB approves a critical Murex release. |
| **Change Window** | Approved time period for implementing a change. | Murex deployment scheduled after EOD completion. |
| **Change Impact Assessment** | Analysis of what systems, users, and processes a change may affect. | Check impact on MXML interfaces and downstream reports. |
| **Change Risk** | Possibility that a change may cause an incident or service disruption. | A workflow change may impact trade processing. |
| **Rollback** | Returning system to previous stable state. | Revert a bad MXML configuration deployment. |
| **Rollback Plan** | Documented steps to restore previous version if deployment fails. | Restore previous Datamart job configuration. |
| **Deployment** | Moving code/configuration into an environment. | Deploying MXML mapping changes to UAT. |
| **Release** | Collection of changes deployed together. | Monthly Murex release including workflow and interface changes. |
| **Release Notes** | Document describing changes included in a release. | Details of new MXML fields and Datamart changes. |
| **Post-Implementation Review (PIR)** | Review after change deployment to check success and issues. | Verify report output after Datamart change. |
| **Environment Promotion** | Moving change from one environment to another. | DEV → SIT → UAT → PROD. |
| **Configuration Item (CI)** | Managed component of IT environment, such as server, database, job, or interface. | Murex Datamart job is a CI. |
| **Configuration Management** | Tracking and controlling configuration items and their versions. | Maintain version history of MXML mappings. |

Change management plans, tracks, and releases changes while minimizing disruption; rollback plans are essential for safe deployment. [181][184]

## 19.4 Monitoring and Alerting

| Term | Meaning | Murex Example |
|---|---|---|
| **Monitoring** | Continuously checking health, performance, jobs, and errors. | Monitor Murex services, EOD jobs, queues, and disk usage. |
| **Observability** | Ability to understand system state using logs, metrics, and traces. | Investigate slow Datamart job using logs and metrics. |
| **Metric** | Measurable system value, such as CPU, memory, latency, or job duration. | Datamart job runtime increased from 20 to 90 minutes. |
| **Metric Threshold** | Limit that triggers an alert when crossed. | CPU usage above 90% for 10 minutes. |
| **Alert** | Notification generated when monitoring detects an issue. | Alert raised for failed Control-M job. |
| **Alert Severity** | Level of importance of an alert. | Critical alert for EOD job failure. |
| **Alert Noise** | Too many low-value alerts that make real issues hard to identify. | Repeated non-critical warnings hide a real P1 issue. |
| **Dashboard** | Visual display of system health and business metrics. | Murex EOD dashboard showing job status and failures. |
| **Health Check** | Test to confirm whether a system/component is working. | Check Murex application, database, and interface connectivity. |
| **Heartbeat** | Periodic signal confirming a system is alive. | Murex service sends heartbeat every minute. |
| **Synthetic Monitoring** | Automated test that simulates user/system activity. | Automated check that MXML endpoint responds successfully. |
| **Event** | System-generated occurrence, such as job completion or error. | Datamart job completed successfully. |
| **Event Management** | Monitoring and handling system events. | Automatically create ticket for critical job failure. |
| **Log** | Record of system activity, errors, warnings, and processing details. | Murex application log showing SQL exception. |
| **Log Analysis** | Reviewing logs to identify errors and root causes. | Search logs for `ERROR`, `Exception`, or failed job ID. |
| **Log Retention** | Duration for which logs are stored. | Keep Murex logs for 90 days for RCA. |
| **Correlation ID** | Unique ID linking related log entries/messages across systems. | Trace one MXML message across Murex and downstream system. |
| **Trace** | End-to-end record of a request/process across components. | Trace MXML message from external system to Murex. |
| **APM** | Application Performance Monitoring. | Monitor Murex response time and database query performance. |

## 19.5 Troubleshooting Terms

| Term | Meaning | Murex Example |
|---|---|---|
| **Troubleshooting** | Systematic process to identify and resolve an issue. | Investigate why EOD job failed. |
| **Diagnosis** | Identifying the likely cause of an issue. | Determine whether failure is due to data, SQL, scheduler, or application. |
| **Symptom** | Observable sign of an issue. | Report contains zero rows. |
| **Error Message** | System message indicating a failure. | `ORA-01400: cannot insert NULL into column`. |
| **Exception** | Error condition that interrupts normal processing. | Java `NullPointerException` in MXML transformation. |
| **Stack Trace** | Detailed error report showing where an exception occurred. | Java stack trace identifies failing MXML mapping class. |
| **Debugging** | Detailed investigation to identify code/configuration issue. | Debug Python script processing MXML file. |
| **Reproduction** | Recreating an issue to understand it. | Rerun job with same input file in UAT. |
| **Reproduce Issue** | Create the same failure conditions again. | Use same market-data snapshot and rerun report. |
| **Isolation** | Narrowing down which component causes the issue. | Confirm database is healthy, so issue is in application/job. |
| **Bisecting** | Testing halves of a process/data set to locate failure point. | Test first half and second half of input file separately. |
| **Baseline** | Known good state used for comparison. | Compare today’s report with last successful report. |
| **Regression** | Issue that returns after previously working correctly. | Report worked yesterday but fails after new deployment. |
| **Root Cause Hypothesis** | Initial possible explanation for an issue. | “Missing reference data may have caused valuation failure.” |
| **Validation** | Confirming that a fix works correctly. | Compare report output after rerun. |
| **Verification** | Checking whether the implemented fix meets requirement. | Validate all expected records are present in report. |
| **Impact Assessment** | Determining business effect of an issue or fix. | Check which reports/users are affected. |
| **Blast Radius** | Scope of systems/users/processes affected by an issue or change. | One failed job affects multiple regulatory reports. |
| **Time to Detect (TTD)** | Time taken to identify an issue. | Alert received 10 minutes after job failure. |
| **Time to Restore (TTR)** | Time taken to restore service. | EOD service restored in 45 minutes. |
| **Mean Time to Detect (MTTD)** | Average time to detect issues. | Improve monitoring to reduce MTTD. |
| **Mean Time to Restore (MTTR)** | Average time to restore service after an incident. | Reduce MTTR using runbooks and automation. |
| **Post-Incident Review** | Meeting/document reviewing incident cause, response, and improvements. | Review why EOD failure was not detected earlier. |
| **Lessons Learned** | Improvements identified from an incident. | Add pre-EOD data-validation checks. |

## 19.6 Escalation and Support Levels

| Term | Meaning | Murex Example |
|---|---|---|
| **Escalation** | Raising an issue to a higher support level or management. | Escalate P1 Murex outage to platform team. |
| **Functional Escalation** | Escalation to a team with specialized skills. | Escalate database issue to DBA team. |
| **Hierarchical Escalation** | Escalation to management for authority or urgency. | Escalate major incident to incident manager. |
| **Automatic Escalation** | Escalation triggered automatically by SLA/time rule. | Ticket auto-escalates if not resolved within SLA. |
| **L1 Support** | First-line support; initial triage and basic troubleshooting. | Check job status, logs, and known issues. |
| **L2 Support** | Second-line support; deeper technical investigation. | Analyze Murex logs, SQL, and workflow failures. |
| **L3 Support** | Specialist support; complex/root-cause resolution. | Murex product/development team fixes code defect. |
| **Support Handoff** | Transferring issue from one team/shift to another. | EOD issue handed from day shift to night shift. |
| **Shift Handover** | Documented transfer of open issues and actions between shifts. | Handover notes include failed jobs and next steps. |
| **On-Call Support** | Engineer available outside normal hours for critical issues. | On-call support handles P1 EOD failure. |
| **Stakeholder Communication** | Updating affected users/management about issue status. | Send updates to Risk and Finance teams. |
| **Status Update** | Periodic communication about incident progress. | “Job restarted; validation in progress.” |
| **Bridge Call** | Live call with multiple teams to resolve major incident. | Murex, DBA, infrastructure, and business teams join. |
| **Incident Commander** | Person coordinating major-incident response. | Coordinates Murex, DBA, infra, and business teams. |

Escalation should include the trigger, affected service, impact, diagnostics collected, actions attempted, and reason for escalation. [186][192]

## 19.7 Runbook and Documentation

| Term | Meaning | Murex Example |
|---|---|---|
| **Runbook** | Step-by-step guide to handle a known task, alert, or failure. | Runbook for restarting failed Datamart job. |
| **SOP** | Standard Operating Procedure; documented repeatable process. | SOP for EOD monitoring and incident handling. |
| **Knowledge Base Article (KBA)** | Document explaining issue, cause, and resolution. | KBA for common MXML validation errors. |
| **Known Error Record** | Record of problem, root cause, workaround, and fix status. | Known error for specific market-data issue. |
| **Troubleshooting Guide** | Document explaining how to diagnose an issue. | Guide for Datamart report failure RCA. |
| **Operational Procedure** | Documented process for routine operational work. | Procedure for daily EOD monitoring. |
| **Incident Report** | Document summarizing incident, impact, actions, and resolution. | Report for P1 EOD failure. |
| **RCA Document** | Document explaining root cause, impact, fix, and prevention. | RCA for recurring MXML failure. |
| **Audit Trail** | Record of actions taken during investigation or change. | Log of who restarted job and when. |
| **Lessons Learned Document** | Document capturing improvements after an incident. | Add automated file-arrival checks. |

A runbook is a tested procedure for a specific alert or failure mode; it should explain how to confirm impact, gather evidence, mitigate, roll back, escalate, validate recovery, and preserve an audit trail. [190][193]

## 19.8 SLA and Support Metrics

| Term | Meaning | Murex Example |
|---|---|---|
| **SLA** | Service Level Agreement; agreed response/resolution time. | P1 incident must be acknowledged in 15 minutes. |
| **OLA** | Operational Level Agreement; internal team commitment. | DBA team responds to database issue within 30 minutes. |
| **SLA Breach** | Failure to meet agreed response/resolution time. | P1 ticket not acknowledged within SLA. |
| **Response Time** | Time taken to start working on an incident. | Support team acknowledges ticket. |
| **Resolution Time** | Time taken to fully resolve an incident. | EOD issue resolved and validated. |
| **Restore Time** | Time taken to restore service, even if permanent fix comes later. | Workaround restores reporting before permanent fix. |
| **Downtime** | Period when service is unavailable or degraded. | Datamart reports unavailable for 30 minutes. |
| **Uptime** | Percentage of time service is available. | Murex service availability target: 99.9%. |
| **Availability** | Ability of service to perform its intended function. | Murex application available for users. |
| **First Contact Resolution (FCR)** | Issue resolved during first support interaction. | L1 resolves known batch restart issue. |
| **Ticket Backlog** | Number of unresolved tickets. | Monitor open P2/P3 tickets daily. |
| **Aging Ticket** | Ticket open for longer than expected. | P3 ticket open for 10 days. |
| **Service Request** | Predefined user request, not an incident. | Request for report access or environment refresh. |

## 19.9 Common Murex Support Scenarios

| Scenario | Possible terms to use |
|---|---|
| EOD job failed | Incident, P1/P2, job dependency, log analysis, restart, rerun, RCA |
| Datamart report missing data | Data reconciliation, data-quality check, feed failure, SQL validation, report failure |
| MXML message rejected | Inbound interface, validation error, field mapping, transformation, reprocessing |
| Murex application slow | Performance tuning, APM, CPU/memory, database query, execution plan |
| Trade not moving to next workflow | Workflow status, task, exception queue, validation, approval |
| Settlement failed | Settlement instruction, payment message, reconciliation, break, downstream system |
| Same issue repeats weekly | Problem management, RCA, known error, permanent fix, preventive action |
| Production change caused issue | Change management, rollback, regression, PIR, post-implementation review |

## 19.10 Standard RCA Template

```text
Incident ID:
Incident Title:
Severity / Priority:
Affected Service:
Business Impact:
Incident Start Time:
Service Restored Time:
Resolution Time:

Symptoms:
- What was observed?

Immediate Actions:
- What was done to restore service?

Investigation:
- Logs checked
- Jobs checked
- Database checks
- Recent changes reviewed
- Downstream systems checked

Root Cause:
- What exactly caused the issue?

Contributing Factors:
- Why was it not detected earlier?

Permanent Fix:
- What will prevent recurrence?

Preventive Actions:
- Monitoring improvement
- Automation improvement
- Data validation improvement
- Runbook update

Lessons Learned:
- What should the team do differently?
```

## 19.11 Interview Quick Answers

**What is an incident?**  
An incident is an unplanned interruption or degradation of an IT service that needs to be restored quickly.

**What is the difference between incident and problem?**  
An incident is the immediate issue affecting service. A problem is the underlying cause that can lead to one or more incidents.

**What is RCA?**  
RCA means Root Cause Analysis. It is a structured investigation to identify why an issue occurred and prevent recurrence.

**What is a workaround?**  
A workaround is a temporary solution that restores service or reduces impact before a permanent fix is available.

**What is a known error?**  
A known error is a problem with a documented root cause and a workaround.

**What is escalation?**  
Escalation is raising an issue to a higher support level, specialist team, or management when required.

**What is a runbook?**  
A runbook is a step-by-step guide for handling a known task, alert, or failure scenario.

**What is MTTR?**  
MTTR means Mean Time to Restore. It measures the average time taken to restore service after an incident.

**What is SLA breach?**  
An SLA breach occurs when the agreed response or resolution time is not met.

**How would you troubleshoot a failed Murex EOD job?**  
“I would first check business impact and job status, review scheduler and application logs, identify the failing step, validate input data and dependencies, apply the approved recovery step, rerun/validate the job, and document RCA and preventive actions.”

A problem is the cause or potential cause of one or more incidents; problem management uses RCA to find and eliminate that cause, while a known error records the confirmed cause and workaround. [181][182][187]
```

## Add this to your GitHub

Save this as:

```text
Murex_Glossary/19_Production_Support_Troubleshooting_Glossary.md
```

Then link it from your main glossary file:

```markdown
- [Production Support & Troubleshooting Glossary](./19_Production_Support_Troubleshooting_Glossary.md)
```

## Most important terms for interviews

For Murex Production Support interviews, prioritize these:

- Incident, problem, change  
- P1/P2/P3/P4  
- Impact, urgency, priority  
- SLA, OLA, escalation  
- RCA, root cause, workaround, permanent fix  
- Known error, KEDB  
- Runbook, SOP, knowledge-base article  
- Monitoring, alert, log analysis  
- MTTR, MTTD, downtime, availability  
- Rollback, regression, post-implementation review  

These terms will help you explain Murex incidents professionally—for example: **“This was a P2 Datamart incident caused by a failed upstream feed; I restored reporting through a controlled rerun, performed RCA, and raised a preventive data-validation improvement.”**[1][2][3]

Citations:
[1] www.atlassian.com › itsm › problem-managementProblem Management in ITIL: Process & Implementation Guide https://www.atlassian.com/itsm/problem-management
[2] IT incident management: ITIL lifecycle, Process & Roles https://www.manageengine.com/products/service-desk/it-incident-management/what-is-it-incident-management.html
[3] Incident Management Best Practices: From ITIL to Automation https://resolve.io/blog/incident-management-best-practices
[4] ITIL Problem Management: The Essential Guide - Ivanti https://www.ivanti.com/glossary/problem-management
[5] ITIL Problem Management Best Practices & Tips that Work https://www.freshworks.com/freshservice/itsm/problem-management-best-practices/
[6] ITIL Problem Management: Complete Guide & Best Practices - Infraon https://infraon.io/blog/itil-problem-management-guide-best-practices/
[7] www.novelvista.com › itil-root-cause-analysisITIL Root Cause Analysis: Process & Practical Guide https://www.novelvista.com/blogs/it-service-management/itil-root-cause-analysis
[8] www.manageengine.com › products › service-deskDifference between ITIL incident, problem, change and asset https://www.manageengine.com/products/service-desk/itsm/incident-problem-change-asset-management.html
[9] www.sherlocks.ai › blog › root-cause-analysis-forRoot Cause Analysis for Production Incidents: A Modern Guide ... https://www.sherlocks.ai/blog/root-cause-analysis-for-production-incidents
[10] web-alert.io › blog › incident-runbook-templateIncident Runbook Template and Examples | Webalert https://web-alert.io/blog/incident-runbook-template-response-guide
[11] ITIL Problem Management: A Comprehensive Guide https://www.invensislearning.com/blog/itil-problem-management-process-simplified/
[12] Incident Management | IT Process Wiki https://wiki.en.it-processmaps.com/index.php/Incident_Management
[13] codezips.com › it-runbook-generator-for-help-deskIT Runbook Generator for Help Desk, NOC, MSP and Sysadmin Teams https://codezips.com/it-runbook-generator-for-help-desk-noc-msp-and-sysadmin-teams/
[14] upstat.io › blog › runbook-procedures-guideComplete Guide to Runbooks and Operational Procedures https://upstat.io/blog/runbook-procedures-guide
[15] upstat.io › blog › runbook-template-examplesRunbook Templates and Examples for IT Teams - upstat.io https://upstat.io/blog/runbook-template-examples


