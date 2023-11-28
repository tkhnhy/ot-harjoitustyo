import pygame

class Player(pygame.sprite.Sprite):
	
	def __init__(self, x, y):
		super().__init__()
        
		self.image = pygame.image.load("src/assets/sprites/spaceship.png")
    
		self.rect = self.image.get_rect()
        
		self.rect.x = x
		self.rect.y = y
	
		self.speed = 5
		self.previous_shoot_time = 0

	def moveplayer(self, dx=0, dy=0):
		self.rect.move_ip(dx, dy)
	
	def canshoot(self, current_time):
		if current_time - self.previous_shoot_time >= 300:
			self.previous_shoot_time = current_time
			return True
		else:
			return False
			
	def update(self):
		pass