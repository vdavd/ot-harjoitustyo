import random
import numpy as np
from entities.user import User
from repositories.user_repository import UserRepository


class GameLogic:
    """Class that handles the internal logic of the game, 
    such as moving tiles and keeping track of points & game state.
    """

    def __init__(self, user_repository: UserRepository):
        """Class constructor that initiates the game.

        Args:
            user_repository (UserRepository): Repository object that handles 
            interfacing with the database.
        """
        self.grid = np.zeros((4, 4), dtype=int)
        self._points = 0
        self._state = "GAME"
        self._repository = user_repository
        self.init_user()
        self.init_game()
        self.update_points()

    def init_user(self, username="guest"):
        """Method that initiates the User object of the player.

        Args:
            username (str, optional): The player's username. 
            If a player with the given username exists, 
            fetches their info from the database. 
            Otherwise creates a new user in the database. Defaults to "guest".
        """
        user = self._repository.find_by_username(username)
        if user:
            self._user = user
        else:
            self._user = User(username)
            self._repository.create_user(self._user)

    def add_tile(self):
        """Method for adding a new tile to a free space in the grid with value 2 or 4.
        """
        free_spaces = [(row, column) for row in range(4)
                       for column in range(4) if self.grid[row, column] == 0]
        if not free_spaces:
            self.change_state("GAMEOVER")
        else:
            row, column = random.choice(free_spaces)
            tile_to_add = 4 if random.random() > 0.8 else 2
            self.grid[row, column] = tile_to_add

    def init_game(self):
        """Method for initiating the grid and game state. 
        Adds two tiles to an empty grid and changes state to GAME.
        """
        self.grid = np.zeros((4, 4), dtype=int)
        self._points = 0
        self.change_state("GAME")
        self.add_tile()
        self.add_tile()

    def move_and_merge_tiles(self, grid: np.ndarray):
        """Method that handles the calculations of moving and merging tiles in the grid.

        Args:
            grid (np.ndarray): The game grid.

        Returns:
            The new grid.
        """
        new_grid = np.zeros_like(grid)
        for row in range(grid.shape[0]):
            first_merge = self.merge_row(grid[row])
            merged_row = self.merge_row(
                np.array(first_merge + [0] * (len(grid[row]) - len(first_merge))))
            new_grid[row] = np.array(
                merged_row + [0] * (len(grid[row]) - len(merged_row)))
        return new_grid

    def merge_row(self, row):
        """Method for handling the calculations of merging a row in the grid.

        Args:
            row: A row of the grid.

        Returns:
            A merged row.
        """
        skip = False
        merged_row = []
        compressed_row = row[row != 0]

        for i in range(len(compressed_row)):
            if skip:
                skip = False
            else:
                if i + 1 < len(compressed_row) and compressed_row[i] == compressed_row[i+1]:
                    merged_row.append(compressed_row[i]*2)
                    skip = True
                else:
                    merged_row.append(compressed_row[i])
        return merged_row

    def update_grid(self, direction):
        """Method for updating the grid according to the user input, 
        with move_and_merge_tiles method. Finally, adds a tile.

        Args:
            direction: The direction of the user input that 
            tells in which direction to move the tiles.
        """
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

    def check_victory(self):
        """Checks whether the 2048 tile exists in the grid. 
        If so, change game state to WIN.
        """
        if 2048 in self.grid:
            self.change_state("WIN")

    def update_points(self):
        """Updates the points and user hiscore, if applicable.
        """
        self._points = self.grid.sum()
        self._user.update_hiscore(self._points)

    def get_points(self):
        """Return the points of the player.

        Returns:
            The player's points.
        """
        return self._points

    def change_state(self, state):
        """Changes the game state.

        Args:
            state: the new game state.
        """
        self._state = state

    def get_state(self):
        """Returns the game state.

        Returns:
            The game state.
        """
        return self._state

    def save_score(self):
        """Saves the new hiscore in the database.
        """
        self._repository.update_hiscore(self._user)

    def get_hiscore(self):
        """Returns the player's hiscore.

        Returns:
            The player's hiscore.
        """
        return self._user.get_hiscore()

    def __str__(self):
        """String representation of the class object.

        Returns:
            The string representation for the game grid.
        """
        return str(self.grid)
