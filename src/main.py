import pygame
from renderer import Renderer
from game_loop import GameLoop


def main():
	display_height = 856
	display_width = 512
	display = pygame.display.set_mode((display_width, display_height))
	
	renderer = Renderer(display)
	clock = pygame.time.Clock()
	
	pygame.init()
	
	game = GameLoop(clock, renderer)
	
	game.Loop()
	
		
if __name__ == "__main__":
	main()