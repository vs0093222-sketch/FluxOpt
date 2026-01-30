# models/inputs.py

from dataclasses import dataclass
from typing import List


@dataclass
class BatteryConfig:
    capacity_kwh: float
    max_charge_kw: float
    max_discharge_kw: float
    min_soc: float        # 0–1
    max_soc: float        # 0–1
    initial_soc: float    # 0–1


@dataclass
class MicrogridInputs:
    load_profile: List[float]          # kWh per hour (24 values)
    solar_profile: List[float]         # kWh per hour (24 values)
    grid_tariff: List[float]           # ₹ / kWh (24 values)
    diesel_cost: float                 # ₹ / kWh
    battery: BatteryConfig
