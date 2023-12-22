import pygame


class EventQueue:
    """Class that handles pygame events.
    """
    def get(self):
        """Returns the current pygame event.
        """
        return pygame.event.get()
