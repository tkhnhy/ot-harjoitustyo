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
			self._player.setplayerdxdy()
			controls = pygame.key.get_pressed()
			if controls[pygame.K_d]:
				self._player.setplayerdxdy(dx = 4)
			if controls[pygame.K_a]:
				self._player.setplayerdxdy(dx = -4)
			if controls[pygame.K_s]:
				self._player.setplayerdxdy(dy = 4)
			if controls[pygame.K_w]:
				self._player.setplayerdxdy(dy = -4)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
			
			self._player.moveplayer()		
			self._clock.tick(fps)
			self._renderer.render()
			
			