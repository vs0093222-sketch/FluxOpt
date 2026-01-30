import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="FluxOpt – Smart Microgrid Optimizer",
    layout="wide"
)

st.title("⚡ FluxOpt – Smart Microgrid Energy Scheduler")
st.markdown("AI‑assisted optimization of cost & CO₂ emissions")

# -----------------------------
# Load dashboard data
# -----------------------------
with open("results/dashboard.json", "r") as f:
    data = json.load(f)

baseline = data["baseline"]
optimized = data["optimized"]
savings = data["savings"]
decisions = data["decisions"]

# -----------------------------
# KPI Section
# -----------------------------
st.subheader("📊 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Baseline Cost (₹)",
    baseline["cost"]
)

col2.metric(
    "Optimized Cost (₹)",
    optimized["cost"],
    f"-{savings['cost_percent']:.2f}%"
)

col3.metric(
    "CO₂ Reduction",
    f"{savings['co2_percent']:.2f}%",
)

# -----------------------------
# Charts
# -----------------------------
st.subheader("📈 Cost & Emissions Comparison")

chart_df = pd.DataFrame({
    "Scenario": ["Baseline", "Optimized"],
    "Cost (₹)": [baseline["cost"], optimized["cost"]],
    "CO₂ (kg)": [baseline["co2"], optimized["co2"]]
})

col4, col5 = st.columns(2)

with col4:
    fig1, ax1 = plt.subplots()
    ax1.bar(chart_df["Scenario"], chart_df["Cost (₹)"], color=["red", "green"])
    ax1.set_title("Cost Comparison")
    st.pyplot(fig1)

with col5:
    fig2, ax2 = plt.subplots()
    ax2.bar(chart_df["Scenario"], chart_df["CO₂ (kg)"], color=["orange", "blue"])
    ax2.set_title("CO₂ Emissions Comparison")
    st.pyplot(fig2)

# -----------------------------
# Hourly Decisions Table
# -----------------------------
st.subheader("🕒 Hour‑wise Optimization Decisions")

rows = []
for d in decisions:
    rows.append({
        "Hour": d["hour"],
        "Actions": ", ".join(d["actions"]),
        "Battery SOC": round(d["battery_soc"], 2)
    })

decision_df = pd.DataFrame(rows)
st.dataframe(decision_df, use_container_width=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "Built for Hackathon | Smart Energy • Sustainability • Optimization"
)
