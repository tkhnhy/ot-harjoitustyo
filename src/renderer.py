import pygame

class Renderer:
	def __init__(self, display, sprites):
		self.display = display
		self.sprites = sprites
	
	def render(self):
		self.display.fill((100, 100, 100))
		self.sprites.draw(self.display)
		pygame.display.update()