import unittest
from enemy_spawns import EnemySpawns
from arrangements import Arrangements

class TestEnemySpawns(unittest.TestCase):
    def setUp(self):
        self.spawner = EnemySpawns()
        self.ref_arrangements = Arrangements()

    def test_change_wave(self):
        self.spawner.change_wave_count(3)
        self.assertEqual(self.spawner.wave_count, 3)

    def test_no_wave(self):
        self.spawner.change_wave_count(6)
        enemies = self.spawner.spawn(500)

        self.assertEqual(enemies, None)
        
    def test_spawn_wave1(self):
        enemies = self.spawner.spawn(100)
        ref_enemies = self.ref_arrangements.arrangement1()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave2(self):
        self.spawner.change_wave_count(1)
        enemies = self.spawner.spawn(6000)
        ref_enemies = self.ref_arrangements.arrangement1()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave3(self):
        self.spawner.change_wave_count(2)
        enemies = self.spawner.spawn(8000)
        ref_enemies = self.ref_arrangements.arrangement2()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave4(self):
        self.spawner.change_wave_count(3)
        enemies = self.spawner.spawn(12000)
        ref_enemies = self.ref_arrangements.arrangement3()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave5(self):
        self.spawner.change_wave_count(4)
        enemies = self.spawner.spawn(20000)
        ref_enemies = self.ref_arrangements.arrangement1()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave6(self):
        self.spawner.change_wave_count(5)
        enemies = self.spawner.spawn(25000)
        ref_enemies = self.ref_arrangements.arrangement2()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave7(self):
        self.spawner.change_wave_count(6)
        enemies = self.spawner.spawn(25000)
        ref_enemies = self.ref_arrangements.arrangement4()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave8(self):
        self.spawner.change_wave_count(7)
        enemies = self.spawner.spawn(25000)
        ref_enemies = self.ref_arrangements.arrangement3()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave9(self):
        self.spawner.change_wave_count(8)
        enemies = self.spawner.spawn(25000)
        ref_enemies = self.ref_arrangements.arrangement5()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave10(self):
        self.spawner.change_wave_count(9)
        enemies = self.spawner.spawn(29000)
        ref_enemies = self.ref_arrangements.arrangement6()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave11(self):
        self.spawner.change_wave_count(10)
        enemies = self.spawner.spawn(35000)
        ref_enemies = self.ref_arrangements.arrangement8()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))

    def test_spawn_wave12(self):
        self.spawner.change_wave_count(11)
        enemies = self.spawner.spawn(35000)
        ref_enemies = self.ref_arrangements.arrangement7()

        enemy_x = [enemy.rect.x for enemy in enemies]
        enemy_y = [enemy.rect.y for enemy in enemies]
        ref_enemy_x = [ref_enemy.rect.x for ref_enemy in ref_enemies]
        ref_enemy_y = [ref_enemy.rect.y for ref_enemy in ref_enemies]

        self.assertEqual((enemy_x, enemy_y), (ref_enemy_x, ref_enemy_y))