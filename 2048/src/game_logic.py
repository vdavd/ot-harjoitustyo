import random
import numpy as np

class GameLogic:
    def __init__(self):
        self.grid = np.zeros((4, 4), dtype=int)
        self.init_grid()

    def add_tile(self):
        free_spaces = [(row, column) for row in range(4) for column in range(4) if self.grid[row, column] == 0]
        row, column = random.choice(free_spaces)
        tile_to_add = 4 if random.random() > 0.8 else 2
        self.grid[row, column] = tile_to_add

    def init_grid(self):
        self.add_tile()
        self.add_tile()

    def move_tiles(self,direction):
        pass

    def update_grid(self, direction):
        pass

    def __str__(self):
        return str(self.grid)