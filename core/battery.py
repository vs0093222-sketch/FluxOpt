# core/battery.py

class Battery:
    def __init__(
        self,
        capacity_kwh: float,
        max_charge_kw: float,
        max_discharge_kw: float,
        min_soc: float,
        max_soc: float,
        initial_soc: float,
    ):
        self.capacity = capacity_kwh
        self.max_charge = max_charge_kw
        self.max_discharge = max_discharge_kw
        self.min_soc = min_soc
        self.max_soc = max_soc
        self.soc = initial_soc  # 0–1

    def available_energy(self) -> float:
        """Energy that can be discharged (kWh)."""
        return max(
            0.0,
            (self.soc - self.min_soc) * self.capacity
        )

    def available_storage(self) -> float:
        """Energy that can be charged (kWh)."""
        return max(
            0.0,
            (self.max_soc - self.soc) * self.capacity
        )

    def charge(self, energy_kwh: float) -> float:
        """
        Charges the battery.
        Returns actual energy charged (kWh).
        """
        energy = min(
            energy_kwh,
            self.max_charge,
            self.available_storage()
        )

        self.soc += energy / self.capacity
        return energy

    def discharge(self, energy_kwh: float) -> float:
        """
        Discharges the battery.
        Returns actual energy discharged (kWh).
        """
        energy = min(
            energy_kwh,
            self.max_discharge,
            self.available_energy()
        )

        self.soc -= energy / self.capacity
        return energy
