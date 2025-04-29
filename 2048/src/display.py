import pygame


class Display:
    """Class fro handling the game display.
    """    
    def __init__(self):
        """Class constructor that declares constants for the display and initiates the screen.
        """        
        self._tile_size = 100
        self._margin = 5
        self._upper_margin = 50
        self._width = 4 * (self._tile_size + self._margin) + self._margin
        self._height = self._width + self._upper_margin
        self._bg_color = (184, 171, 165)
        self._tile_colors = {
            0:    (205, 193, 180),
            2:    (238, 228, 218),
            4:    (237, 224, 200),
            8:    (242, 177, 121),
            16:   (245, 149, 99),
            32:   (246, 124, 95),
            64:   (246, 94, 59),
            128:  (237, 207, 114),
            256:  (215, 180, 97),
            512:  (170, 160, 230),
            1024: (195, 130, 240),
            2048: (240, 100, 200)
        }
        self._font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("2048")

    def draw_points(self, points: int):
        """Method for drawing the player's points on top of the screen.

        Args:
            points (int): The player's points.
        """        
        text = self._font.render(f"Points: {points}", True, (0, 0, 0))
        text_rect = text.get_rect(center=(100, self._upper_margin //2))
        self.screen.blit(text, text_rect)

    def draw_hiscore(self, hiscore: int):
        """Method for drawing the player's hiscore on top of the screen.

        Args:
            hiscore (int): The player's hiscore.
        """        
        text = self._font.render(f"Hiscore: {hiscore}", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self._width - 100, self._upper_margin //2))
        self.screen.blit(text, text_rect)

    def draw_grid(self, grid, points, hiscore):
        """Method for drawing the main view of the game, including the game grid, points and hiscore.

        Args:
            grid: The game grid.
            points: The player's points
            hiscore: The player's hiscore.
        """        
        self.screen.fill(self._bg_color)

        self.draw_points(points)
        self.draw_hiscore(hiscore)

        for row in range(4):
            for column in range(4):

                tile_value = grid[row, column]

                tile_color = self._tile_colors.get(tile_value)

                x = column * (self._tile_size + self._margin) + self._margin
                y = row * (self._tile_size + self._margin) + self._margin + self._upper_margin

                pygame.draw.rect(self.screen, tile_color, (x, y,
                                 self._tile_size, self._tile_size), border_radius=8)

                if tile_value > 0:
                    text = self._font.render(str(tile_value), True, (0, 0, 0))
                    text_rect = text.get_rect(
                        center=(x + self._tile_size // 2, y + self._tile_size // 2))
                    self.screen.blit(text, text_rect)

        pygame.display.flip()

    def draw_gameover(self):
        """Method for drawing the game over -screen.
        """        
        text = self._font.render('GAME OVER', True, (0, 0, 0))
        text_rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, text_rect)
        text = self._font.render('PRESS R TO RESTART', True, (0, 0, 0))
        text_rect = text.get_rect(center=(self._width // 2, self._height // 2 + 50))
        self.screen.blit(text, text_rect)

        pygame.display.flip()

    def draw_win(self):
        """Method for drawing the victory screen.
        """        
        text = self._font.render('YOU WON!', True, (252, 15, 192))
        text_rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, text_rect)
        text = self._font.render('PRESS R FOR NEW GAME', True, (252, 15, 192))
        text_rect = text.get_rect(center=(self._width // 2, self._height // 2 + 50))
        self.screen.blit(text, text_rect)

        pygame.display.flip()
