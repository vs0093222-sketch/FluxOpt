# Smart Microgrid Energy Scheduler (Prototype)

## Overview
This project is a **software-based microgrid simulator and daily energy scheduler** designed to minimize energy cost and diesel usage while meeting all electricity demand.

It simulates a **24-hour operation** of a small microgrid consisting of:
- Solar generation
- Battery storage
- Grid supply (with time-based tariffs)
- Diesel generator (as last resort)

The system compares:
- A **Baseline (traditional) strategy**
- An **Optimized (cost-aware) scheduling strategy**

and clearly shows cost savings.

This prototype is built for **hackathon / academic submission** with a focus on:
- Simplicity
- Explainability
- Correctness
- Real-world relevance

---

## Problem Statement
Small-scale microgrids (used by MSMEs, hospitals, campuses) often rely on rule-based or manual energy management, leading to:
- Excessive diesel usage
- Higher operational costs
- Poor battery utilization

The goal of this project is to demonstrate how **smart, cost-aware scheduling** can significantly reduce cost and diesel dependency.

---

## Features
- 24-hour microgrid simulation
- Baseline vs Optimized strategy comparison
- Time-of-day grid tariff handling
- Battery capacity and charge/discharge constraints
- Clear cost comparison output
- Beginner-friendly, modular code structure

---

## Project Structure
microgrid-prototype/
│
├── data/
│ ├── load.py # Hourly electricity demand
│ ├── solar.py # Hourly solar generation
│ └── tariff.py # Grid tariff, battery & diesel parameters
│
├── baseline.py # Traditional (baseline) energy strategy
├── optimized.py # Cost-aware optimized scheduler
├── compare.py # Comparison of baseline vs optimized
├── main.py # Entry point to run the project
│
├── results/
│ └── summary.txt # Auto-generated results file
│
└── README.md


---

## Requirements
- **Python 3.8 or higher**
- No external libraries required  
  (Uses only standard Python features)

✅ This project runs without `pip install` or virtual environments.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd microgrid-prototype
2. Create Results Folder
mkdir results
Do NOT create summary.txt manually.
It will be created automatically when the program runs.

How to Run the Project
Run the following command from the project root:

python main.py
Expected Output (Terminal)
Example:

Baseline Cost: 12400
Optimized Cost: 9600
Savings (%): 22.58
Output File
After execution, results are saved automatically to:

results/summary.txt
Example content:

Baseline Cost: 12400
Optimized Cost: 9600
Savings (%): 22.58
Baseline vs Optimized Logic (Simple Explanation)
Baseline Strategy
Solar → Load

Remaining load → Grid

Battery charges only from excess solar

No cost awareness

Optimized Strategy
Solar always used first

Battery charged when grid is cheap (night)

Battery discharged during peak tariff hours

Diesel avoided as much as possible

Limitations (Intentional)
No real-time hardware control

No machine learning

No forecasting uncertainty

Focused on clarity and correctness over complexity

Use Case Example
This prototype represents a small hospital or MSME microgrid where:

Solar is available during the day

Grid tariffs vary by time

Diesel is expensive and undesirable

License
This project is intended for educational and hackathon use only.

Team
Member A: Data & Baseline Simulation

Member B: Optimized Scheduler & Comparison

Final Note
This project demonstrates that clear logic, explainability, and comparison are more powerful than complex black-box solutions.


---

### ✅ NEXT STEP
Say **`NEXT: load.py`**  
and I’ll give you the **exact production‑safe code** for the next file.

We’ll finish this **file by file, error‑free**.
::contentReference[oaicite:0]{index=0}

