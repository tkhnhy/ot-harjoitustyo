import unittest
from player import Player

class TestPlayer(unittest.TestCase):
	def setUp(self):
		self.player = Player(100, 100)

	def test_moveplayer(self):
		self.player.moveplayer(4, 0)
		
		self.assertEqual(self.player.rect.x, 104)