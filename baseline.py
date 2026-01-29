"""
baseline.py

Implements the traditional (baseline) microgrid energy management strategy.

Baseline Logic:
1. Use solar power to meet load.
2. Remaining load is met using grid electricity.
3. Battery is charged ONLY from excess solar.
4. No cost awareness, no future planning.

This file acts as the reference case for comparison.
"""

from data.load import LOAD
from data.solar import SOLAR
from data.tariff import GRID_TARIFF, BATTERY


def run_baseline():
    """
    Runs a 24-hour baseline simulation.

    Returns:
        total_cost (float): Total grid energy cost for the day
    """

    battery_soc = 0.0  # State of Charge in kWh
    total_cost = 0.0

    for hour in range(24):
        load = LOAD[hour]
        solar = SOLAR[hour]

        # 1. Use solar to meet load
        solar_used = min(load, solar)
        load -= solar_used
        excess_solar = solar - solar_used

        # 2. Charge battery using excess solar only
        if excess_solar > 0:
            battery_soc += excess_solar * BATTERY["efficiency"]
            battery_soc = min(battery_soc, BATTERY["capacity"])

        # 3. Use grid for remaining load (flat day tariff for baseline)
        if load > 0:
            total_cost += load * GRID_TARIFF["day"]

    return total_cost


# Allow standalone testing
if __name__ == "__main__":
    cost = run_baseline()
    print("Baseline Total Cost:", cost)
