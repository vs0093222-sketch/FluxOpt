"""
optimized.py

Implements a cost-aware optimized microgrid energy scheduler.

Optimized Logic:
1. Solar is always used first.
2. Battery is discharged during peak grid tariff hours.
3. Battery is charged during cheap grid tariff hours.
4. Grid is used when necessary.
5. Diesel is avoided (not used in this simplified prototype).

This strategy minimizes total energy cost while respecting battery constraints.
"""

from data.load import LOAD
from data.solar import SOLAR
from data.tariff import GRID_TARIFF, BATTERY


def get_grid_tariff(hour):
    """
    Returns grid tariff based on hour of day.
    """
    if hour < 6:
        return GRID_TARIFF["night"]
    elif hour < 18:
        return GRID_TARIFF["day"]
    else:
        return GRID_TARIFF["peak"]


def run_optimized():
    """
    Runs a 24-hour optimized simulation.

    Returns:
        total_cost (float): Optimized total grid energy cost for the day
    """

    battery_soc = 0.0  # State of Charge in kWh
    total_cost = 0.0

    for hour in range(24):
        load = LOAD[hour]
        solar = SOLAR[hour]
        tariff = get_grid_tariff(hour)

        # 1. Use solar to meet load
        solar_used = min(load, solar)
        load -= solar_used

        # 2. Discharge battery during peak hours
        if tariff == GRID_TARIFF["peak"] and battery_soc > 0:
            discharge = min(
                load,
                battery_soc,
                BATTERY["max_discharge"]
            )
            battery_soc -= discharge
            load -= discharge

        # 3. Use grid for remaining load
        if load > 0:
            total_cost += load * tariff

        # 4. Charge battery during cheap grid hours
        if tariff == GRID_TARIFF["night"]:
            charge = BATTERY["max_charge"]
            battery_soc += charge * BATTERY["efficiency"]
            battery_soc = min(battery_soc, BATTERY["capacity"])

    return total_cost


# Allow standalone testing
if __name__ == "__main__":
    cost = run_optimized()
    print("Optimized Total Cost:", cost)
