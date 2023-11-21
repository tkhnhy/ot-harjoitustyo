import pygame

class PlayerBullet(pygame.sprite.Sprite):

	def __init__(self, x, y):
		super().__init__()
		
		#self.image = 
		#self.rect = self.image.get_rect()
		
		self.rect.x = x
		self.rect.y = y
		
		self.speed = 8
	
	def bulletmove(self):
		self.rect.move_ip(0, -speed)
		
class EnemyBullet1(pygame.sprite.Sprite):

	def __init__(self, x, y):
		super().__init__()
		
		#self.image = 
		#self.rect = self.image.get_rect()
		
		self.rect.x = x
		self.rect.y = y
		
		self.speed = 8
	
	def bulletmove(self):
		self.rect.move_ip(0, speed)