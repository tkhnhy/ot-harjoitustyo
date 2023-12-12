import pygame


class Enemy1(pygame.sprite.Sprite):
    """An enemy the player has to shoot.

    Args:
        x: Starting x-coordinate
        y: Starting y-coordinate
        pattern: Determines the speen and direction the enemy moves in
    """

    def __init__(self, x, y, pattern):
        super().__init__()

        self.image = pygame.image.load("src/assets/sprites/enemy1.png")

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.pattern = pattern
        self.previous_shoot_time = 0

        self.name = "AlienShip"

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
        """Checks if enough time has passed since the players previous shot to shoot again.
        Args:
            current_time: Time passed since the start of the program

        Returns:
            True if enough time has passed and a new shot is allowed, False if not
        """
        if self.rect.y < 0:
            return False
        if current_time - self.previous_shoot_time >= 2000:
            self.previous_shoot_time = current_time
            return True
        return False

    def update(self):
        """Updates the enemys state.

        Function that is called in gameloop every frame that either moves
        the enemy or destroys it if it has moved too far.

        """
        if self.rect.y > 856:
            self.kill()
        if self.rect.x < -1000:
            self.kill()
        if self.rect.x > 1500:
            self.kill()
        self.move(self.pattern)
