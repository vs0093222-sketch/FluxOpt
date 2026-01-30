from data.load import load_profiles

GRID_CO2 = 0.82
BATTERY_CAPACITY = 20
BATTERY_EFF = 0.9

def run_optimized():
    load, solar, tariff = load_profiles()

    battery = 0
    total_cost = 0
    total_co2 = 0

    for h in range(24):
        remaining_load = load[h]

        # 1. Use solar first
        solar_used = min(remaining_load, solar[h])
        remaining_load -= solar_used
        solar_left = solar[h] - solar_used

        # 2. Charge battery from solar
        if solar_left > 0 and battery < BATTERY_CAPACITY:
            charge = min(solar_left, BATTERY_CAPACITY - battery)
            battery += charge * BATTERY_EFF

        # 3. Charge battery from cheap grid
        if tariff[h] <= 5 and battery < BATTERY_CAPACITY:
            charge = min(3, BATTERY_CAPACITY - battery)
            battery += charge * BATTERY_EFF
            total_cost += charge * tariff[h]
            total_co2 += charge * GRID_CO2

        # 4. Discharge battery during peak hours
        if tariff[h] >= 8 and battery > 0:
            discharge = min(battery, remaining_load)
            battery -= discharge
            remaining_load -= discharge

        # 5. Grid last option
        if remaining_load > 0:
            total_cost += remaining_load * tariff[h]
            total_co2 += remaining_load * GRID_CO2

    return round(total_cost, 2), round(total_co2, 2)
