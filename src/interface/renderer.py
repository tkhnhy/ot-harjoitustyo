import pygame


class Renderer:
    """Class that draws pygame sprites on the screen.
    
    Args:
        display: What display the renderer should draw on
    """
    def __init__(self, display):
        self.display = display

    def render(self, sprites):
        """Draws the sprites and background, also names the display.
        
        Args:
            sprites: List of all the sprites that need to be drawn
        """
        self.display.fill((50, 50, 50))
        sprites.draw(self.display)
        pygame.display.set_caption("SHMUP")
        pygame.display.update()
