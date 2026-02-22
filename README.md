# reservation-analytics-system
A Python-based reservation system that analyzes booking data for vehicle and driving license services.

# Reservation Analytics System

## Project Overview
This project analyzes reservation data for vehicle and driving license services.
It calculates:
- Mean reservation count
- Maximum and minimum slots
- Most busy day
- Least busy day

## Data Structure
Each service contains:
[date, day name, [reservation slots]]

Example:
["13-04-2025", "Sunday", [4, 6, 7, 8, 1]]

## Functions
- calculate_mean(data)
- calculate_max(data)
- calculate_min(data)
- most_busy(data)
- least_busy(data)

## What I Learned
- How to work with nested lists
- How to write reusable functions
- How to analyze structured data