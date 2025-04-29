import pygame
from game_logic import GameLogic
from game_loop import GameLoop
from display import Display
from repositories.user_repository import UserRepository
from database_connection import get_database_connection


def main():
    pygame.init()
    user_repository = UserRepository(get_database_connection())
    game = GameLogic(user_repository)
    display = Display()
    loop = GameLoop(game, display)
    loop.start()


if __name__ == "__main__":
    main()
