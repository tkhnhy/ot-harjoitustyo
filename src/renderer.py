import pygame

class Renderer:
	def __init__(self, display):
		self.display = display
	
	def render(self, sprites):
		self.display.fill((100, 100, 100))
		sprites.draw(self.display)
		pygame.display.update()