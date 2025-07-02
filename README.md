# Monte Carlo Option Pricing Simulator

A mathematical simulation project that prices European call options using **Geometric Brownian Motion** and **Monte Carlo methods**.  
Built from the first principles with a focus on mathematical understanding, probabilistic modeling, and visual intuition.

---

## Project Overview

This project simulates possible future paths of a stock price using **Geometric Brownian Motion (GBM)**  
and estimates the fair price of a **European call option** via **Monte Carlo simulation**.

**Goal:**  
- Understand and implement how financial derivatives can be priced using random processes and expected values — not predictions.

---

## Key Concepts

- **Call Option**: A contract giving the buyer the right (not obligation) to buy an asset at a fixed strike price in the future.  
- **Payoff**: `max(S_T - K, 0)` — the profit from the option at expiry.  
- **Monte Carlo Simulation**: A technique to estimate expected outcomes by simulating many random futures.  
- **Geometric Brownian Motion (GBM)**: A model of stock price movement that ensures prices stay positive and reflect volatility.  
- **Discounting**: Bringing future value to present using `e^(-rT)`.

---

## Math Behind It

- **Stock price simulated using**:  
  `S_t = S_0 * exp[(μ - σ² / 2) * t + σ * W_t]`

- **Payoff of each simulation**:  
  `Payoff = max(S_T - K, 0)`

- **Option price today**:  
  `Price = e^(-rT) * E[Payoff]`

---

## What’s in the Notebook

- Simulation of 1000 GBM stock price paths  
- Histogram of final stock prices $S_T$  
- Computation of option price using expected payoff  
- Discounting using risk-free interest rate  
- Explanatory markdown cells with math, visuals, and logic

---

## Streamlit App (Interactive Version)

A Streamlit-based UI lets you explore the same model with adjustable parameters.

### Run Locally:

```bash
streamlit run interactive_app.py
```
---


## What I Learned

- How randomness can simulate uncertainty in financial markets  
- Why Brownian motion underlies stochastic finance  
- How options are priced using expected values and discounting  
- How to apply core mathematical ideas in a practical context

---

## Requirements

- Python 
- Libraries: `numpy`, `matplotlib`, `seaborn`, `jupyter`

Install with:

```bash
pip install numpy matplotlib seaborn
