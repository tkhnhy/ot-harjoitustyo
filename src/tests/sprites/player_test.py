import unittest
from sprites.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, 100)

    def test_moveplayer(self):
        self.player.moveplayer(4, 0)

        self.assertEqual(self.player.rect.x, 104)

    def test_canshoot_true(self):
        self.assertEqual(self.player.canshoot(1000), True)

    def test_canshoot_false(self):
        self.assertEqual(self.player.canshoot(100), False)

    def test_canshoot_change_previous(self):
        self.player.canshoot(1000)

        self.assertEqual(self.player.previous_shoot_time, 1000)
