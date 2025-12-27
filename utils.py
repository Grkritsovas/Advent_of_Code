import re

# 1. Parsing Numbers only from a string
def extract_ints(text):
    """
    Finds all integers in a string. 
    "Game 1: 3 blue, 4 red" -> [1, 3, 4]
    """
    return [int(x) for x in re.findall(r'-?\d+', text)]

# 2. Grid Reader
def read_grid(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                grid.append(list(line.strip()))
    return grid

# 3. Neighbors (4, or 8 with diagonals=True)
def get_neighbors(grid, row, col, diagonals=False):
    """
    Returns a list of (r, c) tuples for valid neighbors within bounds.
    """
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

# 4. Prints a grid nicely
def print_grid(grid):
    for row in grid:
        print("".join(str(x) for x in row))
    print()