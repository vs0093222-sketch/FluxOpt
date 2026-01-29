"""
load.py

Defines the hourly electricity demand (load profile) for a 24-hour period.
Unit: kWh per hour

Use case modeled:
- Small hospital / MSME
- Low demand at night
- Peak demand during working and evening hours
"""

# Hourly load demand for 24 hours (0–23)
LOAD = [
    8,   # 12 AM
    7,   # 1 AM
    6,   # 2 AM
    6,   # 3 AM
    7,   # 4 AM
    10,  # 5 AM
    14,  # 6 AM
    18,  # 7 AM
    22,  # 8 AM
    26,  # 9 AM
    28,  # 10 AM
    30,  # 11 AM
    29,  # 12 PM
    27,  # 1 PM
    25,  # 2 PM
    24,  # 3 PM
    26,  # 4 PM
    30,  # 5 PM
    32,  # 6 PM
    34,  # 7 PM
    30,  # 8 PM
    22,  # 9 PM
    16,  # 10 PM
    12   # 11 PM
]
