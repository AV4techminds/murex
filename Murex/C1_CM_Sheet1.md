Absolutely. In fact, I **highly recommend** adding a one-page **Quick Recall / Cheat Sheet** at the end of every chapter. It will be extremely useful for your morning revision and interview preparation.

For Git, you can create:

`01-capital-markets-foundation/quick-recall.md`

Here is today's version:

````markdown
# 🧠 Capital Markets Foundation — Quick Recall

> Day 01 | Murex Techno-Functional

---

## 🟦 1. Financial Market

**Financial Market =** Ecosystem where financial assets, instruments, capital and risks are exchanged.

### Main Purposes

💰 Capital Raising  
📈 Investment  
💳 Borrowing / Lending  
💧 Liquidity  
🎯 Price Discovery  
🛡️ Risk Management  
🔄 Risk Transfer  
🌍 Currency Exchange  

---

## 🟩 2. Major Financial Markets

| Market | Think About |
|---|---|
| 💵 Money Market | Short-term funding |
| 🏦 Capital Market | Long-term funding/investment |
| 💱 FX Market | Currency exchange |
| 📊 Equity Market | Ownership / Shares |
| 💰 Debt Market | Bonds / Borrowing |
| 🔄 Derivatives Market | Risk / Underlying |
| 🛢️ Commodity Market | Oil / Gold / Metals |
| 🛡️ Credit Market | Credit / Default Risk |
| 📈 Interest-Rate Market | Rates / Funding / Hedging |

---

## 🟨 3. Capital Market

### Remember

**Capital Market = Longer-term capital**

```text
Capital Market
      |
      +---- Equity
      |       └── Shares
      |
      +---- Debt
      |       ├── Government Bonds
      |       └── Corporate Bonds
      |
      └---- Related Derivatives
````

---

## 🟧 4. Primary vs Secondary Market

### Primary Market

🆕 **NEW SECURITY**

Issuer → Investor

💰 Money goes to issuer.

### Secondary Market

🔄 **EXISTING SECURITY**

Investor A ↔ Investor B

💰 Money normally goes to selling investor.

### Easy Memory

> **Primary = New Issue**
> **Secondary = Existing Security Trading**

---

## 🟥 5. Cash vs Derivative

### Cash Instrument

Value comes directly from the underlying financial asset/security.

Examples:

* Share
* Bond
* Currency

### Derivative

Value is derived from an underlying.

Examples:

* Forward
* Future
* Option
* Swap

```text
Underlying
    ↓
Derivative
```

---

## 🟪 6. OTC vs Exchange

### OTC

**Over-The-Counter**

Counterparty ↔ Counterparty

✔ Flexible
✔ Can be customized
✔ Common in FX and many derivatives

### Exchange-Traded

Exchange ↔ Participants

✔ Standardized
✔ Organized exchange
✔ Exchange rules
✔ Clearing arrangements

### Memory

> **OTC = Flexible**
> **Exchange = Standardized**

---

# 💱 7. FX — Most Important Example

### Business Requirement

🇮🇳 Indian Company needs to pay:

**EUR 10M**

to 🇩🇪 German Supplier.

---

### Exposure

Future EUR obligation.

```text
Need EUR
   ↓
EUR Exposure
```

---

### Risk

EUR/INR may increase.

```text
EUR/INR ₹90
     ↓
EUR/INR ₹95
     ↓
More INR required
```

---

### Current Rate

**EUR/INR = ₹90**

EUR 10M:

**€10M × ₹90 = ₹90 Crore**

---

### Future Rate

**EUR/INR = ₹95**

€10M:

**€10M × ₹95 = ₹95 Crore**

### Difference

**₹5 Crore additional INR requirement**

---

# 🛡️ 8. Hedging

### Definition

**Hedging = Managing/reducing the impact of an existing financial exposure.**

```text
Business Requirement
        ↓
Exposure
        ↓
Risk
        ↓
Hedge
```

### Possible Hedge

💱 **FX Forward**

Company ↔ Bank

---

# ⭐ 9. Payment vs Hedge

### Underlying Payment

Company → German Supplier

**Purpose:** Pay for machinery/services.

### Hedge

Company → Bank

**Purpose:** Manage FX risk.

> ⚠️ **Hedge ≠ Underlying Payment**

---

# 🧩 10. Market vs Instrument vs Trade

### Market

Where financial activity happens.

Example:

**FX Market**

↓

### Instrument

Financial product/contract.

Example:

**EUR/USD Forward**

↓

### Trade

Actual transaction.

Example:

**Company ↔ Bank**

### Remember

```text
MARKET
   ↓
INSTRUMENT
   ↓
TRADE
```

---

# 👥 11. Important Participants

🏦 Banks
🏢 Corporates
📈 Asset Managers
💼 Hedge Funds
🏛️ Governments
🏦 Central Banks
🤝 Brokers
🔄 Exchanges
⚖️ CCPs / Clearing Organizations
🔐 Custodians

---

# 🏢 12. Buy Side vs Sell Side

### Buy Side

Primarily manages/invests capital.

Examples:

* Asset Managers
* Pension Funds
* Hedge Funds
* Investment Funds

### Sell Side

Primarily provides financial products, liquidity, execution and market services.

Examples:

* Investment Banks
* Banks
* Broker-Dealers

> Detailed Buy Side vs Sell Side → **Next Topic**

---

# 🔄 13. High-Level Trade Lifecycle

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

---

# 🚀 14. Murex Mental Model

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
SETTLEMENT
      ↓
ACCOUNTING
      ↓
DATAMART
      ↓
REPORTING
```

---

# 💻 15. Techno-Functional Mapping

| Business        | Functional            | Technical              |
| --------------- | --------------------- | ---------------------- |
| Need to pay EUR | FX transaction        | Trade capture          |
| FX exposure     | Hedge                 | Murex processing       |
| FX risk         | Valuation / Risk      | Risk engine            |
| Trade           | Lifecycle             | Integration            |
| Settlement      | Settlement processing | Interfaces / Jobs      |
| Reporting       | Business reports      | Datamart / SQL         |
| Operations      | Production support    | Linux / Shell / Python |

---

# 🎯 16. The Golden Chain

### Remember this for Murex interviews:

```text
WHY?
 ↓
BUSINESS REQUIREMENT
 ↓
WHAT?
 ↓
FINANCIAL INSTRUMENT
 ↓
TRADE
 ↓
HOW?
 ↓
FUNCTIONAL PROCESS
 ↓
MUREX
 ↓
TECHNICAL PROCESS
 ↓
RISK / P&L
 ↓
SETTLEMENT
 ↓
ACCOUNTING
 ↓
DATAMART / REPORTING
```

---

# 🧠 17. 10-Second Revision

If someone asks:

### What did you learn today?

Say:

> "I learned the foundation of financial and capital markets, including major market types, participants, instruments, primary and secondary markets, OTC and exchange-traded markets. I also understood FX exposure, FX risk and hedging through an end-to-end corporate FX example, and mapped the business requirement to the functional trade lifecycle and high-level Murex processing."

---

# 🎤 18. Interview Rapid Fire

**Q:** What is a financial market?
**A:** Ecosystem for exchanging financial assets, instruments, capital and risks.

**Q:** Capital market?
**A:** Primarily longer-term financing, investment and trading.

**Q:** Money market?
**A:** Short-term funding and instruments.

**Q:** Primary market?
**A:** New securities are issued.

**Q:** Secondary market?
**A:** Existing securities are traded.

**Q:** FX market?
**A:** Market for exchanging currencies.

**Q:** FX risk?
**A:** Risk from exchange-rate movements.

**Q:** Hedging?
**A:** Managing/reducing the impact of an existing exposure.

**Q:** Derivative?
**A:** Contract whose value derives from an underlying.

**Q:** OTC?
**A:** Over-The-Counter bilateral trading arrangement.

**Q:** Trade?
**A:** Actual transaction between counterparties.

**Q:** Why Murex?
**A:** To support processing of financial transactions and related functions such as trading, valuation, risk, P&L, operations, settlement, accounting and reporting.

---

# 🏆 FINAL MEMORY MAP

```text
                FINANCIAL MARKETS
                       │
        ┌──────────────┼──────────────┐
        │              │              │
      MONEY         CAPITAL           FX
      MARKET        MARKET           MARKET
                     │
                ┌────┴────┐
                │         │
             EQUITY      DEBT
                │         │
                └────┬────┘
                     │
                DERIVATIVES
                     │
                     ↓
                 TRADING
                     ↓
                   TRADE
                     ↓
                  MUREX
                     ↓
        ┌────────────┼────────────┐
        ↓            ↓            ↓
      RISK          P&L       OPERATIONS
                                   ↓
                              SETTLEMENT
                                   ↓
                              ACCOUNTING
                                   ↓
                              DATAMART
                                   ↓
                               REPORTING
```

---

## 🔑 Three things to remember from Day 01

> **1. Business Requirement:**
> "I need to solve a financial/business problem."

> **2. Financial Solution:**
> "Which market + instrument + trade can solve/manage it?"

> **3. Murex Solution:**
> "How does the bank capture, process, value, manage risk, settle and report that trade?"

```

**Yes—keep this as a separate `quick-recall.md`.** For every future Murex chapter, I'll prepare the same three-part structure:

**📘 Detailed Notes → 🧪 Hands-on/Business Scenario → 🧠 One-page Quick Recall**

That will make your Git repository useful both for **deep learning now** and **10-minute interview revision later**.
```
