import pygame
from game_logic import GameLogic
from display import Display


class GameLoop:
    """Class that handles the main game loop and input events.
    """    
    def __init__(self, game: GameLogic, display: Display):
        """Class constructor that initiates the game loop object.

        Args:
            game (GameLogic): The game logic object.
            display (Display): The display object.
        """        
        self.game = game
        self.display = display
        self.clock = pygame.time.Clock()

    def start(self):
        """Method for starting the main loop of the game. Checks the game state and changes game behavior based on it.
        """        
        while True:
            self.handle_input()

            match self.game.get_state():
                case "GAME":
                    self.display.draw_grid(self.game.grid, self.game.get_points(), self.game.get_hiscore())
                case "QUIT":
                    self.game.save_score()
                    break
                case "GAMEOVER":
                    self.display.draw_gameover()
                case "WIN":
                    self.display.draw_grid(self.game.grid, self.game.get_points(), self.game.get_hiscore())
                    self.display.draw_win()
            self.clock.tick(15)

    def handle_input(self):
        """Method for handling user input events: restarting the game, moving tiles and quitting.
        """        
        for event in pygame.event.get():
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

            elif event.type == pygame.QUIT:
                self.game.change_state("QUIT")
