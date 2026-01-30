"""
optimized.py
Cost-aware, explainable microgrid scheduler.
"""

from data.load import load_profiles
import os

# =====================
# System parameters
# =====================
BATTERY_EFFICIENCY = 0.9
MAX_CHARGE_RATE = 20        # kWh/hour
MAX_DISCHARGE_RATE = 20     # kWh/hour

PEAK_GRID_THRESHOLD = 8     # ₹/kWh
CHEAP_GRID_THRESHOLD = 5    # ₹/kWh

def run_optimized() -> float:
    """
    Runs optimized cost-aware scheduling.
    Writes explainable decisions to results/decisions.txt
    Returns:
        total_cost (float)
    """

    load, solar, grid_tariff = load_profiles()

    diesel_cost = 18.0
    battery_capacity = 100.0

    battery_soc = 0.0
    total_cost = 0.0

    decisions = []

    for hour in range(len(load)):
        reasons = []
        remaining_load = load[hour]

        # 1️⃣ Use solar first
        solar_used = min(solar[hour], remaining_load)
        remaining_load -= solar_used
        if solar_used > 0:
            reasons.append(f"Used {solar_used:.1f} kWh solar")

        # 2️⃣ Charge battery with excess solar
        excess_solar = solar[hour] - solar_used
        if excess_solar > 0 and battery_soc < battery_capacity:
            charge = min(excess_solar, MAX_CHARGE_RATE, battery_capacity - battery_soc)
            battery_soc += charge * BATTERY_EFFICIENCY
            reasons.append(f"Charged battery with {charge:.1f} kWh solar")

        # 3️⃣ Charge battery from CHEAP grid
        if grid_tariff[hour] <= CHEAP_GRID_THRESHOLD and battery_soc < battery_capacity:
            charge = min(MAX_CHARGE_RATE, battery_capacity - battery_soc)
            battery_soc += charge * BATTERY_EFFICIENCY
            total_cost += charge * grid_tariff[hour]
            reasons.append(f"Charged battery from cheap grid (₹{grid_tariff[hour]:.2f})")

        # 4️⃣ Discharge battery during PEAK grid hours
        if remaining_load > 0 and grid_tariff[hour] >= PEAK_GRID_THRESHOLD:
            discharge = min(remaining_load, battery_soc, MAX_DISCHARGE_RATE)
            if discharge > 0:
                battery_soc -= discharge
                remaining_load -= discharge
                reasons.append("Discharged battery to avoid peak tariff")

        # 5️⃣ Use grid
        if remaining_load > 0:
            total_cost += remaining_load * grid_tariff[hour]
            reasons.append(f"Used grid at ₹{grid_tariff[hour]:.2f}/kWh")
            remaining_load = 0

        decisions.append(f"Hour {hour}: " + " | ".join(reasons))

    # =====================
    # Write explainability
    # =====================
    os.makedirs("results", exist_ok=True)
    with open("results/decisions.txt", "w", encoding="utf-8") as f:
        f.write("Hourly Decision Explanations\n")
        f.write("============================\n\n")
        for line in decisions:
            f.write(line + "\n")

    return total_cost
