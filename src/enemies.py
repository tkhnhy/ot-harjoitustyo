import pygame

class Enemy1(pygame.sprite.Sprite):

    def __init__(self, x, y, pattern):
        super().__init__()

        self.image = pygame.image.load("src/assets/sprites/enemy1.png")

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.pattern = pattern
		
    def move(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)

    def update(self):
        if self.pattern == 1:
            self.move(0, 5)
