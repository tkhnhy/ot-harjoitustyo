import unittest
import pygame
from sprites.player import Player
from game_loop import GameLoop


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0


class StubRenderer:
    def render(self, sprites):
        pass


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self.events = events

    def get(self):
        return self.events


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        events = []
        self.gameloop = GameLoop(
            StubClock(),
            StubRenderer(),
            Player(236, 800),
            StubEventQueue(events)
        )

    def test_spawn_wave1(self):
        self.gameloop.spawn(100)
        num_of_enemies = len(self.gameloop.all_enemies)
        self.assertEqual(num_of_enemies, 4)
