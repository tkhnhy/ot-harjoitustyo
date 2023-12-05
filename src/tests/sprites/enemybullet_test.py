import unittest
import pygame
from sprites.enemybullet import EnemyBullet1


class TestEnemyBullet1(unittest.TestCase):
    def setUp(self):
        self.bullet1 = EnemyBullet1(100, 20, 10)
        self.bullet2 = EnemyBullet1(100, 900, 10)

    def test_update(self):
        self.bullet1.update()

        self.assertEqual(self.bullet1.rect.y, 30)

    def test_update_kill(self):
        bullets = pygame.sprite.Group()
        bullets.add(self.bullet1)
        bullets.add(self.bullet2)
        bullets.update()

        self.assertEqual(len(bullets), 1)
