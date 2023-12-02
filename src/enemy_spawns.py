import pygame
from enemies import Enemy1

class Enemy_Spawns:
	def __init__(self):
		self.wave1spawn = True
		self.wave2spawn = True
	
	def spawn(self, current_time):
		#Wave 1
		if current_time > 0 and self.wave1spawn:
			self.wave1spawn = False
			return self.wave1()			
		#Wave 2
		if current_time > 5000 and self.wave2spawn:
			self.wave2spawn = False
			return self.wave2()

	def wave1(self):
		enemy_list = [
			Enemy1(0, 0, 2),
			Enemy1(440, 0, 2),
			Enemy1(150, -500, 1),
			Enemy1(290, -500, 1)
			]
		return enemy_list

	def wave2(self):
		enemy_list = [
			Enemy1(0, 0, 2),
			Enemy1(440, 0, 2),
			Enemy1(150, -500, 1),
			Enemy1(290, -500, 1)
			]
		return enemy_list