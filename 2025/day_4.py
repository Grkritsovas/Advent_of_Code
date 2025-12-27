import copy

INPUT_FILE = "inputs/input_04.txt"

def count_neighbors(grid, row, col):
    adjacent = 0
    for adjacent_row in range(max(row - 1, 0), min(row + 1, n_rows - 1) + 1):
        for adjacent_col in range(max(col - 1, 0), min(col + 1, n_cols - 1) + 1):
            if adjacent_row == row and adjacent_col == col: #don't count the cell itself
                continue
            if grid[adjacent_row][adjacent_col] == '@':
                adjacent += 1
    
    return adjacent

# Part 1
def part_1(grid, n_rows, n_cols):
    total = 0

    for row in range(n_rows):
        for column in range(n_cols):
            if grid[row][column] == '@' and count_neighbors(grid, row, column) < 4:
                total += 1

    return total

# Part 2
def part_2(grid, n_rows, n_cols):
    def scan_and_remove(grid):
        removed_this_round = 0
        for row in range(n_rows):
            for column in range(n_cols):
                if grid[row][column] == '@' and count_neighbors(grid, row, column) < 4:
                    removed_this_round += 1
                    grid[row][column] = 'X' # mutate
        return removed_this_round

    total_removed = 0
    while True:
        delta = scan_and_remove(grid)
        if delta == 0:
            break
        total_removed += delta

    return total_removed

if __name__ == '__main__':
    grid = []
    with open(INPUT_FILE) as f:
        for line in f:
            if line.strip():
                grid.append(list(line.strip()))

    n_rows = len(grid)
    n_cols = len(grid[0])

    print(f'Part 1: {part_1(grid, n_rows, n_cols)}')

    grid_copy = list(map(list, grid))
    print(f'Part 2: {part_2(grid_copy, n_rows, n_cols)}')