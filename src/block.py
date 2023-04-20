"""
Object to represent a cell in the maze grid

 Author: Toky
 Starting date: 16-04-2023
"""

class Block:

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        self.g = 0
        self.h = 0
        self.f = 0
        self.wall = False
        self.visited = False
        self.prev:Block = None
        self.neighbors:list[Block] = []

    def __repr__(self) -> str:
        return f"({self.i}, {self.j})"
    
    def __gt__(self, other) -> bool:
        return (self.i, self.j) > (other.i, other.j)
    
    def __lt__(self, other) -> bool:
        return (self.i, self.j) < (other.i, other.j)
    
    def __eq__(self, other) -> bool:
        if not other: return False
        return (self.i, self.j) == (other.i, other.j)

    def set_neighbors(self, grid):
        grid: list[list[Block]] = grid
        len_row = len(grid)
        len_col = len(grid[0])
        if self.j - 1 >= 0:
            self.neighbors.append(grid[self.i][self.j - 1])
        if self.j + 1 <= len_col-1:
            self.neighbors.append(grid[self.i][self.j + 1])
        if self.i - 1 >= 0:
            self.neighbors.append(grid[self.i - 1][self.j])
        if self.i + 1 <= len_row-1:
            self.neighbors.append(grid[self.i + 1][self.j])

    def to_rect(self, size: int):
        """Convert coordinates to rectangle

        Args:
            size (int): pixel size

        Returns:
            tuple: return a tuple (x , y, width, height) 
        """
        return (self.j * size, self.i * size, size, size)
