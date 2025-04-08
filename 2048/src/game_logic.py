import random
import numpy as np


class GameLogic:
    def __init__(self):
        self.grid = np.zeros((4, 4), dtype=int)
        self.init_grid()

    def add_tile(self):
        free_spaces = [(row, column) for row in range(4)
                       for column in range(4) if self.grid[row, column] == 0]
        row, column = random.choice(free_spaces)
        tile_to_add = 4 if random.random() > 0.8 else 2
        self.grid[row, column] = tile_to_add

    def init_grid(self):
        self.add_tile()
        self.add_tile()

    def move_and_merge_tiles(self, grid: np.ndarray):
        new_grid = np.zeros_like(grid)
        for row in range(grid.shape[0]):
            first_merge = self.merge_row(grid[row])
            merged_row = self.merge_row(
                np.array(first_merge + [0] * (len(grid[row]) - len(first_merge))))
            new_grid[row] = np.array(
                merged_row + [0] * (len(grid[row]) - len(merged_row)))
        return new_grid

    def merge_row(self, row):
        skip = False
        merged_row = []
        compressed_row = row[row != 0]

        for i in range(len(compressed_row)):
            if skip:
                skip = False
                continue
            else:
                if i + 1 < len(compressed_row) and compressed_row[i] == compressed_row[i+1]:
                    merged_row.append(compressed_row[i]*2)
                    skip = True
                else:
                    merged_row.append(compressed_row[i])
        return merged_row

    def update_grid(self, direction):
        match direction:
            case 'left':
                self.grid = self.move_and_merge_tiles(np.copy(self.grid))
            case 'down':
                new_grid = self.move_and_merge_tiles(np.rot90(self.grid, k=-1))
                self.grid = np.rot90(new_grid, k=1)
            case 'right':
                new_grid = self.move_and_merge_tiles(np.rot90(self.grid, k=2))
                self.grid = np.rot90(new_grid, k=-2)
            case 'up':
                new_grid = self.move_and_merge_tiles(np.rot90(self.grid, k=1))
                self.grid = np.rot90(new_grid, k=-1)

        self.add_tile()

    def __str__(self):
        return str(self.grid)
