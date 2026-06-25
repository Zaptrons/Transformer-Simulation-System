# Transformer Digital Twin

## Overview

This project aims to develop a **Digital Twin** for distribution transformers.

The system simulates transformer operation under different environmental and loading conditions, estimates thermal behavior, and provides the foundation for intelligent monitoring, early warning, and predictive maintenance.

The project is designed as both an educational platform and a prototype for future industrial applications.

---

## Project Goals

* Simulate transformer operating conditions
* Model ambient temperature and load profiles
* Estimate transformer thermal behavior
* Generate operational reports
* Develop an intelligent warning system
* Support predictive maintenance

---

## Current Features

* Stable simulation engine
* Clock and Calendar system
* Time management engine
* Hourly simulation
* Daily simulation
* Monthly simulation
* Yearly simulation
* Environment simulation
* Temperature sensor model
* Load sensor model
* Transformer operating model
* Daily report generation

---

## Current Architecture

```
Simulation
│
├── TimeEngine
│   ├── Clock
│   └── Calendar
│
├── Environment
│
├── Sensors
│   ├── TemperatureSensor
│   └── LoadSensor
│
├── Transformer
│
└── DailyReport
```

---

## Example Output

Each simulated hour generates a structured record:

```json
{
  "Hour": 14,
  "Day": 5,
  "Month": 7,
  "Year": 0,
  "Season": "Summer",
  "Temperature": 76.5,
  "Current Load": 475.0,
  "Load Percentage": 75
}
```

---

## Development Roadmap

### Version 0.2

* Stable simulation engine
* Time management architecture
* One-year simulation

### Version 0.3

* Realistic daily load profiles
* Seasonal temperature profiles

### Version 0.4

* Transformer thermal model
* Hot-spot temperature estimation

### Version 0.5

* Intelligent warning system
* Thermal stress analysis

### Version 0.6

* Predictive maintenance
* Remaining lifetime estimation

### Version 1.0

* Complete Digital Twin
* Dashboard
* Data visualization
* Industrial demonstration

---

## Technologies

* Python
* Object-Oriented Programming (OOP)
* Clean Architecture
* Simulation
* Git
* GitHub

---

## Author

**Hadi Norouzi**

Electronic Engineer

Embedded Systems Developer

Python Developer

---

## Project Status

**Version:** v0.2

The simulation engine is stable and under active development toward a complete Digital Twin platform.
