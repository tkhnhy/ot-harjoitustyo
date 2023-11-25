import pygame
from renderer import Renderer
from game_loop import GameLoop
from player import Player


def main():

	pygame.init()
	
	display_height = 856
	display_width = 512
	display = pygame.display.set_mode((display_width, display_height))
	
	player = Player(236, 800)

	renderer = Renderer(display)
	clock = pygame.time.Clock()
	
	game = GameLoop(clock, renderer, player)
	
	
	game.Loop()
	
		
if __name__ == "__main__":
	main()