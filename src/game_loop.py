import pygame

class GameLoop:

	def __init__(self, clock, renderer, player):
		self._clock = clock
		self._renderer = renderer
		self._player = player

	def Loop(self):
	
		run = True
		fps = 30
	
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
			
			pressed_keys = pygame.key.get_pressed()
				
			self._player.playercontrol(pressed_keys)
			self._clock.tick(fps)
			self._renderer.render()
			
			