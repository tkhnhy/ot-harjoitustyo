import pygame
from enemybullet import EnemyBullet1

class Enemy1(pygame.sprite.Sprite):

    def __init__(self, x, y, pattern):
        super().__init__()

        self.image = pygame.image.load("src/assets/sprites/enemy1.png")

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.pattern = pattern
    
    def move(self, pattern):
        if pattern == 1:
            self.rect.move_ip(0, 5)
        if pattern == 2:
            self.rect.move_ip(0, 3)

    def canshoot(self):
        if self.rect.y < 0:
            return False
        else:
            return True
    
    def update(self):
        if self.rect.y > 856:
            self.kill()
        if 1056 < self.rect.x < -200:
            self.kill()
        self.move(self.pattern)