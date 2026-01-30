"""
plots.py

Generates comparison graphs for:
- Cost
- CO₂ emissions
"""

import os
import matplotlib.pyplot as plt


def plot_results(
    baseline_cost: float,
    optimized_cost: float,
    baseline_co2: float,
    optimized_co2: float
):
    # Ensure results directory exists
    os.makedirs("results", exist_ok=True)

    # =====================
    # COST COMPARISON
    # =====================
    plt.figure(figsize=(6, 4))
    plt.bar(
        ["Baseline", "Optimized"],
        [baseline_cost, optimized_cost],
        color=["red", "green"]
    )
    plt.ylabel("Cost (₹)")
    plt.title("Microgrid Cost Comparison")
    plt.tight_layout()
    plt.savefig("results/cost_comparison.png")
    plt.close()

    # =====================
    # CO₂ COMPARISON
    # =====================
    plt.figure(figsize=(6, 4))
    plt.bar(
        ["Baseline", "Optimized"],
        [baseline_co2, optimized_co2],
        color=["red", "green"]
    )
    plt.ylabel("CO₂ Emissions (kg)")
    plt.title("Microgrid CO₂ Emissions Comparison")
    plt.tight_layout()
    plt.savefig("results/co2_comparison.png")
    plt.close()
