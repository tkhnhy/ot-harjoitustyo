import pygame

class PlayerBullet(pygame.sprite.Sprite):

	def __init__(self, x, y):
		super().__init__()
		
		self.image = pygame.image.load("src/assets/sprites/playerbullet.png")
		self.rect = self.image.get_rect()
		
		self.rect.x = x
		self.rect.y = y
		
		self.speed = 15
	
	def update(self):
		self.rect.move_ip(0, -self.speed)
		if self.rect.y < 0:
			self.kill()
