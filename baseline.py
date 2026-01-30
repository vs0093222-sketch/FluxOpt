from data.load import load_profiles

GRID_CO2 = 0.82

def run_baseline():
    load, solar, tariff = load_profiles()

    total_cost = 0
    total_co2 = 0

    for h in range(24):
        # Baseline: NO solar prioritization, all grid
        grid_load = load[h]

        total_cost += grid_load * tariff[h]
        total_co2 += grid_load * GRID_CO2

    return round(total_cost, 2), round(total_co2, 2)
