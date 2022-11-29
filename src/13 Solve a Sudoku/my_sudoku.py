import math

def sudoku_solver(full_grid):
    cell = get_empty_cell(full_grid)

    #print(cell)

    if not cell:
        return True
   
    for i in range(1, 10):
        placement = get_valid_placement(cell, full_grid, i)

        if placement:

            full_grid[cell[0]][cell[1]] = i

            if sudoku_solver(full_grid):
                return True
    
            full_grid[cell[0]][cell[1]] = 0
    return False
   

def get_empty_cell(full_grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if full_grid[i][j] == 0:
                return (i, j)
    return False

def get_valid_placement(cell, full_grid, val):
    one_dim_index = cell[0] * 9 + cell[1]
    x = math.floor(math.sqrt(one_dim_index))
    box_index = math.floor(one_dim_index % 9) // x + x * (one_dim_index // (9 * x))
    #subgrid_row = math.floor(box_index % (x * x))
    #subgrid_col = box_index // x * x
    subgrid_row = cell[0] - cell[0] % 3
    subgrid_col = cell[1] - cell[1] % 3

    for i in range(0, 9):
        if full_grid[cell[0]][i] == val:
            return False
        if full_grid[i][cell[1]] == val:
            return False

    # for k in range(subgrid_row, subgrid_row+3):
    #     for p in range(subgrid_col, subgrid_col+3):
    #         if full_grid[k][p] == val:
    #             return False
    for k in range(3):
        for j in range(3):
            if full_grid[k+subgrid_row][j+subgrid_col] == val:
                return False
    return True


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