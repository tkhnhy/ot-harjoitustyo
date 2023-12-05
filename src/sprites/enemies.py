import pygame
from sprites.enemybullet import EnemyBullet1


class Enemy1(pygame.sprite.Sprite):

    def __init__(self, x, y, pattern):
        super().__init__()

        self.image = pygame.image.load("src/assets/sprites/enemy1.png")

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.pattern = pattern
        self.previous_shoot_time = 0

    def move(self, pattern):
        if pattern == 1:
            self.rect.move_ip(0, 5)
        if pattern == 2:
            self.rect.move_ip(0, 3)
        if pattern == 3:
            self.rect.move_ip(4, 0)
        if pattern == 4:
            self.rect.move_ip(-4, 0)

    def get_pattern(self):
        return self.pattern

    def canshoot(self, current_time):
        if self.rect.y < 0:
            return False
        elif current_time - self.previous_shoot_time >= 2000:
            self.previous_shoot_time = current_time
            return True
        else:
            return False

    def update(self):
        if self.rect.y > 856:
            self.kill()
        if self.rect.x < -1000:
            self.kill()
        if self.rect.x > 1500:
            self.kill()
        self.move(self.pattern)