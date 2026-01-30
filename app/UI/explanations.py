# app/ui/explanations.py

import streamlit as st


def show_explanations(baseline, optimized):
    st.header("🧠 Decision Explainability")

    hour = st.slider("Select hour", 0, 23, 12)

    col1, col2 = st.columns(2)

    col1.subheader("Baseline Decision")
    col1.info(baseline.hourly_results[hour].explanation)

    col2.subheader("Optimized Decision")
    col2.success(optimized.hourly_results[hour].explanation)
