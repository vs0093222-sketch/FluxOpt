# core/simulator.py

from typing import Callable, List
from models.inputs import MicrogridInputs
from models.outputs import HourResult, SimulationResult
from core.battery import Battery
from utils.validators import validate_inputs


def run_simulation(
    inputs: MicrogridInputs,
    strategy: Callable,
) -> SimulationResult:
    """
    Runs a 24-hour microgrid simulation using the given strategy.
    """
    validate_inputs(inputs)

    battery_cfg = inputs.battery
    battery = Battery(
        capacity_kwh=battery_cfg.capacity_kwh,
        max_charge_kw=battery_cfg.max_charge_kw,
        max_discharge_kw=battery_cfg.max_discharge_kw,
        min_soc=battery_cfg.min_soc,
        max_soc=battery_cfg.max_soc,
        initial_soc=battery_cfg.initial_soc,
    )

    hourly_results: List[HourResult] = []
    total_cost = 0.0

    for hour in range(24):
        load = inputs.load_profile[hour]
        solar_available = inputs.solar_profile[hour]
        tariff = inputs.grid_tariff[hour]

        decision = strategy(
            hour=hour,
            load=load,
            solar_available=solar_available,
            tariff=tariff,
            battery=battery,
            diesel_cost=inputs.diesel_cost,
        )

        # Unpack decision
        solar_used = min(solar_available, decision.get("solar_used", 0.0))
        battery_used = battery.discharge(decision.get("battery_discharge", 0.0))
        battery_charged = battery.charge(decision.get("battery_charge", 0.0))
        grid_used = decision.get("grid_used", 0.0)
        diesel_used = decision.get("diesel_used", 0.0)

        # Cost calculation
        cost = (
            grid_used * tariff +
            diesel_used * inputs.diesel_cost
        )

        total_cost += cost

        explanation = decision.get("explanation", "")

        hourly_results.append(
            HourResult(
                hour=hour,
                load=load,
                solar_used=solar_used,
                battery_used=battery_used,
                grid_used=grid_used,
                diesel_used=diesel_used,
                battery_soc=battery.soc,
                cost=cost,
                explanation=explanation,
            )
        )

    return SimulationResult(
        hourly_results=hourly_results,
        total_cost=total_cost,
    )
