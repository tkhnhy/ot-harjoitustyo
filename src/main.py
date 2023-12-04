import pygame
from renderer import Renderer
from game_loop import GameLoop
from player import Player
from clock import Clock
from highscores import Highscores


def main():

    pygame.init()

    display_height = 856
    display_width = 512
    display = pygame.display.set_mode((display_width, display_height))

    player = Player(236, 800)
    scoresystem = Highscores()

    renderer = Renderer(display)
    clock = Clock()

    game = GameLoop(clock, renderer, player)

    game.loop()

    scoresystem.writescore(game.score)
    scoresystem.readscore()

if __name__ == "__main__":
    main()
