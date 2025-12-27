import re
import os

def _get_path(calling_script):
    """Internal helper to resolve input path from script name."""
    script_dir = os.path.dirname(calling_script)
    script_name = os.path.basename(calling_script)
    day_num = script_name.replace("day", "").replace("_", "").replace(".py", "")

    return os.path.join(script_dir, "inputs", f"input_{day_num}.txt")

def extract_ints(text):
    """Return all integers found in a string."""
    return [int(x) for x in re.findall(r'-?\d+', text)]

def read_grid(calling_script):
    """Returns a 2D list of characters from the input file."""
    grid = []
    with open(_get_path(calling_script)) as f:
        for line in f:
            if line.strip():
                grid.append(list(line.strip()))

    return grid

def read_input(calling_script, mode='lines'):
    """Returns input as list of strings (default) or raw string (mode='raw')."""
    with open(_get_path(calling_script)) as f:
        if mode == 'raw':
            return f.read()

        return [line.strip() for line in f if line.strip()]

def get_neighbors(grid, row, col, diagonals=False):
    """Returns valid neighbor coordinates (r, c)."""
    n_rows, n_cols = len(grid), len(grid[0])
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    
    if diagonals:
        deltas += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
    results = []
    for delta_row, delta_col in deltas:
        neighbor_row, neighbor_col = row + delta_row, col + delta_col
        if 0 <= neighbor_row < n_rows and 0 <= neighbor_col < n_cols:
            results.append((neighbor_row, neighbor_col))

    return results

def print_grid(grid):
    for row in grid:
        print("".join(str(x) for x in row))

    print()