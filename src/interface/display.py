import pygame


class Display:
    def __init__(self):
        self.display_height = 856
        self.display_width = 512

    def give_display(self):
        return pygame.display.set_mode((self.display_width, self.display_height))
