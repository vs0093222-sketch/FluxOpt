# utils/validators.py

from models.inputs import MicrogridInputs


def validate_inputs(inputs: MicrogridInputs):
    if not (
        len(inputs.load_profile) ==
        len(inputs.solar_profile) ==
        len(inputs.grid_tariff) ==
        24
    ):
        raise ValueError("Load, solar, and tariff profiles must be 24 hours long.")

    if inputs.battery.min_soc >= inputs.battery.max_soc:
        raise ValueError("Battery min SOC must be less than max SOC.")

    if not (0 <= inputs.battery.initial_soc <= 1):
        raise ValueError("Initial SOC must be between 0 and 1.")

    if inputs.diesel_cost <= 0:
        raise ValueError("Diesel cost must be positive.")
