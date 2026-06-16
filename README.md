# Transformer Simulation System

## Overview
This project simulates the behavior of a power transformer under varying load and environmental conditions.

It calculates:
- Hourly load changes
- Ambient temperature effects
- Transformer thermal response
- Daily operational reports

---

## Features
- Hourly simulation engine
- Sensor-based architecture (Temperature & Load)
- Transformer state modeling
- Daily report generation
- Statistical analysis (min, max, average)

---

## Architecture
Simulation → Sensors → Transformer → DailyReport

- Simulation: controls simulation flow
- Sensors: read data from environment
- Transformer: calculates operational state
- DailyReport: stores and analyzes results

---

## Output Example
Each hour produces a structured report:

{
  "Hour": 14,
  "Season": "summer",
  "Temperature": 76.5,
  "Current Load": 475.00,
  "Load Percentage": 75
}

---

## Future Work
- Three-phase transformer modeling
- Fault detection system
- Real-time hardware integration (STM32 / ESP)
- Graphical dashboard

---

## Author
Hadi Norouzi