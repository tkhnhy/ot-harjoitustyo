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
		
        self.enemys_bullet_list = pygame.sprite.Group()
    
    def move(self, pattern):
        if pattern == 1:
            self.rect.move_ip(0, 5)
        if pattern == 2:
            self.rect.move_ip(0, 3)

    def shoot(self):
        bullet = EnemyBullet1(self.rect.x + 16, self.rect.y + 20, 10)
        self.enemys_bullet_list.add(bullet)
    
    def update(self):
        if self.rect.y > 856:
            self.kill()
        self.move(self.pattern)
        if self.rect.y < 0:
            pass
        else:
            self.shoot()

    def listbullets(self):
        return self.enemys_bullet_list