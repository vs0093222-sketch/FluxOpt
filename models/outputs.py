# models/outputs.py

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class HourResult:
    hour: int
    load: float
    solar_used: float
    battery_used: float
    grid_used: float
    diesel_used: float
    battery_soc: float
    cost: float
    explanation: str


@dataclass
class SimulationResult:
    hourly_results: List[HourResult]
    total_cost: float
