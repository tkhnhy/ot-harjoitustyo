import pygame
from interface.renderer import Renderer
from interface.display import Display
from game_loop import GameLoop
from sprites.player import Player
from clock import Clock
from highscores import Highscores
from event_queue import EventQueue


def main():

    pygame.init()

    display = Display()

    player = Player(236, 800)
    scoresystem = Highscores("src/highscores.csv")

    renderer = Renderer(display.give_display())
    clock = Clock()
    event_queue = EventQueue()

    game = GameLoop(clock, renderer, player, event_queue)

    game.loop()

    scoresystem.askname(game.score)
    scoresystem.printscore()


if __name__ == "__main__":
    main()
