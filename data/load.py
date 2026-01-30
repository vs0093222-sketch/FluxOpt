"""
load.py
Defines load, solar, and grid tariff profiles.
"""

LOAD = [
    8, 7, 6, 6, 7, 10,
    14, 18, 22, 26, 28, 30,
    29, 27, 25, 24, 26, 30,
    32, 34, 30, 22, 16, 12
]

def load_profiles():
    solar = [
        0, 0, 0, 0, 0, 2,
        6, 10, 14, 18, 22, 25,
        26, 24, 20, 15, 10, 5,
        1, 0, 0, 0, 0, 0
    ]

    tariff = [
        4, 4, 4, 4, 4, 5,
        6, 6, 7, 7, 8, 8,
        8, 7, 7, 6, 6, 8,
        10, 10, 8, 6, 5, 4
    ]

    return LOAD, solar, tariff
