"""
baseline.py
Naive microgrid operation (NO battery intelligence)
"""

from data.load import load_profiles

DIESEL_COST = 18.0          # ₹/kWh
CO2_PER_DIESEL_UNIT = 2.68  # kg CO₂ / kWh


def run_baseline():
    load, solar, grid_tariff = load_profiles()

    total_cost = 0.0
    diesel_used = 0.0

    for hour in range(len(load)):
        remaining_load = load[hour]

        # Use solar first
        solar_used = min(solar[hour], remaining_load)
        remaining_load -= solar_used

        # Use grid
        if remaining_load > 0:
            # ❗ Naive rule: use diesel during peak grid hours
            if grid_tariff[hour] >= 8:
                diesel_used += remaining_load
                total_cost += remaining_load * DIESEL_COST
            else:
                total_cost += remaining_load * grid_tariff[hour]

    total_co2 = diesel_used * CO2_PER_DIESEL_UNIT
    return total_cost, total_co2
