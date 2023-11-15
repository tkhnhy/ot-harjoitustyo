import pygame

class Player(pygame.sprite.Sprite):

	def __init__(self, x, y):
		super().__init__()
		
		self.speed = 2
        self.dx, self.dy = 0, 0

        #self.rect = self.(spritename).get_rect()
        self.rect.x = x
        self.rect.y = y
		
	def movement_controls(self):
        self.dx, self.dy = 0, 0
        controls = pygame.key.get_pressed()
        if controls[pygame.K_d]:
            self.dx = self.speed
        if controls[pygame.K_a]:
            self.dx = -self.speed
        if controls[pygame.K_s]:
            self.dy = self.speed
        if controls[pygame.K_w]:
            self.dy = -self.speed