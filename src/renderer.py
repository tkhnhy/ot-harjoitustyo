import pygame


class Renderer:
    def __init__(self, display):
        self.display = display

    def render(self, sprites):
        self.display.fill((50, 50, 50))
        sprites.draw(self.display)
        pygame.display.set_caption("SHMUP")
        pygame.display.update()
