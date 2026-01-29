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


def compare():
    # Run simulations
    baseline_cost = run_baseline()
    optimized_cost = run_optimized()

    # Calculate savings
    savings_percent = ((baseline_cost - optimized_cost) / baseline_cost) * 100

    # Print results to terminal
    print("========== MICROGRID ENERGY COMPARISON ==========")
    print(f"Baseline Total Cost   : ₹{baseline_cost:.2f}")
    print(f"Optimized Total Cost  : ₹{optimized_cost:.2f}")
    print(f"Cost Savings          : {savings_percent:.2f}%")
    print("================================================")

    # Ensure results directory exists
    os.makedirs("results", exist_ok=True)

    # Write results to file
    with open("results/summary.txt", "w") as f:
        f.write("Microgrid Energy Scheduling Results\n")
        f.write("=================================\n")
        f.write(f"Baseline Total Cost   : ₹{baseline_cost:.2f}\n")
        f.write(f"Optimized Total Cost  : ₹{optimized_cost:.2f}\n")
        f.write(f"Cost Savings          : {savings_percent:.2f}%\n")

    print("\nResults saved to: results/summary.txt")


# Allow standalone execution
if __name__ == "__main__":
    compare()
