import pygame

class GameLoop:

	def __init__(self, clock, renderer):
		self._clock = clock
		self._renderer = renderer
	def Loop(self):
		while True:
			self._clock.tick(30)
			self._renderer.render()