
# Murex Techno-Functional Learning
### Date: 22-July-2026
##############################
Phase 5 – Risk Management
##############################
 Risk Introduction
 Types of Risk
 Market Risk Basics
 Credit Risk Basics
 Liquidity Risk Basics
 Operational Risk Basics
 Risk Appetite
 Risk Tolerance
 Temporary Exposure
 Permanent Exposure
 Hedging
 Production Support Perspective
 FX Risk
 Interest Rate Risk
 Equity Risk
 Commodity Risk
 Counterparty Credit Risk
 Settlement Risk
 Country Risk
 Concentration Risk
 VaR (Value at Risk)
 Stress Testing
 Scenario Analysis
 Limit Monitoring
 Risk Engine
 Risk Reports
 Risk Workflow
 Risk Investigation
 Risk Production Issues
---

# Chapter 1: What is Risk?

## Definition

**Risk is the possibility that actual outcomes differ from expected outcomes, resulting in potential financial loss or other negative impacts.**

### Important Points

* Risk does **not** mean that a loss has already occurred.
* It represents the **possibility** of loss.
* Every financial transaction carries some level of risk.
* Banks earn profits by taking **controlled risks**, not by avoiding all risks.

---

## Real-Life Example

Imagine you lend **₹10 lakhs** to a friend.

### Scenario 1

Your friend repays the loan on time.

**Result:** No financial loss.

### Scenario 2

Your friend cannot repay the loan.

**Result:** Financial loss.

The uncertainty before repayment is called **Risk**.

---

# Chapter 2: Why Do Banks Take Risk?

Banks exist to earn profits by providing financial services.

They intentionally take calculated risks through:

* Lending money
* Foreign Exchange trading
* Derivative trading
* Investments
* Market Making

**Important:** Banks do not try to eliminate all risk. They identify, measure, monitor, and control risk.

---

# Chapter 3: Running Example – ABC Motors FX Forward Trade

ABC Motors wants to purchase machinery from the USA.

Trade Details:

* Product: FX Forward
* Buy Currency: USD
* Sell Currency: INR
* Amount: USD 10 Million
* Agreed Forward Rate: 86.35

After the trade is booked, several risks arise.

---

# Chapter 4: Types of Risk After Trade Booking

## 1. Market Risk

### Definition

Market Risk is the possibility of financial loss due to changes in market prices.

Examples:

* Foreign Exchange rates
* Interest rates
* Equity prices
* Commodity prices

### Example

Forward Rate = 86.35

Market Rate becomes 88.50.

If the bank has not hedged the position, it may incur a loss due to adverse market movements.

---

## 2. Credit Risk

### Definition

Credit Risk is the possibility that the counterparty fails to fulfill its contractual obligations.

### Example

ABC Motors becomes bankrupt before settlement.

The bank may suffer a financial loss because the counterparty cannot pay.

---

## 3. Operational Risk

### Definition

Operational Risk arises due to failures in systems, processes, human activities, or external events.

Examples:

* Incorrect trade booking
* Wrong static data
* Batch failure
* Production issue
* Interface failure
* Market data loading failure

---

## 4. Liquidity Risk

### Definition

Liquidity Risk occurs when the bank cannot obtain sufficient cash or assets to settle its obligations on time.

Example:

The bank must deliver USD 10 Million tomorrow but does not have sufficient USD funds available.

---

# Chapter 5: Risk Management Process

Banks manage risk through four major activities.

1. Identify Risk
2. Measure Risk
3. Monitor Risk
4. Control Risk

This cycle continues throughout the trade lifecycle.

---

# Chapter 6: Risk Appetite

## Definition

Risk Appetite is the maximum level of risk that a bank is willing to accept in order to achieve its business objectives.

### Example

Risk Appetite = USD 50 Million

Current Exposure = USD 48 Million

The bank is still operating within its approved risk appetite.

---

# Chapter 7: Risk Tolerance

## Definition

Risk Tolerance represents the acceptable variation around the bank's approved risk appetite.

Example:

Risk Appetite = USD 50 Million

Risk Tolerance = ± USD 2 Million (example only; actual values depend on bank policy)

Risk Tolerance is defined by the bank's internal risk management framework.

---

# Chapter 8: Temporary Exposure

## Definition

Temporary Exposure occurs when exposure exceeds the approved limit for a short period, but there is a planned corrective action.

### Example

Risk Appetite = USD 50 Million

Current Exposure = USD 58 Million

The bank has already initiated an offsetting hedge that will reduce exposure shortly.

This is considered **Temporary Exposure**.

### Possible Actions

* Execute hedge trade
* Await trade settlement
* Obtain temporary management approval
* Continuously monitor exposure

---

# Chapter 9: Permanent Exposure

## Definition

Permanent Exposure occurs when exposure remains above approved limits for an extended period without corrective action.

### Example

Risk Appetite = USD 50 Million

Exposure remains at USD 58 Million for several days.

No hedge.

No approval.

No reduction.

This requires intervention from Risk Management and senior governance.

### Possible Actions

* Execute hedge trades
* Reduce positions
* Restrict new trades
* Seek formal approval to revise limits (if justified)

---

# Chapter 10: Hedging

## Definition

Hedging is the process of reducing market exposure by taking an offsetting position.

Example:

Current Exposure = +58 Million USD

Offsetting Trade = -8 Million USD

Final Net Exposure = +50 Million USD

**Objective:** Bring the bank's exposure back within its approved risk appetite.

---

# Chapter 11: Murex Perspective

Murex supports Risk Management by:

* Capturing trades
* Calculating positions
* Calculating exposures
* Monitoring risk limits
* Revaluing positions using market data
* Generating risk reports
* Alerting users when configured limits are breached

**Note:** Business approval decisions remain with the bank's Risk Management team; Murex enforces the configured rules.

---

# Chapter 12: Production Support Perspective

### Scenario

A trader reports:

> "I executed the hedge trade yesterday, but Murex still shows the exposure as USD 58 Million."

### Investigation Steps

1. Verify the hedge trade exists.
2. Confirm the trade is booked and validated.
3. Check the trade status and workflow.
4. Verify position aggregation completed successfully.
5. Check whether risk calculations completed successfully.
6. Verify market data availability.
7. Review application and batch logs.
8. Confirm whether the issue is technical or business-related.
9. Escalate to the functional or risk team if the system is functioning correctly but the business calculation requires review.

---

# Key Interview Questions

### Q1. What is Risk?

Risk is the possibility that actual outcomes differ from expected outcomes, resulting in potential financial loss.

---

### Q2. Why do banks take risk?

Banks take controlled risks to earn profits while managing those risks through governance and risk controls.

---

### Q3. What are the major risks after trade booking?

* Market Risk
* Credit Risk
* Operational Risk
* Liquidity Risk

---

### Q4. What is Risk Appetite?

The maximum level of risk a bank is willing to accept to achieve its business objectives.

---

### Q5. What is the difference between Temporary Exposure and Permanent Exposure?

| Temporary Exposure                 | Permanent Exposure                    |
| ---------------------------------- | ------------------------------------- |
| Short-term                         | Long-term                             |
| Planned corrective action exists   | No corrective action                  |
| Hedge or settlement expected       | Requires risk management intervention |
| Usually acceptable with monitoring | Requires escalation and mitigation    |

---

### Q6. What would you do if a trader says a hedge was executed but the exposure did not reduce?

* Verify hedge trade booking.
* Check trade processing.
* Validate position calculations.
* Verify risk engine execution.
* Check market data.
* Review logs.
* Determine whether it is a technical issue or a business issue.
* Escalate appropriately.

---

# Key Takeaways

* Risk is the possibility of loss, not the loss itself.
* Banks manage risk instead of avoiding it.
* The four major risk types are Market, Credit, Operational, and Liquidity Risk.
* Risk Appetite defines the maximum acceptable risk.
* Risk Tolerance defines the acceptable variation around that appetite.
* Temporary exposure is managed with planned corrective actions.
* Permanent exposure requires intervention.
* Hedging reduces market exposure through offsetting trades.
* Murex calculates and monitors exposure but does not make business decisions.
* Production Support verifies whether issues are technical or business-related before escalating.

*                     Investment Banking
                            │
                            ▼
                 Financial Markets Basics
                            │
                            ▼
                 Financial Products
      (FX, MM, Bonds, Equities, Derivatives)
                            │
                            ▼
                  Trade Lifecycle
                            │
        ┌───────────────────┴───────────────────┐
        ▼                                       ▼
   Pre-Trade                             Post-Trade

Client Requirement
        │
        ▼
Sales / Relationship Manager
        │
        ▼
Trader / Dealer
        │
        ▼
Trade Capture
        │
        ▼
Trade Validation
        │
        ▼
Static Data Validation
        │
        ▼
Market Data
        │
        ▼
Pricing & Valuation
        │
        ▼
Trade Confirmation
        │
        ▼
Position Management
        │
        ▼
Hedging
        │
        ▼
⭐ Risk Management   ← Current Module
        │
        ▼
P&L Calculation
        │
        ▼
Settlement
        │
        ▼
Accounting
        │
        ▼
Regulatory Reporting
        │
        ▼
Trade Archive

---

| No | Module                      | Status         |
| -- | --------------------------- | -------------- |
| 1  | Investment Banking Overview | ✅ Completed    |
| 2  | Trade Lifecycle             | ✅ Completed    |
| 3  | Trade Capture               | ✅ Completed    |
| 4  | Trade Validation            | ✅ Completed    |
| 5  | Static Data                 | ✅ Completed    |
| 6  | Market Data                 | ✅ Completed    |
| 7  | Pricing & Valuation         | ✅ Completed    |
| 8  | Position Management         | ✅ Completed    |
| 9  | Hedging                     | ✅ Completed    |
| 10 | Risk Management             | 🟡 In Progress |


Risk Management
      │
      ├── Introduction to Risk               ✅
      │
      ├── Why Banks Take Risk                ✅
      │
      ├── Market Risk                        ✅ Basic
      │
      ├── Credit Risk                        ✅ Basic
      │
      ├── Operational Risk                   ✅ Basic
      │
      ├── Liquidity Risk                     ✅ Basic
      │
      ├── Risk Appetite                      ✅
      │
      ├── Risk Tolerance                     ✅
      │
      ├── Temporary Exposure                 ✅
      │
      ├── Permanent Exposure                 ✅
      │
      ├── Hedging & Exposure Reduction       ✅
      │
      ├── Production Support Scenarios       ✅
      │
      └── Investigation Process              ✅
