import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Monte Carlo Option Pricing", layout="centered")
st.title("📈 Monte Carlo Simulator for Option Pricing")
st.markdown("Simulate stock prices using Geometric Brownian Motion and price a European call option. (only first 100 plots are plotted to avoid overloading)")

# --- Sidebar Parameters ---
st.sidebar.header("Simulation Parameters")
S0 = st.sidebar.number_input("Initial Stock Price (S₀)", value=100.0)
K = st.sidebar.number_input("Strike Price (K)", value=105.0)
T = st.sidebar.number_input("Time to Maturity (T in years)", value=1.0)
mu = st.sidebar.number_input("Expected Return (μ)", value=0.1)
sigma = st.sidebar.number_input("Volatility (σ)", value=0.2)
r = st.sidebar.number_input("Risk-Free Rate (r)", value=0.05)
N = st.sidebar.slider("Time Steps (N)", min_value=100, max_value=2000, value=1000, step=100)
M = st.sidebar.slider("Simulations (M)", min_value=100, max_value=5000, value=1000, step=100)

# --- Simulate GBM Paths ---
dt = T / N
t = np.linspace(0, T, N+1)
final_prices = []

fig, ax = plt.subplots(figsize=(10, 4))

for _ in range(M):
    W = np.zeros(N+1)
    W[1:] = np.cumsum(np.random.normal(0, np.sqrt(dt), size=N))
    S = S0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)
    final_prices.append(S[-1])
    if _ < 100:  # plot only first 1000 paths
        ax.plot(t, S, linewidth=0.6, alpha=0.4)

ax.set_title("Simulated Stock Price Paths")
ax.set_xlabel("Time (t)")
ax.set_ylabel("S(t)")
ax.grid(True)
st.pyplot(fig)

# --- Histogram and Option Price ---
final_prices = np.array(final_prices)
payoffs = np.maximum(final_prices - K, 0)
expected_payoff = np.mean(payoffs)
option_price = np.exp(-r * T) * expected_payoff

st.subheader("📊 Final Stock Price Distribution")
fig2, ax2 = plt.subplots(figsize=(8, 3.5))
ax2.hist(final_prices, bins=30, color='skyblue', edgecolor='black')
ax2.set_title("Histogram of Final Stock Prices")
ax2.set_xlabel("Final Price (S_T)")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)
st.write(f"**Estimated Option Price:** ₹{option_price:.2f}")

# --- Summary ---
st.markdown("---")
st.caption("Built with NumPy, Matplotlib, and Streamlit.")