"""
optimized.py
Cost-aware, explainable microgrid scheduler.
Dashboard-ready output.
"""

from data.load import load_profiles
import os
import json

BATTERY_EFFICIENCY = 0.9
MAX_CHARGE_RATE = 20
MAX_DISCHARGE_RATE = 20
DIESEL_COST = 18.0
CO2_PER_DIESEL_UNIT = 2.68
PEAK_GRID_THRESHOLD = 8


def run_optimized():
    load, solar, grid_tariff = load_profiles()

    battery_capacity = 100.0
    battery_soc = 0.0

    total_cost = 0.0
    diesel_used = 0.0
    decisions = []

    for hour in range(len(load)):
        remaining = load[hour]
        actions = []

        # Solar
        solar_used = min(solar[hour], remaining)
        remaining -= solar_used
        if solar_used > 0:
            actions.append(f"Solar {solar_used:.1f} kWh")

        # Charge battery
        excess = solar[hour] - solar_used
        if excess > 0 and battery_soc < battery_capacity:
            charge = min(excess, MAX_CHARGE_RATE, battery_capacity - battery_soc)
            battery_soc += charge * BATTERY_EFFICIENCY
            actions.append(f"Charge {charge:.1f} kWh")

        # Discharge battery at peak
        if remaining > 0 and grid_tariff[hour] >= PEAK_GRID_THRESHOLD:
            discharge = min(remaining, battery_soc, MAX_DISCHARGE_RATE)
            if discharge > 0:
                battery_soc -= discharge
                remaining -= discharge
                actions.append("Battery discharge")

        # Grid
        if remaining > 0:
            total_cost += remaining * grid_tariff[hour]
            actions.append("Grid used")
            remaining = 0

        # Diesel (still possible)
        if remaining > 0:
            diesel_used += remaining
            total_cost += remaining * DIESEL_COST
            actions.append("Diesel used")

        decisions.append({
            "hour": hour,
            "actions": actions,
            "battery_soc": round(battery_soc, 2)
        })

    total_co2 = diesel_used * CO2_PER_DIESEL_UNIT
    return total_cost, total_co2, decisions
