import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("src/assets/sprites/boss.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.health = 30
        
        self.previous_shoot_time = 0
