import unittest
import numpy as np
import random
from game_logic import GameLogic
from repositories.user_repository import UserRepository
from database_connection import get_database_connection


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        random.seed(10)
        user_repository = UserRepository(get_database_connection())
        self.game_logic = GameLogic(user_repository)

    def test_game_logic_object_initiates_correctly(self):
        zero_counts = np.count_nonzero(self.game_logic.grid == 0)
        two_counts = np.count_nonzero(self.game_logic.grid == 2)
        four_counts = np.count_nonzero(self.game_logic.grid == 4)

        self.assertEqual(zero_counts, 14)
        self.assertTrue(two_counts <= 2)
        self.assertTrue(four_counts <= 2)

    def test_update_grid_works(self):
        grid = np.array([[0, 0, 0, 0], [0, 0, 0, 0],
                        [2, 0, 0, 8], [0, 2, 0, 2]])

        self.game_logic.update_grid('left')
        self.game_logic.update_grid('up')
        self.game_logic.update_grid('right')
        self.game_logic.update_grid('down')

        self.assertEqual(self.game_logic.grid.all(), grid.all())

    def test_str_representation_is_correct(self):
        self.game_logic.update_grid('left')

        self.assertEqual(str(self.game_logic),
                         '[[2 0 0 0]\n [0 0 0 0]\n [2 4 0 0]\n [0 0 0 0]]')
        
    def test_get_points_works(self):
        self.game_logic.update_grid('left')
        self.game_logic.update_points()

        self.assertEqual(self.game_logic.get_points(), 8)

    def test_get_state_works(self):
        self.assertEqual(self.game_logic.get_state(), "GAME")

    def test_check_victory_works(self):
        self.game_logic.grid = np.array([[2048,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]])
        self.game_logic.check_victory()

        self.assertEqual(self.game_logic.get_state(), "WIN")
