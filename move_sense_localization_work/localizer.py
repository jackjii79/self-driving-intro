#!/usr/bin/python3.5
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    area = sum([len(grid[i]) for i in range(height)])
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row, width = [], len(grid[i])
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    #
    # TODO - implement this in part 2
    #
    for row in range(len(beliefs)):
        new_row = []
        for col in range(len(beliefs[row])):
            new_row.append(beliefs[row][col] * (int(grid[row][col] == color) * p_hit + (1 - int(grid[row][col] == color)) * p_miss))
        new_beliefs.append(new_row)
    return normalize(new_beliefs)

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    new_G = [[0.0 for i in range(len(beliefs[j]))] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy) % height
            new_j = (j + dx) % len(new_G[new_i])
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
