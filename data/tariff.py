"""
tariff.py

Defines energy pricing and battery configuration for the microgrid.

Includes:
- Time-of-day grid tariff
- Diesel generation cost
- Battery capacity and constraints

All values are realistic and suitable for hackathon demonstration.
"""

# Grid electricity tariff (₹ per kWh)
# Time-of-Day based pricing
GRID_TARIFF = {
    "night": 4,   # 12 AM – 6 AM (cheap)
    "day": 6,     # 6 AM – 6 PM (normal)
    "peak": 9     # 6 PM – 10 PM (expensive)
}

# Diesel generation cost (₹ per kWh)
# Kept high to ensure diesel is used as last resort
DIESEL_COST = 20

# Battery configuration
BATTERY = {
    "capacity": 50,        # kWh (maximum storage)
    "max_charge": 10,      # kWh per hour
    "max_discharge": 10,   # kWh per hour
    "efficiency": 0.90     # 90% round-trip efficiency
}
