import pygame


class Player(pygame.sprite.Sprite):
    """The player controlled spaceship.

    Args:
        x: The ships starting x coordinate
        y: The ships starting y coordinate
    """

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("src/assets/sprites/spaceship.png")

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.speed = 5
        self.previous_shoot_time = 0

    def moveplayer(self, dx=0, dy=0):
        """Moves the player on the screen the specified amount.

        Args
            dx: How many pixels the ship moves in the x-axis
            dy: How many pixels the ship moves in the y-axis
        """
        self.rect.move_ip(dx, dy)

    def canshoot(self, current_time):
        """Checks if enough time has passed since the players previous shot to shoot again.
        Args:
            current_time: Time passed since the start of the program
        
        Returns:
            True if enough time has passed and a new shot is allowed, False if not enough time has passed
        """
        if current_time - self.previous_shoot_time >= 300:
            self.previous_shoot_time = current_time
            return True
        return False
    
    def update(self):
        pass
