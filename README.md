# Advent of Code Solutions

Monorepo for my [Advent of Code](https://adventofcode.com/) solutions.

## Structure

```mermaid
graph TD
    Root[Advent_of_Code] --> Utils[utils.py]
    Root --> Setup[setup_inputs.py]
    Root --> Year[2025 /]
    Year --> Inputs[inputs /]
    Year --> Script[day01.py]
```
### Instructions

setup_inputs.py: Downloads inputs for the year.

utils.py: Shared helpers (input reading, grid parsing, math).

inputs/: Auto-generated folder (ignored by Git).
