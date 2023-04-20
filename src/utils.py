
from src.block import Block
from src.constant import GRID20x20


def ascci_to_grid(ascii_grid:str) -> tuple[list[list[Block]], Block, Block]:
    """Convert a ascci_grid string to an array grid and specify the start and end positions

    Args:
        ascii_grid (str): grid string to convert. # the walls, I the start position and O the end position

    Returns:
        tuple: returns an array of block with start and end positions (grid, start, end)
    """    
    rows = ascii_grid.strip().split("\n")
    len_row = len(rows)
    len_col = len(rows[0])
    assert all(len_col == len(row) for row in rows), "The grid should be rectangular"
    grid = [[Block(i, j) for j in range(len_col)] for i in range(len_row)]
    for i in range(len_row):
        for j in range(len_col):
            if rows[i][j] == "#":
                grid[i][j].wall = True
            elif rows[i][j] == "I":
                start = grid[i][j]
            elif rows[i][j] == "O":
                end = grid[i][j]
    assert start != None and end != None, "Start and end must be specified"
    return (grid, start, end)


def initialise(grid:list[list[Block]]) -> None:
    """Set all neighbors of the all blocks in the grid

    Args:
        grid (list[list[Block]]): grid to be initialized
    """    
    for row in grid:
        for col in row:
            col.set_neighbors(grid)
            

def manhattan_heuristic(current:Block, target:Block) -> int:
    """Manhattan heuristic function for finding the distance between two blocks

    Args:
        current (Block): the current block
        target (Block): the target block

    Returns:
        int: manhattan distance between two blocks
    """    
    return abs(current.i - target.i) + abs(current.j - target.j)