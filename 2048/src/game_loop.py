import pygame
from game_logic import GameLogic
from display import Display
from event_queue import EventQueue
from clock import Clock


class GameLoop:
    """Class that handles the main game loop and input events.
    """

    def __init__(self, game: GameLogic, display: Display, event_queue: EventQueue, clock: Clock):
        """Class constructor that initiates the game loop object.

        Args:
            game (GameLogic): The game logic object.
            display (Display): The display object.
            event_queue (EventQueue): The queue of pygame input events.
            clock (Clock): Pygame clock object.
        """
        self.game = game
        self.display = display
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        """Method for starting the main loop of the game. 
        Checks the game state and changes game behavior based on it.
        """
        while True:
            self.handle_input()

            match self.game.get_state():
                case "GAME":
                    self.display.draw_grid(
                        self.game.grid, self.game.get_points(), self.game.get_hiscore())
                case "QUIT":
                    self.game.save_score()
                    break
                case "GAMEOVER":
                    self.display.draw_gameover()
                case "WIN":
                    self.display.draw_grid(
                        self.game.grid, self.game.get_points(), self.game.get_hiscore())
                    self.display.draw_win()
            self._clock.tick(15)

    def handle_input(self):
        """Method for handling user input events: restarting the game, moving tiles and quitting.
        """
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.game.init_game()

                if self.game.get_state() == "GAME":
                    if event.key == pygame.K_RIGHT:
                        self.game.update_grid('right')
                    if event.key == pygame.K_LEFT:
                        self.game.update_grid('left')
                    if event.key == pygame.K_UP:
                        self.game.update_grid('up')
                    if event.key == pygame.K_DOWN:
                        self.game.update_grid('down')

                    self.game.update_points()
                    self.game.check_victory()

                    return

            elif event.type == pygame.QUIT:
                self.game.change_state("QUIT")
