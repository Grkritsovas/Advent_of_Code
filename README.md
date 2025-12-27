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
