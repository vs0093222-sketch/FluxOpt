"""
compare.py

Compares baseline and optimized microgrid strategies.
Also generates graphs.
"""

from baseline import run_baseline
from optimized import run_optimized
from plots import plot_results
import os


def compare():
    # Run simulations
    baseline_cost, baseline_co2 = run_baseline()
    optimized_cost, optimized_co2 = run_optimized()

    # Calculate savings
    cost_savings = ((baseline_cost - optimized_cost) / baseline_cost) * 100
    co2_reduction = (
        ((baseline_co2 - optimized_co2) / baseline_co2) * 100
        if baseline_co2 > 0 else 0
    )

    # Print results
    print("========== MICROGRID ENERGY COMPARISON ==========")
    print(f"Baseline Cost      : ₹{baseline_cost:.2f}")
    print(f"Optimized Cost     : ₹{optimized_cost:.2f}")
    print(f"Cost Savings       : {cost_savings:.2f}%")
    print("-----------------------------------------------")
    print(f"Baseline CO₂       : {baseline_co2:.2f} kg")
    print(f"Optimized CO₂      : {optimized_co2:.2f} kg")
    print(f"CO₂ Reduction      : {co2_reduction:.2f}%")
    print("================================================")

    # Save summary
    os.makedirs("results", exist_ok=True)
    with open("results/summary.txt", "w", encoding="utf-8") as f:
        f.write("Microgrid Energy Scheduling Results\n")
        f.write("=================================\n")
        f.write(f"Baseline Cost   : ₹{baseline_cost:.2f}\n")
        f.write(f"Optimized Cost  : ₹{optimized_cost:.2f}\n")
        f.write(f"Cost Savings   : {cost_savings:.2f}%\n\n")
        f.write(f"Baseline CO₂   : {baseline_co2:.2f} kg\n")
        f.write(f"Optimized CO₂  : {optimized_co2:.2f} kg\n")
        f.write(f"CO₂ Reduction  : {co2_reduction:.2f}%\n")

    # Generate graphs
    plot_results(
        baseline_cost,
        optimized_cost,
        baseline_co2,
        optimized_co2
    )


if __name__ == "__main__":
    compare()
