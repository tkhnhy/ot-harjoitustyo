import pygame

class Renderer:
	def __init__(self, display):
		self.display = display
	
	def render(self):
		self.display.fill((173, 173, 173))
		
		pygame.display.update()