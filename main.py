"""
main.py

Entry point for the Smart Microgrid Energy Scheduler prototype.

Running this file will:
- Execute baseline simulation
- Execute optimized simulation
- Compare results
- Save output to results/summary.txt
"""

from compare import compare


def main():
    print("\nStarting Smart Microgrid Energy Scheduler...\n")
    compare()
    print("\nSimulation completed successfully.\n")


if __name__ == "__main__":
    main()
