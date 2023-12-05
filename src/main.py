import pygame
from interface.renderer import Renderer
from interface.display import Display
from game_loop import GameLoop
from sprites.player import Player
from clock import Clock
from highscores import Highscores


def main():

    pygame.init()

    display = Display()

    player = Player(236, 800)
    scoresystem = Highscores()

    renderer = Renderer(display.give_display())
    clock = Clock()

    game = GameLoop(clock, renderer, player)

    game.loop()

    scoresystem.writescore(game.score)
    scoresystem.readscore()


if __name__ == "__main__":
    main()
