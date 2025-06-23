Monte Carlo Option Pricing Simulator

A mathematical simulation project that prices European call options using Geometric Brownian Motion and Monte Carlo methods. Built entirely from first principles with a focus on mathematical understanding, probabilistic modeling, and visual intuition.

⸻

📌 Project Overview

This project simulates possible future paths of a stock price using Geometric Brownian Motion (GBM) and estimates the fair price of a European call option via Monte Carlo simulation.

The goal:

Understand and implement how financial derivatives can be priced using random processes and expected values rather than prediction.

⸻

🧠 Key Concepts
	•	Call Option: A contract giving the buyer the right (not obligation) to buy an asset at a fixed strike price in the future.
	•	Payoff: \max(S_T - K, 0) — the profit from the option at expiry.
	•	Monte Carlo Simulation: A technique to estimate expected outcomes by simulating many random futures.
	•	Geometric Brownian Motion (GBM): A model of stock price movement that ensures prices stay positive and reflect volatility.
	•	Discounting: Bringing future value to present using e^{-rT}.

⸻

🧮 Math Behind It
	•	Stock price simulated using:
S_t = S_0 \cdot \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
	•	Payoff of each simulation:
\text{Payoff} = \max(S_T - K, 0)
	•	Option price today:
\text{Price} = e^{-rT} \cdot \mathbb{E}[\text{Payoff}]

⸻

📊 What’s in the Notebook
	•	Simulation of 1000 GBM paths
	•	Histogram of final stock prices
	•	Computation of option price using average discounted payoff
	•	Clean code and visualizations
	•	Markdown explanations of every formula and logic step

⸻

🎯 What I Learned
	•	How randomness can be used to simulate financial uncertainty
	•	Why Brownian motion is foundational in modeling markets
	•	How options are priced probabilistically rather than deterministically
	•	How to apply pure math and probability to real-world finance

⸻

🔧 Requirements
	•	Python 3.x
	•	numpy, matplotlib, seaborn, jupyter

Install with:

pip install numpy matplotlib seaborn


⸻