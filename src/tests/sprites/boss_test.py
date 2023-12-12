import unittest
from sprites.boss import Boss


class TestBoss(unittest.TestCase):
    def setUp(self):
        self.boss = Boss(100, 200)

    def test_reduce_health(self):
        self.boss.reduce_health()
        self.assertEqual(self.boss.health, 29)

    def test_canshoot_true(self):
        self.assertEqual(self.boss.canshoot(2000), True)

    def test_canshoot_false(self):
        self.assertEqual(self.boss.canshoot(800), False)
