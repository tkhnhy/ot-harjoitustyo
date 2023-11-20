import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load("src/assets/sprites/spaceship.png")
    
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
		
        self.dx = 0
        self.dy = 0

        self.keyleft = False
        self.keyright = False
        self.keyup = False
        self.keydown = False
    
    def moveplayer(self):
        self.rect.move_ip(self.dx, self.dy)
    
    def setplayerdirection(self, left=False, right=False, up=False, down=False):
        self.keyleft = left
        self.keyright = right
        self.keyup = up
        self.keydown = down

    def playermovement(self):
        if self.keyleft and not self.keyright:
            self.dx = -4