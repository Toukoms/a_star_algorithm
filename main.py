import pygame
from pygame.constants import *
from src.maze import Maze
from src.constant import GRID10x10, GRID20x20, GRID40x40, GRID60x60
from src.utils import ascci_to_grid, initialise

pygame.init()

grid, start, end = ascci_to_grid(GRID60x60)
initialise(grid)

ROW, COL = len(grid), len(grid[0])
SIZE = 640//ROW
WIDTH = SIZE * COL
HEIGHT = SIZE * ROW

labyrinth = Maze(grid, start, end)
timer = pygame.time.Clock()

def show_gird():
    for row in grid:
        for col in row:
            if col.wall:
                color = pygame.color.THECOLORS["black"]  # (0, 0, 0)
            else:
                color = pygame.color.THECOLORS["white"]  # (255, 255, 255)
            pygame.draw.rect(window, color, col.to_rect(SIZE))


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* algorithm")

font_text = pygame.font.SysFont("arial", 10)

window.fill((255, 255, 255))
show_gird()

run = True

while run:
    
    for block in labyrinth.open_list.all:
        pygame.draw.rect(window, pygame.color.THECOLORS["green"], block.to_rect(SIZE))
        
    for row in grid:
        for col in row:
            if col.visited:
                pygame.draw.rect(window, pygame.color.THECOLORS["red"], col.to_rect(SIZE))
            # if not col.wall:
            #     info = font_text.render(f"{col.g} + {col.h} = {col.f}", 1, (0, 0, 0))
            #     window.blit(info, col.to_rect(SIZE))
                
    # draw the start position
    pygame.draw.rect(window, pygame.color.THECOLORS["aqua"], start.to_rect(SIZE))
    
    if not labyrinth.found:
        labyrinth.find()
    else:
        for block in labyrinth.path:
            pygame.draw.rect(window, pygame.color.THECOLORS["blue"], block.to_rect(SIZE))
        # run = False
    
    # draw the end position        
    pygame.draw.rect(window, pygame.color.THECOLORS["yellow"], end.to_rect(SIZE))
    
    for e in pygame.event.get():
        if e.type == QUIT:
            run = False
    
    pygame.display.flip()
    # timer.tick(30)

pygame.quit()
