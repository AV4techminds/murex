
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
