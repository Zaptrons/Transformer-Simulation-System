> 🚧 Active Development

# Transformer Simulation System

A modular Python framework for distribution transformer simulation.

---

# Overview

This project models the hourly operation of a distribution transformer by combining:

* Ambient temperature
* Load profile
* Transformer operating state
* Time progression
* Daily reporting

The project is designed with clean architecture principles to make future expansion simple and maintainable.

---

# Current Features

* Hourly simulation engine
* Modular time management

  * Clock
  * Calendar
  * TimeEngine
* Temperature sensor simulation
* Load sensor simulation
* Transformer operating state calculation
* Daily report generation
* Dependency Injection architecture
* Clean separation of responsibilities

---

# Project Architecture

```text
Simulation
│
├── TimeEngine
│     ├── Clock
│     └── Calendar
│
├── TemperatureSensor
├── LoadSensor
├── Transformer
└── DailyReport
```

---

# Example Output

```python
{
    "Record Number": 125,
    "Hour": 14,
    "Day": 6,
    "Month": 3,
    "Year": 0,
    "Season": "Spring",

    "Ambient Temperature": 31.4,
    "Current Load": 482.3,
    "Load Percentage": 76.2,
    "Oil Temperature": 68.7
}
```

---

# Development Status

## Version 0.3

Current Status

- Stable simulation architecture
- Stable time management subsystem
- Stable simulation workflow
- Modular project structure

---

# Roadmap

## Version 0.4

* Improved transformer thermal model
* Better operating state calculations

## Version 0.5

* Historical statistical analysis
* Data visualization

## Version 0.6

* Multiple transformer simulation
* Network-level analysis

## Future Goals

* Automatic feeder load balancing
* Intelligent transformer loading analysis
* Distribution network optimization
* STM32 / ESP hardware integration
* Web dashboard

---

# Technologies

* Python
* Object-Oriented Programming (OOP)
* Dependency Injection
* Clean Architecture principles

---

# Author

**Hadi Norouzi**

Electrical & Embedded Systems Engineer

Repository:
https://github.com/Zaptrons/Transformer-Simulation-System