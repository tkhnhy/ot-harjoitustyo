import unittest
import pygame
from sprites.enemies import Enemy1


class TestEnemy1(unittest.TestCase):
    def setUp(self):
        self.enemyp1 = Enemy1(100, 100, 1)
        self.enemyp2 = Enemy1(100, -10, 2)

    def test_move_pat1(self):
        self.enemyp1.move(1)

        self.assertEqual(self.enemyp1.rect.y, 105)

    def test_move_pat2(self):
        self.enemyp2.move(2)

        self.assertEqual(self.enemyp2.rect.y, -7)

    def test_canshoot_true(self):
        self.assertEqual(self.enemyp1.canshoot(2000), True)

    def test_canshoot_false_y(self):
        self.assertEqual(self.enemyp2.canshoot(2000), False)

    def test_canshoot_false_time(self):
        self.assertEqual(self.enemyp1.canshoot(1000), False)

    def test_canshoot_change_previous(self):
        self.enemyp1.canshoot(2000)

        self.assertEqual(self.enemyp1.previous_shoot_time, 2000)

    def test_update_move(self):
        self.enemyp1.update()

        self.assertEqual(self.enemyp1.rect.y, 105)

    def test_update_death(self):
        enemies = pygame.sprite.Group()
        enemydie = Enemy1(5000, 5000, 1)
        enemies.add(enemydie)
        enemydie.update()

        self.assertEqual(len(enemies), 0)
