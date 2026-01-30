# core/scheduler.py

def optimized_strategy(
    hour: int,
    load: float,
    solar_available: float,
    tariff: float,
    battery,
    diesel_cost: float,
):
    """
    Cost-aware optimized scheduling strategy.
    Uses tariff signals to decide battery charging and discharging.
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

    explanation_parts = []

    # 1. Use solar first
    solar_used = min(solar_available, remaining_load)
    decision["solar_used"] = solar_used
    remaining_load -= solar_used

    if solar_used > 0:
        explanation_parts.append("Used available solar energy")

    # 2. Tariff-based battery logic
    LOW_TARIFF = 0.7
    HIGH_TARIFF = 1.3

    if tariff <= LOW_TARIFF:
        # Cheap electricity → charge battery if possible
        charge_amount = battery.available_storage()
        decision["battery_charge"] = charge_amount
        explanation_parts.append(
            "Grid tariff is low, charging battery for future use"
        )

    elif tariff >= HIGH_TARIFF:
        # Expensive electricity → discharge battery
        discharge_amount = battery.available_energy()
        decision["battery_discharge"] = discharge_amount
        explanation_parts.append(
            "Grid tariff is high, discharging battery to reduce cost"
        )

    else:
        explanation_parts.append(
            "Grid tariff is moderate, preserving battery"
        )

    # 3. Supply remaining load
    if remaining_load > 0:
        if decision["battery_discharge"] > 0:
            used = decision["battery_discharge"]
            remaining_load -= used

        if remaining_load > 0:
            decision["grid_used"] = remaining_load
            remaining_load = 0
            explanation_parts.append("Remaining load met using grid supply")

    # 4. Diesel last resort
    if remaining_load > 0:
        decision["diesel_used"] = remaining_load
        remaining_load = 0
        explanation_parts.append("Diesel used as last resort")

    decision["explanation"] = (
        f"Hour {hour}: " + "; ".join(explanation_parts)
    )

    return decision
