"""
 Algorithm A*, implemented with python
 
 Author: Toky
 Starting date: 16-04-2023
"""

from src.block import Block
from src.open_list import OpenList
from src.utils import manhattan_heuristic


class AStar:

    def __init__(self, grid: list[list[Block]], start: Block, end: Block):
        self.grid = grid
        self.start = start
        self.end = end
        self.open_list = OpenList(self.start)
        self.found = False
        self.path: list[Block] = []
        self.current: Block = None

    def backtrack(self):
        """Backtrack to the start of the maze to find the path
        """        
        self.path = []
        temp = self.current
        self.path.append(temp)
        while (temp.prev):
            self.path.append(temp)
            temp = temp.prev

    def find(self):
        """Find the shortest path in a maze from start position to end position
        """        
        size = self.open_list.size()
        self.current = self.open_list.get_priority()
        # self.current.h = manhattan_heuristic(self.current, self.end)
        # self.current.f = self.current.g + self.current.h
        if size != 0:
            if self.current == self.end:
                self.found = True
                self.backtrack()
            neighbors = self.current.neighbors
            for neighbor in neighbors:
                if not neighbor.visited and not neighbor.wall:
                    g = self.current.g + 1
                    if neighbor in self.open_list.all:
                        if neighbor.g > g:
                            neighbor.g = g
                    else:
                        neighbor.g = g
                        self.open_list.insert(neighbor)
                    neighbor.h = manhattan_heuristic(neighbor, self.end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.prev = self.current
            self.open_list.pop(self.current)
            # self.open_list.binary_pop(self.current)
            self.current.visited = True
