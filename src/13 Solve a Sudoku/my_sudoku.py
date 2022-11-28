import math

def sudoku_solver(full_grid):
    cell = get_empty_cell(full_grid)

    if not cell:
        return True
   
    placement = get_valid_placement(cell, full_grid)

    if not placement:
        return False

    return sudoku_solver(full_grid)
   

def get_empty_cell(full_grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if full_grid[i][j] == 0:
                return (i, j)
    return False

def get_valid_placement(cell, full_grid):
    for iteration in range(1, 10):
        row_valid = True
        col_valid = True
        subgrid_valid = True
        one_dim_index = cell[0] * 9 + cell[1]
        x = math.sqrt(one_dim_index)
        box_index = (one_dim_index % 9) / x + x * (one_dim_index / (9 * x))
        subgrid_row = box_index % x * x
        subgrid_col = box_index / x * x

        for i in range(0, 9):
            if full_grid[cell[0]][i] == iteration:
                row_valid = False
                break
            if full_grid[i][cell[1]] == iteration:
                col_valid = False
                break

        for k in range(subgrid_row, subgrid_row+3):
            for p in range(subgrid_col, subgrid_col+3):
                if full_grid[k][p] == iteration:
                    subgrid_valid = False
                    break

        if row_valid and col_valid and subgrid_valid:
            full_grid[cell[0]][cell[1]] = iteration
            return True
    return False


grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
sudoku_solver(grid)
print(grid)