from baseline import run_baseline
from optimized import run_optimized

def compare():
    b_cost, b_co2 = run_baseline()
    o_cost, o_co2 = run_optimized()

    print("========== MICROGRID ENERGY COMPARISON ==========")
    print(f"Baseline Cost      : ₹{b_cost}")
    print(f"Optimized Cost     : ₹{o_cost}")
    print(f"Cost Savings       : {((b_cost - o_cost)/b_cost)*100:.2f}%")
    print("-----------------------------------------------")
    print(f"Baseline CO₂       : {b_co2} kg")
    print(f"Optimized CO₂      : {o_co2} kg")
    print(f"CO₂ Reduction      : {((b_co2 - o_co2)/b_co2)*100:.2f}%")
    print("================================================")
