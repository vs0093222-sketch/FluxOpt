"""
compare.py

Compares baseline and optimized microgrid strategies.

Outputs:
- Baseline total cost
- Optimized total cost
- Percentage cost savings

Also writes results to:
results/summary.txt
"""

import os
from baseline import run_baseline
from optimized import run_optimized


def calculate_savings(baseline_cost: float, optimized_cost: float) -> float:
    """
    Calculate percentage cost savings.
    """
    if baseline_cost <= 0:
        raise ValueError("Baseline cost must be greater than zero")

    return ((baseline_cost - optimized_cost) / baseline_cost) * 100


def compare():
    # Run simulations
    baseline_cost = run_baseline()
    optimized_cost = run_optimized()

    # Calculate savings
    savings_percent = calculate_savings(baseline_cost, optimized_cost)

    # Print results to terminal
    print("========== MICROGRID ENERGY COMPARISON ==========")
    print(f"Baseline Total Cost   : ₹{baseline_cost:.2f}")
    print(f"Optimized Total Cost  : ₹{optimized_cost:.2f}")
    print(f"Cost Savings          : {savings_percent:.2f}%")
    print("================================================")

    # Ensure results directory exists
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    # Write results to file
    summary_path = os.path.join(results_dir, "summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("Microgrid Energy Scheduling Results\n")
        f.write("=================================\n")
        f.write(f"Baseline Total Cost   : ₹{baseline_cost:.2f}\n")
        f.write(f"Optimized Total Cost  : ₹{optimized_cost:.2f}\n")
        f.write(f"Cost Savings          : {savings_percent:.2f}%\n")

    print(f"\nResults saved to: {summary_path}")


# Allow standalone execution
if __name__ == "__main__":
    compare()
