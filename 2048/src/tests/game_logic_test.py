import unittest
import numpy as np
from game_logic import GameLogic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game_logic = GameLogic()

    def test_game_logic_object_initiates_correctly(self):
        zero_counts = np.count_nonzero(self.game_logic.grid == 0)
        two_counts = np.count_nonzero(self.game_logic.grid == 2)
        four_counts = np.count_nonzero(self.game_logic.grid == 4)

        self.assertEqual(zero_counts, 14)
        self.assertTrue(two_counts <= 2)
        self.assertTrue(four_counts <= 2)
