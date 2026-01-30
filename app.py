# app/app.py

import streamlit as st

from models.inputs import MicrogridInputs, BatteryConfig
from core.simulator import run_simulation
from core.baseline import baseline_strategy
from core.scheduler import optimized_strategy

from app.ui.sidebar import scenario_builder
from app.ui.charts import show_comparison
from app.ui.explanations import show_explanations

st.set_page_config(
    page_title="FluxOpt Virtual Lab",
    layout="wide",
)

st.title("⚡ FluxOpt — Interactive Microgrid Virtual Lab")
st.caption(
    "Design a microgrid scenario, run baseline vs optimized scheduling, "
    "and understand every energy decision."
)

# Sidebar inputs
inputs = scenario_builder()

st.divider()

if st.button("▶ Run Simulation", use_container_width=True):
    with st.spinner("Simulating microgrid operation..."):
        baseline_result = run_simulation(inputs, baseline_strategy)
        optimized_result = run_simulation(inputs, optimized_strategy)

    st.success("Simulation completed successfully")

    show_comparison(baseline_result, optimized_result)
    show_explanations(baseline_result, optimized_result)
