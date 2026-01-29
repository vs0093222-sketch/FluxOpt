"""
solar.py

Defines the hourly solar power generation profile for a 24-hour period.
Unit: kWh per hour

Assumptions:
- Zero generation at night
- Peak generation around midday
- Gradual ramp-up and ramp-down
- Suitable for a small hospital / MSME rooftop solar plant
"""

# Hourly solar generation for 24 hours (0–23)
SOLAR = [
    0,   # 12 AM
    0,   # 1 AM
    0,   # 2 AM
    0,   # 3 AM
    2,   # 4 AM
    6,   # 5 AM
    12,  # 6 AM
    18,  # 7 AM
    24,  # 8 AM
    28,  # 9 AM
    30,  # 10 AM
    32,  # 11 AM
    30,  # 12 PM
    26,  # 1 PM
    20,  # 2 PM
    14,  # 3 PM
    8,   # 4 PM
    2,   # 5 PM
    0,   # 6 PM
    0,   # 7 PM
    0,   # 8 PM
    0,   # 9 PM
    0,   # 10 PM
    0    # 11 PM
]
