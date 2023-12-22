import unittest
import pygame
from sprites.player import Player
from game_loop import GameLoop
from sprites.enemies import Enemy1
from sprites.playerbullet import PlayerBullet
from sprites.enemybullet import EnemyBullet1


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

    def test_pbullet_enemy_coll(self):
        test_enemy = Enemy1(100, 100, 1)
        test_bullet = PlayerBullet(100, 100)

        self.gameloop.all_sprites_group.add(test_enemy)
        self.gameloop.all_enemies.add(test_enemy)
        self.gameloop.all_player_bullets_group.add(test_bullet)
        self.gameloop.all_sprites_group.add(test_bullet)

        pre_len = len(self.gameloop.all_enemies)
        self.gameloop.check_pbullet_enemy_coll()

        self.assertGreater(pre_len, len(self.gameloop.all_enemies))

    def test_ebullet_player_coll(self):
        test_ebullet = EnemyBullet1(236, 800, 5)

        self.gameloop.all_sprites_group.add(test_ebullet)
        self.gameloop.enemy_bullets.add(test_ebullet)

        pre_len = len(self.gameloop.playergroup)

        self.gameloop.check_ebullet_player_coll()

        self.assertGreater(pre_len, len(self.gameloop.playergroup))

    def test_enemy_player_coll(self):
        test_enemy = Enemy1(236, 800, 1)

        self.gameloop.all_sprites_group.add(test_enemy)
        self.gameloop.all_enemies.add(test_enemy)

        pre_len = len(self.gameloop.playergroup)

        self.gameloop.check_enemy_player_coll()

        self.assertGreater(pre_len, len(self.gameloop.playergroup))