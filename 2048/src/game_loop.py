import pygame
from game_logic import Game2048
from display import Display

class GameLoop:
    def __init__(self, game: Game2048, display: Display):
        self.game = game
        self.display = display
        self.clock = pygame.time.Clock()

    def start(self):
        while True:
            if self.handle_input() == False:
                break

            self.display.draw_grid(self.game.grid)
            self.clock.tick(30)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.game.update_grid('right')
                if event.key == pygame.K_LEFT:
                    self.game.update_grid('left')
                if event.key == pygame.K_UP:
                    self.game.update_grid('up')
                if event.key == pygame.K_DOWN:
                    self.game.update_grid('down')
            elif event.type == pygame.QUIT:
                return False