# app/ui/charts.py

import streamlit as st
import pandas as pd
import plotly.express as px


def show_comparison(baseline, optimized):
    st.header("📊 Strategy Comparison")

    col1, col2 = st.columns(2)

    col1.metric(
        "Baseline Total Cost (₹)",
        round(baseline.total_cost, 2)
    )

    col2.metric(
        "Optimized Total Cost (₹)",
        round(optimized.total_cost, 2),
        delta=round(baseline.total_cost - optimized.total_cost, 2)
    )

    df = pd.DataFrame([
        {
            "Hour": r.hour,
            "Grid": r.grid_used,
            "Diesel": r.diesel_used,
            "Battery": r.battery_used,
            "Solar": r.solar_used,
        }
        for r in optimized.hourly_results
    ])

    fig = px.bar(
        df,
        x="Hour",
        y=["Solar", "Battery", "Grid", "Diesel"],
        title="Optimized Energy Mix (Hourly)",
        labels={"value": "Energy (kWh)", "variable": "Source"},
    )

    st.plotly_chart(fig, use_container_width=True)
