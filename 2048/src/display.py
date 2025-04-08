import pygame


class Display:
    def __init__(self):
        self._tile_size = 100
        self._margin = 5
        self._width = 4 * (self._tile_size + self._margin) + self._margin
        self._height = self._width
        self._bg_color = (184, 171, 165)
        self._tile_colors = {
            0: (200, 190, 175),
            2: (235, 225, 215),
            4: (240, 226, 200),
            8: (240, 175, 118),
        }
        self._font = pygame.font.Font(None, 36)
        self.screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("2048")

    def draw_grid(self, grid):
        self.screen.fill(self._bg_color)

        for row in range(4):
            for column in range(4):

                tile_value = grid[row, column]

                tile_color = self._tile_colors.get(tile_value)

                x = column * (self._tile_size + self._margin) + self._margin
                y = row * (self._tile_size + self._margin) + self._margin

                pygame.draw.rect(self.screen, tile_color, (x, y,
                                 self._tile_size, self._tile_size), border_radius=8)

                if tile_value > 0:
                    text = self._font.render(str(tile_value), True, (0, 0, 0))
                    text_rect = text.get_rect(
                        center=(x + self._tile_size // 2, y + self._tile_size // 2))
                    self.screen.blit(text, text_rect)

        pygame.display.flip()
