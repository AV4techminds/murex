# `01-capital-markets-foundation/day-01-capital-markets-overview.md`

````markdown
# Day 01 — Capital Markets Overview

> Murex Techno-Functional Preparation
>
> Chapter: 01 — Capital Markets Foundation
> Topic: Capital Markets Overview
> Learning Mode: Business → Functional → Technical → Murex → Hands-on
> Status: 🟡 In Progress

---

# 1. Learning Objective

The objective of this topic is to build a strong understanding of:

- Financial markets
- Capital markets
- Types of financial markets
- Why financial markets exist
- Market participants
- Financial instruments
- Financing
- Investment
- Liquidity
- Risk management
- Hedging
- FX exposure
- FX risk
- Market vs instrument vs trade
- Primary vs secondary markets
- OTC vs exchange-traded markets
- High-level trade lifecycle
- Business requirement
- Functional requirement
- Technical implementation
- Murex relevance

The goal is not memorization.

The goal is to understand:

```text
WHY
 ↓
BUSINESS REQUIREMENT
 ↓
WHAT
 ↓
FINANCIAL PRODUCT / TRADE
 ↓
HOW
 ↓
FUNCTIONAL PROCESS
 ↓
SYSTEM IMPLEMENTATION
 ↓
MUREX
 ↓
TECHNICAL ECOSYSTEM
 ↓
RISK / P&L / SETTLEMENT / ACCOUNTING / REPORTING
````

---

# 2. What Is a Financial Market?

## Definition

A financial market is an ecosystem in which participants buy, sell, issue, exchange, finance, invest in, or manage financial assets, instruments, capital, and financial risks.

Financial markets enable:

* Capital raising
* Investment
* Borrowing
* Lending
* Trading
* Liquidity management
* Price discovery
* Risk transfer
* Hedging
* Financial risk management

A financial market does not necessarily mean a physical location.

Modern financial markets can operate through:

* Exchanges
* Electronic trading platforms
* Dealer networks
* Brokers
* OTC bilateral arrangements
* Electronic communication networks
* Clearing and settlement infrastructure

---

# 3. Why Do Financial Markets Exist?

Financial markets exist because different participants have different financial needs.

For example:

### Company

A company may need:

* Funding
* Foreign currency
* Interest-rate management
* Commodity-price protection

### Investor

An investor may have:

* Excess capital
* Investment objectives
* Return objectives
* Portfolio risk

### Bank

A bank may:

* Provide financing
* Execute client trades
* Make markets
* Provide liquidity
* Hedge exposures
* Trade for its own portfolio

Financial markets bring these participants together.

---

# 4. Major Types of Financial Markets

Financial markets can be classified in different ways.

For Murex preparation, understand the following major areas:

```text
FINANCIAL MARKETS
│
├── Money Market
│
├── Capital Market
│   ├── Equity Market
│   └── Debt / Fixed-Income Market
│
├── Foreign Exchange Market
│
├── Derivatives Market
│
├── Commodity Market
│
├── Credit Market
│
└── Interest-Rate Market
```

These categories can overlap.

For example, an interest-rate derivative can belong to both:

* Derivatives
* Interest-rate products

---

# 5. Money Market

## Definition

The money market is the market for short-term borrowing, lending and financial instruments, generally involving maturities of up to one year.

## Purpose

The money market primarily supports:

* Short-term funding
* Liquidity management
* Cash management
* Short-term borrowing and lending

## Examples

* Treasury Bills
* Commercial Paper
* Certificates of Deposit
* Repo
* Interbank lending

## Business Example

A bank temporarily needs additional liquidity.

Another institution has excess cash.

The bank can obtain short-term funding through the money market.

```text
Institution A
Has excess cash
      |
      | Short-term funding
      v
Institution B
Needs liquidity
```

---

# 6. Capital Market

## Definition

The capital market is the part of the financial system primarily associated with longer-term capital raising, investment and trading through instruments such as equities and debt securities.

## Main Areas

```text
CAPITAL MARKET
│
├── Equity
│   └── Shares
│
└── Debt
    ├── Government Bonds
    └── Corporate Bonds
```

Capital-market participants may also use derivatives to manage risks associated with these markets.

---

# 7. Primary Market

## Definition

The primary market is where newly issued securities are sold to investors and the issuer receives the proceeds.

## Business Requirement

A company needs:

```text
₹1,000 Crore
```

to expand its business.

It decides to issue new shares.

## Flow

```text
Company / Issuer
       |
       | Issues new shares
       v
Primary Market
       |
       | Shares
       v
Investor
       |
       | Capital
       v
Company
```

## Business Objective

The company is raising new capital.

---

# 8. Secondary Market

## Definition

The secondary market is where previously issued financial instruments are traded between investors or other market participants.

## Example

Investor A already owns shares.

Investor B wants to buy them.

```text
Investor A
    |
    | Shares
    v
Investor B

Investor B
    |
    | Money
    v
Investor A
```

The issuer generally does not receive the proceeds from this particular secondary-market transaction.

## Business Objective

Secondary markets provide:

* Liquidity
* Price discovery
* Ability to enter or exit investments

---

# 9. Equity Market

## Definition

The equity market is the market where ownership interests in companies are issued and traded.

## Example

```text
Investor
    |
    | Capital
    v
Company
    |
    | Shares
    v
Investor
```

The investor receives an ownership interest.

## Business Requirement

A company needs capital without taking on additional debt.

## Possible Solution

Issue equity.

---

# 10. Debt Market

## Definition

The debt market is the market where debt instruments are issued and traded.

Examples:

* Government bonds
* Corporate bonds
* Notes
* Other fixed-income securities

## Business Requirement

A company needs ₹1,000 crore but does not want to issue additional equity.

## Possible Solution

Raise debt.

```text
Investor
    |
    | Money
    v
Company / Issuer
    |
    | Bond
    v
Investor
```

The company has a contractual obligation according to the bond terms.

---

# 11. Foreign Exchange Market

## Definition

The foreign exchange (FX) market is the global market in which one currency is exchanged for another.

Examples:

```text
EUR/USD
USD/INR
GBP/USD
USD/JPY
```

## Why Is FX Needed?

Participants require foreign currencies for:

* Imports
* Exports
* International payments
* International investments
* Foreign funding
* Hedging
* Trading

---

# 12. Real-World FX Business Requirement

## Business Requirement

An Indian company has purchased equipment from a German company.

The German supplier must receive:

```text
EUR 10 Million
```

in three months.

The Indian company primarily has INR.

Therefore:

```text
Business Requirement
       ↓
Need EUR 10M
       ↓
Foreign Currency Requirement
       ↓
FX Transaction
```

---

# 13. FX Exposure

The company has a future obligation:

```text
Pay EUR 10M
```

The company does not know exactly how much INR will be required in three months because the EUR/INR exchange rate can change.

This creates an:

> FX Exposure

---

# 14. FX Risk

Assume today's rate is:

```text
EUR/INR = ₹90
```

Required amount:

```text
EUR 10M
```

Current INR equivalent:

```text
€10M × ₹90
= ₹900M
= ₹90 Crore
```

Suppose after three months:

```text
EUR/INR = ₹95
```

Then:

```text
€10M × ₹95
= ₹950M
= ₹95 Crore
```

Additional INR requirement:

```text
₹95 Crore - ₹90 Crore
= ₹5 Crore
```

Therefore, the company faces uncertainty in its INR cost.

This is:

> **Foreign Exchange Risk**

---

# 15. Hedging

## Definition

Hedging is a risk-management technique used to reduce or manage the impact of an existing financial exposure.

## Business Requirement

The company knows:

> "I must pay EUR 10M in three months."

But it is worried:

> "EUR may become more expensive against INR."

Therefore:

```text
Future EUR Payment
       ↓
EUR Exposure
       ↓
FX Risk
       ↓
Hedging Requirement
```

---

# 16. FX Forward

One possible hedge is an FX Forward.

## Definition

An FX forward is a derivative contract in which two parties agree today to exchange specified currencies at an agreed exchange rate for a future date.

Simplified:

```text
Company
    |
    | FX Forward
    v
Bank
```

Suppose the company agrees to:

```text
₹90 / EUR
```

for:

```text
EUR 10M
```

Simplified INR amount:

```text
€10M × ₹90
= ₹90 Crore
```

If the market rate later becomes ₹95, the forward helps the company manage the uncertainty associated with the future exchange rate.

---

# 17. Important Hedging Trade-Off

Hedging is about managing uncertainty.

It does not mean:

> "The company will always get the best possible market rate."

Suppose the market moves:

```text
₹90 → ₹95
```

The hedge protects against the unfavorable increase.

But suppose the market moves:

```text
₹90 → ₹85
```

The company could have obtained EUR more cheaply at the market rate if it had remained unhedged.

Therefore:

```text
HEDGING
│
├── Reduces uncertainty
│
├── Protects against unfavorable movements
│
└── May reduce benefit from favorable movements
```

---

# 18. Payment vs Hedge

This is an important distinction.

## Actual Business Payment

```text
Indian Company
       |
       | EUR Payment
       v
German Supplier
```

Purpose:

> Fulfill the underlying business obligation.

## FX Hedge

```text
Indian Company
       |
       | FX Forward
       v
Bank
```

Purpose:

> Manage the FX exposure associated with the future obligation.

### Key Principle

```text
Underlying Business Obligation
            |
            v
          Exposure
            |
            v
           Risk
            |
            v
       Hedge Trade
```

The hedge and the underlying payment are related, but they are not the same transaction.

---

# 19. Derivatives Market

## Definition

A derivative is a financial contract whose value depends on an underlying asset, rate, index, currency, commodity or other reference.

Examples:

* Forward
* Future
* Option
* Swap

## Examples

```text
EUR/USD
   ↓
FX Derivative
```

```text
Interest Rate
   ↓
Interest Rate Swap
```

```text
Equity
   ↓
Equity Derivative
```

---

# 20. Commodity Market

## Definition

The commodity market is the market where physical commodities and commodity-related financial contracts are traded.

Examples:

* Crude Oil
* Natural Gas
* Gold
* Silver
* Agricultural commodities
* Metals

## Why Do Participants Use It?

* Physical requirements
* Investment
* Trading
* Speculation
* Hedging

---

# 21. Credit Market

## Definition

The credit market is the market involving borrowing, lending and financial instruments whose value or risk is linked to the creditworthiness of a borrower or issuer.

Examples:

* Corporate bonds
* Credit-linked instruments
* Credit derivatives
* Credit Default Swaps

---

# 22. Interest-Rate Market

## Definition

The interest-rate market involves financial instruments and transactions whose value or cash flows are affected by interest rates.

Examples:

* Government bonds
* Interest-rate swaps
* OIS
* FRAs
* Interest-rate futures

## Business Requirements

Participants may use interest-rate markets for:

* Funding
* Investment
* Trading
* Interest-rate risk management
* Hedging

---

# 23. OTC Market

## Definition

OTC means:

> Over-The-Counter

OTC trading generally occurs directly between counterparties rather than through a centralized exchange order book.

Examples:

* FX forwards
* Interest-rate swaps
* Customized derivatives

OTC transactions can provide flexibility in:

* Notional
* Maturity
* Currency
* Payment dates
* Contract terms

A detailed OTC vs Exchange-Traded comparison will be covered later.

---

# 24. Exchange-Traded Market

## Definition

An exchange-traded market is a market where standardized instruments are traded through an organized exchange.

Characteristics may include:

* Standardized contracts
* Organized trading
* Exchange rules
* Transparent pricing
* Clearing arrangements

Examples include:

* Stocks
* Futures
* Certain options

---

# 25. Market vs Instrument vs Trade

These three terms must be clearly separated.

## Market

The financial ecosystem where financial activity occurs.

Example:

```text
FX Market
```

## Instrument

The financial product or contract.

Example:

```text
EUR/USD Forward
```

## Trade

The actual transaction entered into by two counterparties.

Example:

```text
Bank A
   |
   | EUR/USD Forward Trade
   |
Bank B
```

### Relationship

```text
Market
   ↓
Instrument
   ↓
Trade
```

---

# 26. Business Requirement → Functional Requirement → Technical Requirement

This is one of the most important learning patterns for our Murex preparation.

## Business Requirement

The business says:

> "Our corporate client must pay EUR 10M in three months and wants to reduce the risk of EUR appreciation against INR."

This describes the business need.

---

## Functional Requirement

The functional team translates that need into a financial process:

```text
Client has EUR exposure
        ↓
FX risk identified
        ↓
Client enters FX hedge
        ↓
FX Forward booked
        ↓
Trade lifecycle processed
        ↓
Risk / P&L calculated
        ↓
Settlement handled
```

---

## Technical Requirement

The technical team needs to implement/support the process.

Potential technical areas include:

```text
Trade Capture
      ↓
Integration
      ↓
MXML / Interface
      ↓
Murex Processing
      ↓
Oracle / Data
      ↓
Risk / P&L
      ↓
Settlement
      ↓
Datamart
      ↓
Reporting
```

Supporting technology can involve:

* Linux / Unix
* Shell scripting
* Python
* Oracle / SQL
* Networking
* SFTP
* APIs
* Messaging
* MXML
* Monitoring
* DevOps

---

# 27. Murex Perspective

From a Murex perspective, the transaction is not finished when the trader executes it.

The trade may need to pass through:

```text
Trade Execution
       ↓
Trade Capture
       ↓
Validation
       ↓
Enrichment
       ↓
Position
       ↓
Valuation
       ↓
Risk
       ↓
P&L
       ↓
Confirmation
       ↓
Settlement
       ↓
Accounting
       ↓
Datamart
       ↓
Reporting
```

The exact implementation depends on the institution and its architecture.

---

# 28. Full End-to-End Business Story

## Scenario

An Indian manufacturing company imports machinery from Germany.

The German supplier will receive:

```text
EUR 10M
```

after three months.

The company earns primarily in INR.

---

## Step 1 — Business Requirement

The company needs:

```text
EUR 10M
```

in three months.

Business problem:

> The company does not know how much INR will be required at the future payment date.

---

## Step 2 — Risk Identification

Potential problem:

```text
EUR appreciates against INR
        ↓
EUR becomes more expensive
        ↓
More INR required
        ↓
Higher business cost
```

This is FX risk.

---

## Step 3 — Hedging Decision

The company wants to reduce the uncertainty.

It approaches its bank.

```text
Company
   ↓
Bank
   ↓
FX Hedging Solution
```

---

## Step 4 — Trade

The company enters an FX forward with the bank.

```text
Company
    ↕
FX Forward
    ↕
Bank
```

The trade becomes a financial transaction that must be processed.

---

## Step 5 — Trade Capture

The bank captures the transaction in its trading system.

Potential information includes:

* Product
* Currency pair
* Buy/Sell direction
* Notional
* Rate
* Trade date
* Value date
* Maturity
* Counterparty
* Legal entity
* Book
* Portfolio

These concepts will be studied in detail later.

---

## Step 6 — Murex Processing

The trade may be processed in Murex.

```text
Trade
  ↓
Validation
  ↓
Enrichment
  ↓
Valuation
  ↓
Risk
  ↓
P&L
```

---

## Step 7 — Integration

Other systems may exchange information with Murex.

Possible technologies:

```text
External System
      ↓
API / SFTP / Messaging
      ↓
MXML / Integration Layer
      ↓
Murex
```

---

## Step 8 — Technical Processing

Technical teams may use:

### Linux / Unix

For:

* Batch jobs
* Files
* Processes
* Logs
* Operational support

### Shell

For:

* Automation
* File processing
* Job control
* Monitoring

### Python

For:

* Data validation
* File processing
* Automation
* Reconciliation
* Operational tooling

### Oracle / SQL

For:

* Data investigation
* Validation
* Reconciliation
* Reporting/support

---

## Step 9 — Risk and P&L

The bank needs to understand:

* Current valuation
* Market exposure
* FX sensitivity
* Profit/Loss
* Counterparty exposure

---

## Step 10 — Settlement

When the transaction reaches the relevant settlement date, the contractual currency obligations need to be fulfilled.

---

## Step 11 — Accounting

The relevant financial events are reflected in accounting processes.

---

## Step 12 — Datamart and Reporting

Data may flow into a data/reporting environment.

```text
Murex
  ↓
Datamart
  ↓
Reports
  ↓
Business / Risk / Management
```

---

# 29. Complete Story — One View

```text
BUSINESS NEED
Company must pay EUR 10M
          |
          v
FX EXPOSURE
Future EUR obligation
          |
          v
FX RISK
EUR/INR may increase
          |
          v
HEDGING REQUIREMENT
Reduce FX uncertainty
          |
          v
FX FORWARD
Trade with Bank
          |
          v
TRADE CAPTURE
          |
          v
VALIDATION
          |
          v
ENRICHMENT
          |
          v
MUREX PROCESSING
          |
     +----+----+
     |         |
     v         v
 VALUATION    RISK
     |         |
     +----+----+
          |
          v
         P&L
          |
          v
    CONFIRMATION
          |
          v
      SETTLEMENT
          |
          v
      ACCOUNTING
          |
          v
      DATAMART
          |
          v
       REPORTING
```

---

# 30. Technical Ecosystem — High Level

```text
External Systems
       |
       v
Networking
       |
       +-- API
       +-- SFTP
       +-- Messaging
       |
       v
Linux / Unix
       |
       +-- Shell
       +-- Python
       |
       v
Integration
       |
       +-- MXML
       |
       v
Murex
       |
       +-- Trading
       +-- Risk
       +-- P&L
       +-- Operations
       |
       v
Oracle / SQL
       |
       v
Datamart
       |
       v
Reporting
```

This is a conceptual architecture only. The actual architecture differs between organizations.

---

# 31. Key Business Use Cases

## Use Case 1 — Corporate FX Payment

Business need:

> Pay a foreign supplier.

Market:

> FX Market.

Instrument:

> FX transaction.

---

## Use Case 2 — FX Hedging

Business need:

> Reduce uncertainty caused by exchange-rate movements.

Possible instrument:

> FX Forward.

---

## Use Case 3 — Corporate Funding

Business need:

> Raise money for expansion.

Possible instruments:

> Bonds or equity.

---

## Use Case 4 — Investor Portfolio

Business need:

> Invest capital and generate returns.

Possible instruments:

> Equity, bonds, derivatives and other investments.

---

## Use Case 5 — Bank Risk Management

Business need:

> Manage exposure created by client transactions or market movements.

Possible solutions:

> Hedging transactions and risk-management strategies.

---

# 32. Important Distinctions

| Concept          | Meaning                                                               |
| ---------------- | --------------------------------------------------------------------- |
| Financial Market | Broad ecosystem for financial activity                                |
| Capital Market   | Market primarily associated with longer-term financing and investment |
| Money Market     | Short-term funding and instruments                                    |
| Primary Market   | New securities are issued                                             |
| Secondary Market | Existing securities are traded                                        |
| Equity           | Ownership interest                                                    |
| Debt             | Borrowing/credit obligation                                           |
| FX               | Currency exchange                                                     |
| Derivative       | Contract derived from an underlying                                   |
| OTC              | Bilateral/non-centralized exchange trading arrangement                |
| Exchange-Traded  | Standardized instruments traded through an organized exchange         |
| Exposure         | Financial position subject to risk                                    |
| Risk             | Potential adverse financial impact from uncertainty                   |
| Hedge            | Position/strategy used to reduce or manage risk                       |
| Trade            | Actual transaction between counterparties                             |
| Instrument       | Financial product/contract                                            |
| Market           | Financial ecosystem                                                   |

---

# 33. Glossary

| Term             | Definition                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Capital Market   | Market primarily associated with longer-term capital raising, investment and trading       |
| Financial Market | Ecosystem where financial assets, instruments, capital and risks are exchanged             |
| Money Market     | Market for short-term borrowing, lending and financial instruments                         |
| Primary Market   | Market for newly issued securities                                                         |
| Secondary Market | Market for trading previously issued securities                                            |
| Equity           | Ownership interest in a company                                                            |
| Debt             | Financial obligation created by borrowing                                                  |
| Bond             | Debt security issued by an entity                                                          |
| FX               | Foreign Exchange                                                                           |
| FX Exposure      | Exposure resulting from foreign-currency assets, liabilities or commitments                |
| FX Risk          | Risk caused by changes in exchange rates                                                   |
| Hedging          | Risk-management technique used to reduce/manage exposure                                   |
| FX Forward       | Derivative contract for a future currency exchange at an agreed rate                       |
| Derivative       | Contract whose value depends on an underlying                                              |
| Underlying       | Asset, rate, index, currency, commodity or reference from which a derivative derives value |
| OTC              | Over-The-Counter                                                                           |
| Liquidity        | Ability to transact or convert an asset with limited price impact                          |
| Price Discovery  | Process by which market prices are determined                                              |
| Counterparty     | Other party to a financial transaction                                                     |
| Trade            | Executed financial transaction                                                             |
| Instrument       | Financial product or contract                                                              |
| Notional         | Reference amount used in financial calculations                                            |
| Valuation        | Process of determining the value of a financial position                                   |
| P&L              | Profit and Loss                                                                            |
| Settlement       | Fulfillment of obligations created by a trade                                              |
| Datamart         | Data environment used for reporting and analysis                                           |
| Legal Entity     | Legally recognized entity entering into a transaction                                      |
| Exposure         | Amount or position subject to potential financial impact                                   |

---

# 34. Interview Questions

## Q1. What are financial markets?

Financial markets are ecosystems where participants raise, invest, borrow, lend, trade and manage financial assets, instruments, capital and risks.

---

## Q2. What is a capital market?

A capital market is a major part of the financial system primarily associated with longer-term capital raising, investment and trading through instruments such as equities and debt securities.

---

## Q3. What is the difference between financial markets and capital markets?

Financial markets are the broader concept. Capital markets are a major component of the financial system focused primarily on longer-term financing, investment and trading.

---

## Q4. What is the difference between money market and capital market?

Money markets primarily support short-term borrowing, lending and instruments, generally up to one year.

Capital markets primarily support longer-term financing, investment and trading.

---

## Q5. What is FX risk?

FX risk is the risk that changes in exchange rates will adversely affect the value or cost of a foreign-currency exposure.

---

## Q6. Why would a corporate use an FX forward?

A corporate may use an FX forward to manage uncertainty associated with a future foreign-currency requirement or exposure.

---

## Q7. What is the difference between an underlying exposure and a hedge?

The underlying exposure comes from the company's business activity, such as a future EUR payment.

The hedge is a separate financial position taken to reduce or manage the risk associated with that exposure.

---

## Q8. What is the difference between payment and hedge?

The payment fulfills the underlying business obligation.

The hedge manages the financial risk associated with that obligation.

---

## Q9. What is the difference between primary and secondary markets?

In the primary market, newly issued securities are sold and the issuer receives the proceeds.

In the secondary market, existing securities are traded between market participants.

---

## Q10. What is the difference between market, instrument and trade?

A market is the financial ecosystem, an instrument is the financial product or contract, and a trade is the actual transaction entered into between counterparties.

---

# 35. Scenario-Based Interview Question

### Question

An Indian corporate needs to pay EUR 10M to a German supplier in three months. EUR/INR is currently ₹90 and the corporate is worried that EUR may appreciate.

Explain the complete scenario.

### Strong Answer Structure

```text
1. Business Requirement
   ↓
   Future EUR payment

2. Exposure
   ↓
   EUR 10M future obligation

3. Risk
   ↓
   EUR/INR may increase

4. Risk Management
   ↓
   Hedge the exposure

5. Instrument
   ↓
   FX Forward

6. Counterparty
   ↓
   Bank

7. Trade
   ↓
   FX Forward is booked

8. Processing
   ↓
   Capture → Validation → Enrichment

9. Murex
   ↓
   Valuation → Risk → P&L

10. Operations
    ↓
    Confirmation → Settlement

11. Finance
    ↓
    Accounting

12. Data
    ↓
    Datamart → Reporting
```

---

# 36. Hands-On Exercise

## Scenario

Create your own trade story.

### Business

An Indian company must pay:

```text
EUR 10M
```

after three months.

### Market

```text
EUR/INR = ₹90
```

### Risk

EUR/INR may increase.

### Task

Explain:

1. Business requirement
2. Exposure
3. Risk
4. Hedging requirement
5. Possible financial instrument
6. Counterparty
7. Trade
8. Trade capture
9. Validation
10. Enrichment
11. Valuation
12. Risk
13. P&L
14. Settlement
15. Accounting
16. Datamart
17. Reporting
18. Where Murex fits
19. Where Linux/Shell could fit
20. Where Python could fit
21. Where Oracle/SQL could fit
22. Where networking/integration could fit

---

# 37. Day 01 Learning Status

## Conceptual

* [x] Financial Market
* [x] Capital Market
* [x] Money Market
* [x] Primary Market
* [x] Secondary Market
* [x] Equity Market
* [x] Debt Market
* [x] FX Market
* [x] Derivatives Market
* [x] Commodity Market
* [x] Credit Market
* [x] Interest-Rate Market
* [x] OTC Market — introduction
* [x] Exchange-Traded Market — introduction

## Risk & Product

* [x] FX Exposure
* [x] FX Risk
* [x] Hedging
* [x] FX Forward — basic understanding
* [x] Payment vs Hedge

## Murex

* [x] Market vs Instrument vs Trade
* [x] High-Level Trade Lifecycle
* [x] Murex relevance
* [x] Business → Functional → Technical mapping

## Practical

* [ ] Full hands-on FX trade simulation
* [ ] Murex-style trade data
* [ ] Integration simulation
* [ ] Linux/Shell processing
* [ ] Python validation
* [ ] Oracle/SQL validation
* [ ] Failure scenarios
* [ ] Production troubleshooting

These practical items will be developed as we progress through the later chapters.

---

# 38. Chapter 01 — Remaining Topics

* [ ] Capital Markets Overview
* [ ] Buy Side / Sell Side
* [ ] Asset Classes
* [ ] Cash vs Derivatives
* [ ] OTC vs Exchange Traded
* [ ] Trading Venues
* [ ] Market Participants
* [ ] Trade Terminology
* [ ] Trade Date / Value Date / Maturity
* [ ] Notional / Price / Rate / Quantity
* [ ] Books / Portfolios / Desks
* [ ] Counterparties
* [ ] Legal Entities

---

# 39. Learning Principle

For every future topic, follow:

```text
CONCEPT
   ↓
DEFINITION
   ↓
WHY DOES IT EXIST?
   ↓
BUSINESS REQUIREMENT
   ↓
REAL-WORLD USE CASE
   ↓
FINANCIAL PRODUCT
   ↓
TRADE
   ↓
FUNCTIONAL PROCESS
   ↓
MUREX PROCESS
   ↓
TECHNICAL IMPLEMENTATION
   ↓
INTEGRATION
   ↓
DATABASE / DATA
   ↓
RISK / P&L
   ↓
SETTLEMENT
   ↓
PRODUCTION SUPPORT
   ↓
HANDS-ON LAB
   ↓
TROUBLESHOOTING
   ↓
INTERVIEW QUESTIONS
   ↓
GLOSSARY
```

---

# 40. Final Mental Model

The most important model from Day 01:

```text
BUSINESS
Company needs EUR
       ↓
MARKET
FX Market
       ↓
INSTRUMENT
FX Forward
       ↓
TRADE
Company ↔ Bank
       ↓
MUREX
Trade Processing
       ↓
RISK / VALUATION / P&L
       ↓
OPERATIONS
Confirmation / Settlement
       ↓
FINANCE
Accounting
       ↓
DATA
Datamart / Reporting
       ↓
TECHNOLOGY
Linux / Shell / Python /
Oracle / SQL / Networking /
Integration / MXML / DevOps
```

> **This is the techno-functional mindset we will use throughout the entire Murex preparation.**

```

### One change I strongly recommend for our sessions

From now on, **don't copy notes immediately after every explanation**. We'll discuss first.

For example, for the next topic **Buy Side / Sell Side**, we'll actually take one transaction and follow:

**Corporate → Bank → Trader → Desk → Book → Counterparty → Murex → Risk → Settlement**

During the discussion, I'll keep challenging you with questions such as:

> "Why does the bank need a trader here?"  
> "Who is the counterparty?"  
> "Which side is Buy Side?"  
> "Where would this trade be booked?"  
> "What would Murex need to know?"  
> "What could go wrong technically?"


That will give you something much more valuable than interview notes: **a complete mental model of how a real bank transaction works.**
```
