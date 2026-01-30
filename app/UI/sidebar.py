# app/ui/sidebar.py

import streamlit as st
from models.inputs import MicrogridInputs, BatteryConfig


def scenario_builder() -> MicrogridInputs:
    st.sidebar.header("🔧 Scenario Builder")

    st.sidebar.subheader("Load Profile (kWh)")
    base_load = st.sidebar.slider(
        "Average hourly load",
        min_value=1.0,
        max_value=20.0,
        value=8.0,
    )
    load_profile = [base_load] * 24

    st.sidebar.subheader("Solar Generation (kWh)")
    solar_peak = st.sidebar.slider(
        "Peak solar generation",
        min_value=0.0,
        max_value=15.0,
        value=6.0,
    )
    solar_profile = [
        solar_peak if 9 <= h <= 16 else 0.0
        for h in range(24)
    ]

    st.sidebar.subheader("Grid Tariff (₹/kWh)")
    low_tariff = st.sidebar.slider("Night tariff", 1.0, 5.0, 2.0)
    high_tariff = st.sidebar.slider("Peak tariff", 5.0, 12.0, 8.0)

    grid_tariff = [
        high_tariff if 17 <= h <= 22 else low_tariff
        for h in range(24)
    ]

    st.sidebar.subheader("Battery Configuration")
    battery = BatteryConfig(
        capacity_kwh=st.sidebar.slider("Battery capacity (kWh)", 5.0, 30.0, 10.0),
        max_charge_kw=st.sidebar.slider("Max charge rate (kW)", 1.0, 10.0, 3.0),
        max_discharge_kw=st.sidebar.slider("Max discharge rate (kW)", 1.0, 10.0, 3.0),
        min_soc=0.2,
        max_soc=0.9,
        initial_soc=0.5,
    )

    diesel_cost = st.sidebar.slider(
        "Diesel cost (₹/kWh)",
        min_value=8.0,
        max_value=20.0,
        value=12.0,
    )

    return MicrogridInputs(
        load_profile=load_profile,
        solar_profile=solar_profile,
        grid_tariff=grid_tariff,
        diesel_cost=diesel_cost,
        battery=battery,
    )
