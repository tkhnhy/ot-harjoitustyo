import pygame
from pygame.constants import DROPTEXT

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load("src/assets/sprites/spaceship.png")
    
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

        self.keyleft = False
        self.keyright = False
        self.keyup = False
        self.keydown = False
        
    def playercontrol(self, pressed_keys):
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -4)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, 4)
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(4, 0)
    
    def setplayerdirection(self, left=False, right=False, up=False, down=False):
        self.keyleft = left
        self.keyright = right
        self.keyup = up
        self.keydown = down
