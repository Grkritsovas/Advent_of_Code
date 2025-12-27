import os
import sys
from aocd import get_data

if __name__ == "__main__":
    year = int(sys.argv[1]) if len(sys.argv) > 1 else 2025
    base_folder = str(year)
    input_folder = os.path.join(base_folder, "inputs")

    if not os.path.exists(input_folder):
        os.makedirs(input_folder, exist_ok=True)

    for day in range(1, 26):
        filename = os.path.join(input_folder, f"input_{day:02}.txt")
        
        if os.path.exists(filename):
            continue
            
        print(f"Downloading Day {day}...")
        try:
            data = get_data(day=day, year=year)
            with open(filename, "w") as f:
                f.write(data)
        except Exception:
            print(f"Skipping Day {day}")