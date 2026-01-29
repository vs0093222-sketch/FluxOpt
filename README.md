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
Working on this project – Rajarshi, Devashish, Neitik, Himanshu

