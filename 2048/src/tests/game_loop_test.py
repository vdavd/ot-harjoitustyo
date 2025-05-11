import pygame
import unittest
import random
import numpy as np
from game_logic import GameLogic
from game_loop import GameLoop
from unittest.mock import Mock
from repositories.user_repository import UserRepository
from database_connection import get_database_connection

class MockClock:
    def tick(self, fps):
        pass

class MockEvent:
    def __init__(self, event_type, key=None):
        self.type = event_type
        self.key = key

class MockEventQueue:
    def __init__(self, events=[]):
        self._events = events

    def get(self):
        return self._events
    


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        random.seed(10)
        user_repository = UserRepository(get_database_connection())
        self.game_logic = GameLogic(user_repository)
        self.mock_display = Mock()
        self.mock_clock = MockClock()
        self.mock_event_queue = MockEventQueue([MockEvent(pygame.KEYDOWN, pygame.K_LEFT), MockEvent(pygame.QUIT)])

    def test_draw_grid_is_called_when_state_is_game(self):
        game_loop = GameLoop(self.game_logic, self.mock_display,
                             self.mock_event_queue, self.mock_clock)
        game_loop.start()

        self.mock_display.draw_grid.assert_called()

    def test_draw_win_is_called_when_state_is_win(self):
        self.game_logic.grid = np.array(
            [[2048, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        game_loop = GameLoop(self.game_logic, self.mock_display,
                             self.mock_event_queue, self.mock_clock)
        game_loop.start()

        self.mock_display.draw_win.assert_called()
