import pygame
from pygame.constants import DROPTEXT

class Player(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		super().__init__()
        
		self.image = pygame.image.load("src/assets/sprites/spaceship.png")
    
		self.rect = self.image.get_rect()
        
		self.rect.x = x
		self.rect.y = y
	
		self.speed = 5

	def moveplayer(self, dx=0, dy=0):
		self.rect.move_ip(dx, dy)

	def update(self):
		pass