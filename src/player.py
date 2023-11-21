import pygame
from pygame.constants import DROPTEXT

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load("src/assets/sprites/spaceship.png")
    
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
    def playercontrol(self, pressed_keys):
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -4)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, 4)
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(4, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 512:
            self.rect.right = 512
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 856:
            self.rect.bottom = 856
