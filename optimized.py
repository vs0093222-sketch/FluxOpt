"""
optimized.py

Cost-aware, explainable microgrid scheduler.
"""

from data.load import load_profiles

# System parameters
BATTERY_EFFICIENCY = 0.9
MAX_CHARGE_RATE = 20       # kWh per hour
MAX_DISCHARGE_RATE = 20    # kWh per hour

CO2_PER_DIESEL_UNIT = 2.68  # kg CO2 per unit diesel


def run_optimized() -> float:
    """
    Runs optimized cost-aware scheduling.

    Returns:
        total_cost (float)
    """

    # Load profiles
    load, solar, grid_tariff = load_profiles()

    # Configurable parameters
    diesel_cost = 18.0        # ₹/kWh
    battery_capacity = 100.0 # kWh

    battery_soc = 0.0
    total_cost = 0.0
    diesel_used = 0.0

    for hour in range(len(load)):
        remaining_load = load[hour]

        # 1️⃣ Use solar first
        solar_used = min(solar[hour], remaining_load)
        remaining_load -= solar_used

        # 2️⃣ Charge battery with excess solar
        excess_solar = solar[hour] - solar_used
        if excess_solar > 0 and battery_soc < battery_capacity:
            charge = min(
                excess_solar,
                MAX_CHARGE_RATE,
                battery_capacity - battery_soc
            )
            battery_soc += charge * BATTERY_EFFICIENCY

        # 3️⃣ Battery vs Grid (cost-aware)
        if remaining_load > 0 and grid_tariff[hour] > diesel_cost:
            discharge = min(
                remaining_load,
                battery_soc,
                MAX_DISCHARGE_RATE
            )
            battery_soc -= discharge
            remaining_load -= discharge

        # 4️⃣ Use grid
        if remaining_load > 0:
            total_cost += remaining_load * grid_tariff[hour]
            remaining_load = 0

        # 5️⃣ Diesel as last resort
        if remaining_load > 0:
            diesel_used += remaining_load
            total_cost += remaining_load * diesel_cost

    return total_cost
