#!/usr/bin/python3
"""module.for perimeter of island"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid:"""
    perimeter = 0
    if not grid or not grid[0]:
        return 0
    for array_idx, array in enumerate(grid):
        for col_idx, col in enumerate(array):
            if col == 1:
                # check left
                before_idx = col_idx - 1
                before = 0
                if before_idx >= 0:
                    before = array[before_idx]
                if before == 0:
                    perimeter += 1
                # up
                up_index = array_idx - 1
                up = 0
                if up_index >= 0:
                    up = grid[up_index][col_idx]
                if up == 0:
                    perimeter += 1
                # down
                down_idx = array_idx + 1
                down = 0
                if down_idx < (len(grid) - 1):
                    down = grid[down_idx][col_idx]
                if down == 0:
                    perimeter += 1
                # right
                after_idx = col_idx + 1
                after = 0
                if col_idx < len(array):
                    after = array[after_idx]
                if after == 0:
                    perimeter += 1
                    break
    return perimeter
