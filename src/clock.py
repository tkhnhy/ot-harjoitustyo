import pygame


class Clock:
    """Class that contains the clock used to control games time.
    """
    def __init__(self):
        self.clock = pygame.time.Clock()

    def tick(self, fps):
        """Makes the clock update.
        """
        self.clock.tick(fps)

    def get_ticks(self):
        """Returns passed time as ticks.
        """
        return pygame.time.get_ticks()
