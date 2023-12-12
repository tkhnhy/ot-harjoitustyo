import pygame
from sprites.enemybullet import EnemyBullet1
from sprites.playerbullet import PlayerBullet
from enemy_spawns import EnemySpawns


class GameLoop:
    """Class that contains the main gameplay loop.
    """

    def __init__(self, clock, renderer, player, event_q):
        self._clock = clock
        self._renderer = renderer
        self._player = player
        self._event = event_q
        
        self.playergroup = pygame.sprite.Group()
        self.playergroup.add(self._player)
        self.all_enemies = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()
        self.all_player_bullets_group = pygame.sprite.Group()
        self.all_sprites_group.add(self._player)
        self.enemy_bullets = pygame.sprite.Group()

        self.enemy_spawns = EnemySpawns()

        self.score = 0

        self.run = True

    def spawn(self, time):
        """Adds the enemies from spawner to sprite groups
        
        Args:
            time: the time that it sends to spawner to retrieve a list of enemies to add
        """
        try:
            for enemy in self.enemy_spawns.spawn(time):
                    self.all_sprites_group.add(enemy)
                    self.all_enemies.add(enemy)
        except:
            pass

    def playercontrol(self, pressed_keys, time):
        """Responsible for controlling the player based on which key is pressed.
        
        Args:
            pressed_keys: The current key that is pressed
            time: Time that has passed since program start
        """

        if pressed_keys[pygame.K_w]:
            self._player.moveplayer(0, -self._player.speed)
        if pressed_keys[pygame.K_s]:
            self._player.moveplayer(0, self._player.speed)
        if pressed_keys[pygame.K_a]:
            self._player.moveplayer(-self._player.speed, 0)
        if pressed_keys[pygame.K_d]:
            self._player.moveplayer(self._player.speed, 0)
        if pressed_keys[pygame.K_SPACE]:
            if self._player.canshoot(time):
                bullet = PlayerBullet(
                    self._player.rect.x + 10, self._player.rect.y + 20)
                self.all_player_bullets_group.add(bullet)
                self.all_sprites_group.add(bullet)
            else:
                pass
        
        self._player.rect.left = max(0, min(self._player.rect.left, 512))
        self._player.rect.right = min(512, max(self._player.rect.right, 0))
        self._player.rect.top = max(0, min(self._player.rect.top, 856))
        self._player.rect.bottom = min(856, max(self._player.rect.bottom, 0))

    def enemy_shooting(self, time):
        for enemy in self.all_enemies:
                if enemy.canshoot(time):
                    if enemy.name == "AlienShip":
                        bullet = EnemyBullet1(
                            enemy.rect.x + 14, enemy.rect.y + 30, 8)
                        self.enemy_bullets.add(bullet)
                        self.all_sprites_group.add(bullet)
                    if enemy.name == "BossAlien":
                        bullets = [
                            EnemyBullet1(enemy.rect.x + 14, enemy.rect.y + 30, 8),
                            ]
                        for bullet in bullets:
                            self.enemy_bullets.add(bullet)
                            self.all_sprites_group.add(bullet)

    def check_pbullet_enemy_coll(self):
        """Checks collision between playerbullets and enemies, and removes them if collide.
        """
        for bullet in self.all_player_bullets_group:
                enemy_hits = pygame.sprite.spritecollide(
                    bullet, self.all_enemies, True)
                for enemy in enemy_hits:
                    if enemy.name == "AlienShip":
                        self.all_enemies.remove(enemy)
                        self.all_sprites_group.remove(enemy)
                        self.score += 10
                    if enemy.name == "BossAlien":
                        enemy.reduce_health()
                        if enemy.health <= 0:
                            self.all_enemies.remove(enemy)
                            self.all_sprites_group.remove(enemy)
                            self.score += 100
                            self.run = False
                        
                if enemy_hits:
                    self.all_player_bullets_group.remove(bullet)
                    self.all_sprites_group.remove(bullet)

    def check_ebullet_player_coll(self):
        """Checks collision between enemy bullets and player and ends game if collide.
        """
        for bullet in self.enemy_bullets:
                player_hit = pygame.sprite.spritecollide(
                    bullet, self.playergroup, True)
                if player_hit:
                    pygame.time.wait(1000)
                    self.run = False

    def check_enemy_player_coll(self):
        """Checks collision between enemies and player and ends game if collide.
        """
        for enemy in self.all_enemies:
                enemy_player = pygame.sprite.spritecollide(
                    enemy, self.playergroup, True)
                if enemy_player:
                    pygame.time.wait(1000)
                    self.run = False

    def loop(self):

        fps = 30

        while self.run:
            for event in self._event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            current_time = self._clock.get_ticks()
            if current_time > 50000:
                self.run = False
            
            self.spawn(current_time)

            # Enemy shooting
            self.enemy_shooting(current_time)

            pressed_keys = pygame.key.get_pressed()
            self.playercontrol(pressed_keys, current_time)
            self.all_sprites_group.update()

            # Collisions
            self.check_pbullet_enemy_coll()
            self.check_ebullet_player_coll()
            self.check_enemy_player_coll()

            self._clock.tick(fps)
            self._renderer.render(self.all_sprites_group)
