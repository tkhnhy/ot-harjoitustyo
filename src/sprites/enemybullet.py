import pygame


class EnemyBullet1(pygame.sprite.Sprite):
    """A projectile shot by the enemies.
    
    Args:
        x: starting x position
        y: startin y position
        speed: how fast the bullet travels
    """
    def __init__(self, x, y, speed):
        super().__init__()

        self.image = pygame.image.load("src/assets/sprites/enemybullet.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def update(self):
        if self.rect.y > 856:
            self.kill()
        self.rect.move_ip(0, self.speed)
