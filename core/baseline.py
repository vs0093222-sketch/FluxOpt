# core/baseline.py

def baseline_strategy(
    hour: int,
    load: float,
    solar_available: float,
    tariff: float,
    battery,
    diesel_cost: float,
):
    """
    Naive baseline strategy:
    - Use solar first
    - Then grid
    - Use battery only if grid is insufficient
    - Diesel as last resort
    - No proactive battery charging
    """

    remaining_load = load
    decision = {
        "solar_used": 0.0,
        "battery_discharge": 0.0,
        "battery_charge": 0.0,
        "grid_used": 0.0,
        "diesel_used": 0.0,
        "explanation": "",
    }

    # 1. Use solar
    solar_used = min(solar_available, remaining_load)
    decision["solar_used"] = solar_used
    remaining_load -= solar_used

    # 2. Use grid
    if remaining_load > 0:
        grid_used = remaining_load
        decision["grid_used"] = grid_used
        remaining_load = 0

    # 3. Battery only if grid somehow insufficient (rare)
    if remaining_load > 0:
        battery_used = battery.available_energy()
        decision["battery_discharge"] = battery_used
        remaining_load -= battery_used

    # 4. Diesel last
    if remaining_load > 0:
        decision["diesel_used"] = remaining_load
        remaining_load = 0

    decision["explanation"] = (
        f"Hour {hour}: Used solar first, then grid. "
        "Battery and diesel were only used if unavoidable."
    )

    return decision
