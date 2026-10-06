# Murex Techno-Functional — Day 1
# Chapter 1: Capital Markets Foundation

# 📋 Today's Agenda

## Topic 1 — Capital Markets Overview
- What is a Financial Market?
- Why do Financial Markets exist?
- Major types of Financial Markets
- Market vs Product vs Trade
- Business Requirement
- Functional Requirement
- Technical Requirement
- Real-world FX example

## Topic 2 — Buy Side vs Sell Side
- What is Buy Side?
- What is Sell Side?
- Examples
- Buy Side vs Sell Side
- Important interview clarification
- Client vs Counterparty introduction
- Murex relevance

## Topic 3 — Asset Classes
- What is an Asset Class?
- FX
- Rates
- Fixed Income / Debt
- Equity
- Credit
- Commodities
- Asset Class vs Product vs Trade
- Asset Class vs Derivative classification
- Asset Class and Risk
- Asset Class and Market Data
- Murex relevance

## Final Revision
- Quick Recall
- Key Definitions
- Memory Map
- End-to-End Business Story

---

# 1. CAPITAL MARKETS OVERVIEW

## 1.1 What is a Financial Market?

### Definition

A **Financial Market** is an ecosystem where participants buy, sell, issue, exchange, finance, invest in, and manage financial assets and financial risks.

### Simple Explanation

Think of a financial market as a place/system where:

- Someone needs money
- Someone has money
- Someone wants to invest
- Someone wants to borrow
- Someone wants to buy or sell a financial asset
- Someone wants to manage financial risk

The financial market connects these participants.

### Simple Formula

Financial Market:

**Money + Investment + Funding + Risk Management**

---

# 1.2 Why Do Financial Markets Exist?

Financial markets mainly exist for the following purposes.

## 1. Capital Raising

Companies and governments need money for:

- Business expansion
- Infrastructure
- Projects
- Working capital
- Other funding requirements

They can raise money through:

- Bonds
- Shares
- Loans
- Other financial instruments

### Example

```text
Company
   |
   | Needs Funding
   v
Financial Market
   |
   v
Investors / Banks
   |
   v
Capital Raised


---

2. Investment

Some institutions have excess money and want to invest it.

Examples:

Mutual Funds

Pension Funds

Insurance Companies

Asset Managers


They may invest in:

Bonds

Equity

Money-market instruments

Derivatives

Other financial products



---

3. Liquidity

Liquidity means the ability to buy or sell an asset without excessive difficulty.

Example:

An investor owns a bond but needs cash.

A functioning market may allow the investor to sell the bond to another participant.

Investor
   |
   | Owns Bond
   |
   | Needs Cash
   v
Financial Market
   |
   v
Sell Bond
   |
   v
Receive Cash


---

4. Price Discovery

Markets help determine the current market price of financial instruments.

Prices are influenced by:

Supply

Demand

Interest rates

Economic conditions

Market expectations

Risk

Liquidity


Example

EUR/INR:

EUR/INR = ₹90

This represents the market price/exchange rate at that point in time.


---

5. Risk Management

Participants have different financial risks.

Examples:

FX Risk

Interest Rate Risk

Equity Risk

Credit Risk

Commodity Risk


Financial markets provide instruments and mechanisms to manage these risks.


---

6. Risk Transfer

One participant may want to reduce a particular risk.

Another participant may be willing to take that exposure.

Financial instruments, especially derivatives, can help transfer/manage risk.


---

1.3 Major Types of Financial Markets

Money Market

Focus:

> Short-term borrowing and lending.



Examples:

Treasury Bills

Commercial Paper

Certificates of Deposit

Short-term funding



---

Capital Market

Focus:

> Longer-term financing and investment.



Major areas:

Equity Market

Debt/Bond Market



---

FX Market

Focus:

> Buying and selling/exchanging currencies.



Examples:

EUR/USD

USD/INR

GBP/USD

USD/JPY

EUR/INR


Common FX products:

FX Spot

FX Forward

FX Swap

FX Option

NDF



---

Equity Market

Focus:

> Ownership/share-price exposure.



Examples:

Shares

Equity instruments

Equity derivatives



---

Debt/Bond Market

Focus:

> Borrowing and lending through debt instruments.



Examples:

Government Bonds

Corporate Bonds



---

Derivatives Market

Focus:

> Contracts whose value is derived from an underlying asset, price, rate, index, or other reference.



Examples:

Forwards

Futures

Options

Swaps


Underlying exposures can include:

FX

Interest Rates

Equity

Commodities

Credit



---

1.4 Market vs Product vs Trade

This is one of the most important concepts to remember.

Market

The broader financial environment.

Example:

> FX Market



Product

The specific financial instrument.

Example:

> FX Forward



Trade

The actual transaction between specific parties with specific terms.

Example:

> Corporate enters an EUR/INR FX Forward with a Bank.



Memory Pattern

MARKET
   |
   v
PRODUCT
   |
   v
TRADE

Example

FX Market
   |
   v
FX Forward
   |
   v
EUR/INR Forward Trade
   |
   v
Corporate <----> Bank


---

1.5 Business Requirement → Functional Requirement → Technical Requirement

This pattern will be used throughout our Murex learning.

Business Requirement

The business requirement explains what the business wants to achieve.

Example:

> An Indian company needs EUR 10 million after three months and wants to reduce uncertainty caused by EUR/INR movements.




---

Functional Requirement

The functional requirement explains what the financial/business process needs to do.

Example:

> Identify the FX exposure, book an EUR/INR FX Forward, process the trade lifecycle, calculate valuation/risk/P&L, and settle the transaction.




---

Technical Requirement

The technical requirement explains how systems/processes support the functional requirement.

Potential areas:

Trade capture

Interfaces

MxML/API

Validation

Workflow

Market data

Processing

Database

Risk/P&L

Settlement

Accounting

DataMart

Reporting



---

1.6 Real-World FX Example

An Indian manufacturer purchases machinery from Germany.

The German supplier requires:

> EUR 10 million



Payment is required after:

> 3 months



The Indian company mainly earns money in:

> INR




---

Current Exchange Rate

Suppose:

EUR/INR = ₹90

If the company needed EUR 10 million today:

EUR 10M × ₹90

= ₹900M

= ₹90 Crore


---

What if EUR Becomes More Expensive?

Suppose after some time:

EUR/INR = ₹95

Then:

EUR 10M × ₹95

= ₹950M

= ₹95 Crore

Difference:

₹95 Crore - ₹90 Crore

= ₹5 Crore

Therefore, the company has exposure to:

> FX Risk




---

Possible Solution

The company can consider using an:

> EUR/INR FX Forward



to manage/reduce the uncertainty associated with the future exchange rate.


---

1.7 Murex View of the FX Example

The business story can become a Murex processing flow:

Business Requirement
        |
        v
FX Exposure
        |
        v
FX Hedge Requirement
        |
        v
FX Forward Trade
        |
        v
Murex Trade Capture
        |
        v
Validation
        |
        v
Enrichment
        |
        v
Workflow
        |
        v
Market Data
        |
        v
Valuation
        |
        v
Risk / P&L
        |
        v
Confirmation
        |
        v
Settlement
        |
        v
Accounting
        |
        v
DataMart / Reporting

This flow will become much more detailed as we progress through the Murex course.


---

2. BUY SIDE VS SELL SIDE

2.1 What is Buy Side?

Definition

The Buy Side broadly consists of institutions whose primary activities involve investing capital, managing portfolios, or managing their own financial exposures.

Examples

Asset Management Companies

Mutual Funds

Pension Funds

Insurance Companies

Hedge Funds

Sovereign Wealth Funds

Corporate Treasury


Simple Memory

> BUY SIDE = INVEST / MANAGE




---

2.2 Buy Side Example

Suppose a Mutual Fund has:

₹500 Crore

It wants to invest the money.

It may invest in:

Government Bonds

Corporate Bonds

Equity

Other financial instruments


Mutual Fund
     |
     | Investment Money
     v
Financial Market
     |
     +----> Bonds
     |
     +----> Equity
     |
     +----> Other Products

The Mutual Fund is acting as a Buy-Side participant.


---

2.3 What is Sell Side?

Definition

The Sell Side broadly consists of institutions that provide financial products, pricing, liquidity, execution, financing, and related market services.

Examples

Investment Banks

Banks

Broker-Dealers

Securities Firms

Market Makers


Simple Memory

> SELL SIDE = PROVIDE



Think:

Product + Pricing + Liquidity + Execution


---

2.4 Sell Side Example

Suppose a corporate needs an FX hedge.

It approaches a bank.

Corporate
     |
     | Needs FX Hedge
     v
Bank
     |
     +----> Provides Price
     |
     +----> Provides Product
     |
     +----> Executes Trade
     |
     +----> Manages Risk
     |
     +----> Settles Trade

The bank is acting as the Sell Side.


---

2.5 Buy Side vs Sell Side

Buy Side	Sell Side

Invests/manages money or exposure	Provides financial products/services
Manages portfolios	Provides pricing
Takes investment positions	Provides liquidity
Manages investment/hedging requirements	Provides execution
Examples: Mutual Funds, Asset Managers	Examples: Banks, Investment Banks, Brokers



---

2.6 Important Interview Point

Do NOT think:

BUY = BUY SIDE
SELL = SELL SIDE

This is incorrect.

Buy Side/Sell Side describes the role/business model of the institution, not simply whether that institution bought or sold something in a particular trade.

Example

Bank A buys USD from Bank B.

Bank A does not automatically become Buy Side.

A bank can be a Sell-Side institution and still:

Buy

Sell

Hedge

Trade

Manage positions



---

2.7 Corporate Treasury

Corporate Treasury manages the financial exposures of a company.

For example:

Corporate
    |
    +----> FX Exposure
    |
    +----> Interest Rate Exposure
    |
    +----> Commodity Exposure
    |
    v
Risk Management / Hedging
    |
    v
Bank

A corporate may approach a bank to hedge its exposure.


---

2.8 Client vs Counterparty — Introduction

Suppose:

Corporate A <-----> Bank B

The corporate may be the bank's:

> Client



For the specific trade, the corporate is also a:

> Counterparty



We will study Counterparties, Legal Entities and Static Data separately later.


---

2.9 Buy Side / Sell Side in Murex

Imagine a bank using Murex.

A corporate requests an FX transaction.

Corporate
     |
     | FX Requirement
     v
Bank FX Trader
     |
     v
Murex
     |
     +----> Trade Capture
     |
     +----> Validation
     |
     +----> Enrichment
     |
     +----> Workflow
     |
     +----> Valuation
     |
     +----> Risk
     |
     +----> P&L
     |
     +----> Confirmation
     |
     +----> Settlement

This is why understanding market participants matters in Murex.


---

3. ASSET CLASSES

3.1 What is an Asset Class?

Definition

An Asset Class is a broad category of financial instruments with similar underlying exposures, characteristics, market behavior, and risk drivers.

Simple Meaning

> Asset Class tells us what broad type of financial exposure/market we are dealing with.




---

3.2 Major Asset Classes

For our Murex learning, focus on:

FX
Rates
Fixed Income / Debt
Equity
Credit
Commodity

Memory:

> F R F E C C




---

3.3 FX

Meaning

Foreign Exchange.

It deals with currencies.

Examples:

EUR/USD

USD/INR

GBP/USD

USD/JPY

EUR/INR


Common Products

FX Spot

FX Forward

FX Swap

FX Option

NDF


Main Risk

> FX / Currency Risk



Example

Indian Company
      |
      | Needs EUR
      v
EUR/INR Exposure
      |
      v
FX Risk
      |
      v
FX Hedge


---

3.4 Rates

Rates primarily deals with:

> Interest rates and interest-rate exposure.



Examples:

Interest Rate Swap

FRA

Swaption

Cap

Floor


Example

A company has floating-rate borrowing.

If interest rates increase, its interest expense may increase.

It may use an Interest Rate Swap to manage the exposure.

Company
   |
   v
Floating Rate Exposure
   |
   v
Interest Rate Risk
   |
   v
Interest Rate Swap

Important Market Data

Interest-rate curves

Yield curves

Discount curves

Forward curves



---

3.5 Fixed Income / Debt

Fixed Income mainly refers to debt instruments that generate contractual cashflows.

Examples:

Government Bonds

Corporate Bonds


Bond Example

Face Value = ₹100 Crore
Coupon = 7%
Maturity = 10 Years

A bond's market value can change because of:

Interest rates

Credit quality

Credit spreads

Liquidity

Time to maturity


Simple Bond Flow

Government / Company
        |
        | Borrow Money
        v
       Bond
        |
        v
     Investor


---

3.6 Equity

Equity represents ownership or exposure to equity prices.

Examples:

Shares

Equity Futures

Equity Options

Equity Swaps


Example

An investment fund owns shares.

If the share price changes:

Equity Price
     |
     v
Position Value
     |
     v
P&L

Main Risk

> Equity Price Risk




---

3.7 Credit

Credit is related to:

> Creditworthiness, default risk, and credit-spread exposure.



Examples:

Corporate Bonds

Credit Default Swaps (CDS)

Credit-linked products


Example

An investor owns exposure to Company ABC.

The investor is worried about default.

A CDS can be used to manage/transfer credit risk.

Investor
    |
    | Credit Exposure
    v
Company ABC
    |
    v
Credit / Default Risk
    |
    v
CDS / Credit Protection

Main Risks

Default Risk

Credit Spread Risk

Counterparty Risk



---

3.8 Commodity

Commodities are physical/raw materials and financial products linked to them.

Examples:

Crude Oil

Natural Gas

Gold

Silver

Copper

Electricity

Agricultural Commodities


Example

An airline needs fuel.

If oil prices increase:

Oil Price ↑
     |
     v
Fuel Cost ↑
     |
     v
Airline Risk
     |
     v
Commodity Hedge

Main Risk

> Commodity Price Risk




---

3.9 Asset Class vs Product vs Trade

This is one of the most important concepts.

Example: EUR/INR FX Forward

Asset Class

> FX



Product

> FX Forward



Trade

> A specific EUR/INR Forward contract between Corporate and Bank.



Asset Class
     |
     v
FX
     |
     v
Product
     |
     v
FX Forward
     |
     v
Specific Trade
     |
     v
Corporate <-----> Bank


---

3.10 Another Example — Rates

Asset Class
     |
     v
Rates
     |
     v
Product
     |
     v
Interest Rate Swap
     |
     v
Specific Trade
     |
     v
Company <-----> Bank


---

3.11 Another Example — Equity

Asset Class
     |
     v
Equity
     |
     v
Product
     |
     v
Equity Option
     |
     v
Specific Trade


---

3.12 Asset Class vs Derivative Classification

Do not confuse these two classification methods.

Asset Class Classification

Tells us the market/underlying exposure:

FX
Rates
Equity
Credit
Commodity

Instrument Nature

Tells us what type of instrument it is:

Cash
Forward
Future
Option
Swap

Therefore:

> FX Forward = FX asset class + Derivative



And:

> Equity Option = Equity asset class + Derivative




---

3.13 Asset Class and Risk

Different asset classes have different major risk drivers.

Asset Class	Major Risk

FX	FX / Currency Risk
Rates	Interest Rate Risk
Fixed Income	Interest Rate + Credit + Liquidity Risk
Equity	Equity Price Risk
Credit	Default + Credit Spread Risk
Commodity	Commodity Price Risk



---

3.14 Asset Class and Market Data

Different products require different market data.

FX

Examples:

EUR/INR
USD/INR
EUR/USD

Rates

Examples:

Interest Rates
Yield Curves
Discount Curves
Forward Curves

Equity

Examples:

Share Prices
Index Levels
Volatility

Credit

Examples:

Credit Spreads
Credit Curves
Default-related assumptions

Commodity

Examples:

Oil Prices
Gold Prices
Gas Prices
Commodity Forward Curves

This becomes important later when we study Market Data and Murex valuation problems.


---

3.15 Asset Class and Murex Production Support

Understanding the asset class helps us identify where to investigate.

Issue:

> "EUR/INR Forward valuation is incorrect."



Think:

FX
  |
  v
FX Forward
  |
  v
FX Market Data
  |
  v
Pricing / Valuation
  |
  v
Risk / P&L


---

Issue:

> "IRS valuation changed unexpectedly."



Think:

Rates
  |
  v
Interest Rate Swap
  |
  v
Interest Rate Curves
  |
  v
Pricing / Valuation
  |
  v
Risk / P&L


---

Issue:

> "CDS P&L is incorrect."



Think:

Credit
  |
  v
CDS
  |
  v
Credit Spread / Curve
  |
  v
Valuation
  |
  v
P&L

This is the type of thinking we will develop for Production Support.


---

4. KEY DEFINITIONS — DAY 1

Financial Market

An ecosystem where participants trade, invest, finance, and manage financial assets and risks.

Buy Side

Institutions primarily investing/managing capital, portfolios, or financial exposures.

Sell Side

Institutions providing financial products, pricing, liquidity, execution and related services.

Asset Class

A broad category of financial instruments with similar underlying exposures and risk drivers.

Product

A specific financial instrument offered/traded in a market.

Trade

A specific transaction between parties with defined terms.

FX

Foreign Exchange; trading/exchange of currencies.

Rates

Market/instruments related primarily to interest rates.

Fixed Income

Debt instruments with contractual cashflows.

Equity

Ownership/share-price exposure.

Credit

Exposure related to creditworthiness, default and credit spreads.

Commodity

Physical/raw-material exposure and related financial products.


---

5. QUICK RECALL

Financial Market

Remember:

> CAPITAL + INVESTMENT + LIQUIDITY + PRICE + RISK




---

Buy Side

Remember:

> INVEST / MANAGE



Examples:

Asset Manager
Mutual Fund
Pension Fund
Insurance
Hedge Fund
Corporate Treasury


---

Sell Side

Remember:

> PROVIDE



Think:

Product
Pricing
Liquidity
Execution

Examples:

Bank
Investment Bank
Broker
Market Maker


---

Asset Classes

Remember:

> F R F E C C



F = FX
R = Rates
F = Fixed Income
E = Equity
C = Credit
C = Commodity


---

Market → Product → Trade

Remember:

FX Market
    |
    v
FX Forward
    |
    v
EUR/INR Forward Trade


---

6. MUREX MENTAL MODEL

This is the most important diagram from today's lesson.

FINANCIAL MARKET
                           |
                           v
                      ASSET CLASS
                           |
                           v
                         PRODUCT
                           |
                           v
                          TRADE
                           |
                           v
                         MUREX
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
       Trading          Risk / P&L       Settlement
          |                |                |
          +----------------+----------------+
                           |
                           v
                    Accounting / Data
                           |
                           v
                    DataMart / Reporting
                           |
                           v
                  Production Support


---

7. DAY 1 MASTER MEMORY MAP

CAPITAL MARKETS
      |
      +----> Financial Markets
      |          |
      |          +----> Funding
      |          +----> Investment
      |          +----> Liquidity
      |          +----> Price Discovery
      |          +----> Risk Management
      |          +----> Risk Transfer
      |
      +----> Participants
      |          |
      |          +----> Buy Side
      |          +----> Sell Side
      |
      +----> Asset Classes
                 |
                 +----> FX
                 +----> Rates
                 +----> Fixed Income
                 +----> Equity
                 +----> Credit
                 +----> Commodity
                            |
                            v
                         PRODUCTS
                            |
                            v
                          TRADES
                            |
                            v
                          MUREX


---

8. FULL END-TO-END STORY

🏭 Indian Manufacturer — EUR 10 Million Requirement

Indian Manufacturer
        |
        | Needs machinery from Germany
        |
        v
German Supplier
        |
        | Requires EUR 10M
        |
        v
Business Requirement
        |
        | "We need EUR 10M after 3 months."
        |
        v
FX Exposure
        |
        | Company earns mainly INR
        |
        v
FX Risk
        |
        | EUR may become more expensive
        |
        v
Financial Market
        |
        v
FX Market
        |
        v
Asset Class
        |
        v
FX
        |
        v
Hedging Requirement
        |
        v
Product
        |
        v
FX Forward
        |
        v
Sell Side Bank
        |
        | Provides price / liquidity / execution
        |
        v
Trade
        |
        | Corporate <-----> Bank
        | EUR 10M
        | Agreed forward rate
        | Future settlement date
        |
        v
Murex Trade Capture
        |
        v
Validation
        |
        v
Enrichment
        |
        v
Workflow
        |
        v
Market Data
        |
        v
Pricing / Valuation
        |
        v
Risk
        |
        v
P&L
        |
        v
Confirmation
        |
        v
Settlement
        |
        v
Accounting
        |
        v
DataMart
        |
        v
Reporting
        |
        v
Production Support
        |
        v
Monitoring / Logs / SQL / Linux / Batch / Interfaces


---

9. BUSINESS → FUNCTIONAL → TECHNICAL STORY

Business

Corporate needs EUR 10M
after 3 months.

↓

Risk

EUR/INR may move.

↓

Functional Solution

Use an EUR/INR FX Forward
to manage the exposure.

↓

Murex Functional Process

Capture
→ Validate
→ Enrich
→ Workflow
→ Value
→ Risk/P&L
→ Confirm
→ Settle
→ Account
→ Report

↓

Technical Layer

API / MxML / XML / JSON
        |
        v
Murex
        |
        v
Processing
        |
        v
Database
        |
        v
Risk / P&L
        |
        v
DataMart
        |
        v
Reporting

↓

Production Support

Issue
   |
   v
Business Impact
   |
   v
Identify Module
   |
   v
Check Trade
   |
   v
Check Workflow
   |
   v
Check Logs
   |
   v
Check Interface
   |
   v
Check Database
   |
   v
Find Root Cause
   |
   v
Fix / Workaround
   |
   v
Validate


---

10. DAY 1 — FINAL TAKEAWAYS

If you remember only these points today, that is enough:

1.

> Financial Markets connect participants who need funding, want to invest, or need to manage financial risk.



2.

> Buy Side mainly invests/manages money or exposure.



3.

> Sell Side mainly provides products, pricing, liquidity and execution.



4.

> Asset Class tells us the broad type of financial exposure/market.



5.

> Market → Product → Trade



Example:

FX Market
   |
   v
FX Forward
   |
   v
EUR/INR Forward Trade

6.

> Different asset classes have different products, market data, pricing, risks and settlement processes.



7.

> Murex connects the business transaction to trading, processing, risk, P&L, settlement, accounting and reporting.




---

📌 DAY 1 PROGRESS

Chapter 1 — Capital Markets Foundation

[x] Capital Markets Overview

[x] Buy Side / Sell Side

[x] Asset Classes

[ ] Cash vs Derivatives

[ ] OTC vs Exchange Traded

[ ] Trading Venues

[ ] Market Participants

[ ] Trade Terminology

[ ] Trade Date / Value Date / Maturity

[ ] Notional / Price / Rate / Quantity

[ ] Books / Portfolios / Desks

[ ] Counterparties

[ ] Legal Entities


Status

Day 1 — 3 major topics completed ✅

Next Lesson: Cash Instruments vs Derivatives

### How to use these notes today

Don't repeatedly read the whole Markdown file. Do this:

**1st reading:** Read the full notes slowly.  
**2nd reading:** Read only the **Quick Recall + Memory Map**.  
**3rd step:** Close Git and explain the **full dotted-line story** aloud from memory.

If you can reconstruct:

**Business → FX Risk → FX Market → FX → FX Forward → Trade → Murex → Risk/P&L → Settlement → Accounting → DataMart → Production Support**

without looking, you've started converting recognition into **recall**.

Glossary:
#########
# Murex Techno-Functional — Day 1
# Terms Glossary

---

## 1. Capital Markets

| Term | Simple Meaning |
|---|---|
| Financial Market | Ecosystem where financial assets, money and risk are traded, funded, invested or managed. |
| Capital Market | Market used mainly for raising and investing long-term capital. |
| Money Market | Market for short-term borrowing, lending and funding. |
| FX Market | Market where currencies are traded against each other. |
| Equity Market | Market where shares/stocks are issued and traded. |
| Debt Market | Market where debt instruments such as bonds are issued and traded. |
| Derivatives Market | Market where contracts derive their value from an underlying asset, rate, currency or index. |
| Liquidity | How easily an asset can be bought or sold without significantly affecting its price. |
| Price Discovery | Process through which market participants determine the market price. |
| Risk Management | Identifying, measuring, monitoring and controlling financial risks. |
| Risk Transfer | Moving financial risk from one party to another, often using derivatives. |
| Capital Raising | Obtaining money for business or investment purposes. |

---

## 2. Market Participants

| Term | Simple Meaning |
|---|---|
| Market Participant | Any entity that participates in financial markets. |
| Bank | Financial institution providing banking, financing, trading and other financial services. |
| Investment Bank | Bank involved in capital markets, trading, financing and advisory activities. |
| Commercial Bank | Bank mainly providing deposits, loans, payments and traditional banking services. |
| Corporate | Business/company participating in financial markets for funding, investment or hedging. |
| Asset Manager | Institution managing investments on behalf of clients/investors. |
| Hedge Fund | Investment fund using specialized investment/trading strategies. |
| Pension Fund | Institution managing retirement assets. |
| Insurance Company | Institution providing insurance and managing/investing collected premiums. |
| Sovereign Wealth Fund | Government-owned investment fund managing state assets. |
| Central Bank | Institution responsible for monetary policy and other central banking functions. |
| Broker | Intermediary helping clients execute transactions. |
| Market Maker | Participant providing buy/sell prices and liquidity. |

---

## 3. Buy Side

| Term | Simple Meaning |
|---|---|
| Buy Side | Institutions mainly investing or managing capital, portfolios or exposures. |
| Asset Manager | Institution managing investments for clients. |
| Mutual Fund | Investment vehicle pooling money from investors to invest in assets. |
| Pension Fund | Fund managing retirement investments. |
| Hedge Fund | Investment fund using specialized strategies. |
| Corporate Treasury | Company function managing cash, funding, liquidity and financial exposures. |
| Portfolio | Collection of financial positions/investments managed together. |

### Important

Buy Side does NOT mean the institution is buying something in every trade.

A bank can buy USD in an FX trade and still be a Sell-Side institution.

---

## 4. Sell Side

| Term | Simple Meaning |
|---|---|
| Sell Side | Institutions providing financial products, pricing, liquidity, execution and related services. |
| Investment Bank | Major Sell-Side participant providing trading, financing and advisory services. |
| Dealer | Institution/person that trades financial products and often provides prices to clients. |
| Market Maker | Provides bid/offer prices and liquidity. |
| Liquidity Provider | Participant providing the ability for others to transact. |
| Execution | Completing a financial transaction. |
| Pricing | Determining the price/rate at which a product can be traded. |

---

## 5. Asset Classes

### Six Important Murex Asset Classes

| Asset Class | Meaning | Examples |
|---|---|---|
| FX | Currency exposure | FX Spot, Forward, Swap, Option |
| Rates | Interest-rate exposure | IRS, FRA, Cap, Floor, Swaption |
| Fixed Income / Debt | Debt instruments and cash flows | Government Bond, Corporate Bond |
| Equity | Ownership/share-price exposure | Equity, Equity Option, Equity Future |
| Credit | Credit/default/spread exposure | CDS, Credit Products |
| Commodity | Commodity-price exposure | Oil, Gold, Gas, Copper |

### Memory Trick

**F → R → F → E → C → C**

FX → Rates → Fixed Income → Equity → Credit → Commodities

---

## 6. FX Terms

| Term | Simple Meaning |
|---|---|
| Currency | Money issued by a country or monetary authority. |
| Currency Pair | Two currencies quoted against each other, e.g. EUR/INR. |
| Base Currency | First currency in a currency pair. |
| Quote Currency | Second currency in a currency pair. |
| FX Spot | Exchange of currencies with near-term settlement. |
| FX Forward | Agreement today to exchange currencies at a future date at an agreed rate. |
| FX Swap | Combination of two FX transactions with different settlement dates. |
| FX Option | Contract giving the holder a right, but generally not an obligation, to buy/sell currency. |
| NDF | Non-Deliverable Forward; generally settled financially instead of physical currency delivery. |
| FX Risk | Risk caused by changes in currency exchange rates. |

### Example

EUR/INR = 90

Means:

**1 EUR = ₹90**

---

## 7. Rates Terms

| Term | Simple Meaning |
|---|---|
| Interest Rate | Cost of borrowing money or return earned from lending/investing money. |
| Interest Rate Swap (IRS) | Derivative where parties exchange interest-payment streams. |
| FRA | Forward Rate Agreement; contract that locks an interest rate for a future period. |
| Cap | Derivative providing protection against an interest rate rising above a specified level. |
| Floor | Derivative providing protection against an interest rate falling below a specified level. |
| Swaption | Option giving the right to enter into an interest-rate swap. |
| Yield Curve | Relationship between interest rates/yields and different maturities. |
| Discount Curve | Curve used to calculate the present value of future cash flows. |
| Forward Curve | Curve representing implied future rates/prices for different maturities. |

---

## 8. Fixed Income / Debt

| Term | Simple Meaning |
|---|---|
| Bond | Debt instrument through which an issuer borrows money from investors. |
| Issuer | Entity issuing a financial instrument. |
| Investor | Party investing money in a financial instrument. |
| Coupon | Periodic interest payment on a bond. |
| Maturity | Date when the instrument reaches its contractual end. |
| Principal | Original/contractual amount associated with a debt instrument. |
| Yield | Return/yield measure associated with a debt investment. |
| Government Bond | Debt issued by a government. |
| Corporate Bond | Debt issued by a company. |

---

## 9. Trade Terminology

| Term | Simple Meaning |
|---|---|
| Trade | Specific transaction between parties involving a financial product. |
| Trade Date | Date on which the trade is agreed/booked. |
| Value Date | Date on which settlement/exchange of value occurs. |
| Maturity Date | Contractual end date of a trade. |
| Notional | Contractual reference amount used to determine payments/exposure. |
| Price | Monetary value or quoted price of an instrument. |
| Rate | Agreed or market rate used in a financial transaction. |
| Quantity | Number/amount of units of an asset or instrument. |
| Position | Current financial holding or exposure resulting from trades. |
| Exposure | Amount of financial risk or economic sensitivity a party has. |
| Counterparty | Other party involved in a transaction. |

---

## 10. Market → Asset Class → Product → Trade

This is one of the most important concepts.

```text
Financial Market
      ↓
FX Market
      ↓
FX Asset Class
      ↓
FX Forward Product
      ↓
Specific Trade
      ↓
Corporate ↔ Bank
      ↓
EUR/INR Forward

Example

Market       → FX Market
Asset Class  → FX
Product      → FX Forward
Trade        → ABC Ltd buys EUR 10M from XYZ Bank


---

11. OTC vs Exchange-Traded

Term	Simple Meaning

OTC	Over-The-Counter; trade negotiated directly between counterparties or through dealer/intermediary infrastructure.
Exchange-Traded	Instrument traded through an organized exchange.
Standardized Contract	Contract with predefined specifications.
Bilateral	Agreement directly between two parties.
Central Counterparty (CCP)	Entity that can stand between trading parties for clearing and risk management.
Clearing	Process of determining obligations between trading parties before settlement.
Settlement	Actual exchange/payment of money, securities, currencies or other obligations.



---

12. Books, Portfolios & Desks

Term	Simple Meaning

Trading Desk	Business unit/team responsible for trading a particular product or market.
Book	Collection of trades/positions managed together.
Portfolio	Collection of financial positions managed as a group.
Position	Net exposure resulting from one or more trades.
Desk	Organizational/business unit responsible for specific trading activity.
P&L	Profit and Loss generated by trades/positions.


Simple Relationship

Bank
  ↓
Trading Division
  ↓
Trading Desk
  ↓
Book / Portfolio
  ↓
Trades
  ↓
Positions
  ↓
Risk + P&L


---

13. Counterparty & Legal Entity

Term	Simple Meaning

Counterparty	Party on the opposite side of a transaction.
Legal Entity	Legally recognized organization that can enter into contracts.
Client	Party receiving services/products from another institution.
Issuer	Entity issuing a financial instrument.
Beneficiary	Party entitled to receive a payment or benefit.
Settlement Account	Account used for settlement-related cash movements.
Legal Entity Hierarchy	Organizational structure connecting related legal entities.


Example

ABC Manufacturing
       ↕
   FX Forward
       ↕
XYZ Bank Ltd

For this trade:

ABC Manufacturing → Counterparty to XYZ Bank
XYZ Bank           → Counterparty to ABC Manufacturing


---

14. Murex Terms Introduced Today

Term	Simple Meaning

Murex MX.3	Platform used by financial institutions for trading, risk, operations, finance and related activities.
Trade Capture	Recording a financial transaction in the system.
Validation	Checking whether trade information is valid and complete.
Enrichment	Adding required information to a trade.
Workflow	Defined sequence of processing steps.
Market Data	Financial information such as FX rates, interest rates, curves, prices and volatility.
Pricing / Valuation	Determining the current value or price of a trade/position.
Risk	Measurement of potential financial impact from risk factors.
P&L	Profit and Loss generated by trades/positions.
Confirmation	Formal confirmation of trade details between parties.
Settlement	Completion of contractual payment/exchange obligations.
Accounting	Recording financial impacts in accounting books/systems.
DataMart	Structured data environment used for analysis and reporting.
Reporting	Producing business, risk, regulatory or operational information.



---

15. Master Memory Map

CAPITAL MARKETS
       ↓
MARKETS
       ↓
FX / RATES / EQUITY / DEBT / CREDIT / COMMODITIES
       ↓
ASSET CLASS
       ↓
PRODUCT
       ↓
TRADE
       ↓
COUNTERPARTIES
       ↓
BOOK / PORTFOLIO
       ↓
POSITION
       ↓
MARKET DATA
       ↓
PRICING / VALUATION
       ↓
RISK
       ↓
P&L
       ↓
CONFIRMATION
       ↓
SETTLEMENT
       ↓
ACCOUNTING
       ↓
DATAMART
       ↓
REPORTING


---

⭐ 15 Terms to Remember Today

1. Financial Market


2. Buy Side


3. Sell Side


4. Asset Class


5. FX


6. Rates


7. Product


8. Trade


9. Counterparty


10. Notional


11. Trade Date


12. Value Date


13. Maturity Date


14. Book / Portfolio


15. Position




---

🧠 One-Line Memory

Market → Asset Class → Product → Trade → Counterparty
→ Book → Position → Market Data → Valuation → Risk → P&L
→ Confirmation → Settlement → Accounting → DataMart → Reporting

End of Day 1 Glossary
