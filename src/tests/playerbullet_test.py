import unittest
import pygame
from playerbullet import PlayerBullet


class TestPlayerBullet(unittest.TestCase):
    def setUp(self):
        self.playerbullet = PlayerBullet(50, 500)
        self.playerbullet2 = PlayerBullet(50, 0)

    def test_update(self):
        self.playerbullet.update()
        
        self.assertEqual(self.playerbullet.rect.y, 485)
    
    def test_update_kill(self):
        bullets = pygame.sprite.Group()
        bullets.add(self.playerbullet)
        bullets.add(self.playerbullet2)
        bullets.update()

        self.assertEqual(len(bullets), 1)