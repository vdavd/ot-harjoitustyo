import pygame
from game_logic import GameLogic
from game_loop import GameLoop
from display import Display


def main():
    pygame.init()
    game = GameLogic()
    display = Display()
    loop = GameLoop(game, display)
    loop.start()


if __name__ == "__main__":
    main()
