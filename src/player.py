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

	def playercontrol(self, pressed_keys):
		
		if pressed_keys[pygame.K_w]:
			self.moveplayer(0, -self.speed)
		if pressed_keys[pygame.K_s]:
			self.moveplayer(0, self.speed)
		if pressed_keys[pygame.K_a]:
			self.moveplayer(-self.speed, 0)
		if pressed_keys[pygame.K_d]:
			self.moveplayer(self.speed, 0)
		
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > 512:
			self.rect.right = 512
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= 856:
			self.rect.bottom = 856

	def moveplayer(self, dx=0, dy=0):
		self.rect.move_ip(dx, dy)