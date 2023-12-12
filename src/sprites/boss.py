import pygame


class Boss(pygame.sprite.Sprite):
    """A boss enemy.
    
    Args:
        x: starting x position
        y: starting y position
    """
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("src/assets/sprites/boss.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.health = 30

        self.previous_shoot_time = 0
        self.fireseq = 1

        self.name = "BossAlien"

    def reduce_health(self):
        """Reduces the bosses health.
        """
        self.health -= 1

    def canshoot(self, current_time):
        """Checks if enough time has passed since the players previous shot to shoot again.
        Args:
            current_time: Time passed since the start of the program

        Returns:
            True if enough time has passed and a new shot is allowed, False if not
        """
        if self.rect.y < -70:
            return False
        if current_time - self.previous_shoot_time >= 1000:
            self.previous_shoot_time = current_time
            return True
        return False

    def move(self):
        if self.rect.y < -50:
            self.rect.move_ip(0, 2)
        else:
            pass

    def setfire(self, mode):
        self.fireseq = mode

    def update(self):
        self.move()
