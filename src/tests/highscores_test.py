import unittest
from highscores import Highscores

class TestHighscores(unittest.TestCase):
    def setUp(self):
        self.highscore_handler = Highscores("src/tests/test_highscore.csv")