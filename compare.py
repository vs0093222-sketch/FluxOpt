"""
compare.py
Final comparison + dashboard JSON (SAFE CO₂ handling)
"""

from baseline import run_baseline
from optimized import run_optimized
from plots import plot_results
import json
import os


def main():
    baseline_cost, baseline_co2 = run_baseline()
    optimized_cost, optimized_co2, decisions = run_optimized()

    # Cost savings
    cost_savings = ((baseline_cost - optimized_cost) / baseline_cost) * 100

    # SAFE CO₂ reduction calculation
    if baseline_co2 > 0:
        co2_reduction = ((baseline_co2 - optimized_co2) / baseline_co2) * 100
    else:
        co2_reduction = 0.0

    print("========== MICROGRID ENERGY COMPARISON ==========")
    print(f"Baseline Cost      : ₹{baseline_cost:.2f}")
    print(f"Optimized Cost     : ₹{optimized_cost:.2f}")
    print(f"Cost Savings       : {cost_savings:.2f}%")
    print("-----------------------------------------------")
    print(f"Baseline CO₂       : {baseline_co2:.2f} kg")
    print(f"Optimized CO₂      : {optimized_co2:.2f} kg")
    print(f"CO₂ Reduction      : {co2_reduction:.2f}%")
    print("================================================")

    dashboard = {
        "baseline": {
            "cost": baseline_cost,
            "co2": baseline_co2
        },
        "optimized": {
            "cost": optimized_cost,
            "co2": optimized_co2
        },
        "savings": {
            "cost_percent": round(cost_savings, 2),
            "co2_percent": round(co2_reduction, 2)
        },
        "decisions": decisions
    }

    os.makedirs("results", exist_ok=True)
    with open("results/dashboard.json", "w", encoding="utf-8") as f:
        json.dump(dashboard, f, indent=4)

    plot_results(
        baseline_cost,
        optimized_cost,
        baseline_co2,
        optimized_co2
    )


if __name__ == "__main__":
    main()
