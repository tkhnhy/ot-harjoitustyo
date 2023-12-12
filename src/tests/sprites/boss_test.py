import unittest
from sprites.boss import Boss

class TestBoss(unittest.TestCase):
    def setUp(self):
        self.boss = Boss(100, 200)