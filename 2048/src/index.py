from game_logic import Game2048
from game_loop import GameLoop
from display import Display
import pygame
    

def main():
    pygame.init()
    game = Game2048()
    display = Display()
    loop = GameLoop(game, display)
    loop.start()

if __name__ == "__main__":
    main()