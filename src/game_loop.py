import pygame
from enemies import Enemy1
from enemybullet import EnemyBullet1
from playerbullet import PlayerBullet


class GameLoop:

    def __init__(self, clock, renderer, player):
        self._clock = clock
        self._renderer = renderer
        self._player = player

        self.playergroup = pygame.sprite.Group()
        self.playergroup.add(self._player)
        self.all_sprites_group = pygame.sprite.Group()
        self.all_player_bullets_group = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()
        self.all_sprites_group.add(self._player)
        self.enemy_bullets = pygame.sprite.Group()

        self.test_enemy = Enemy1(200, -500, 1)
        self.all_enemies.add(self.test_enemy)
        self.all_sprites_group.add(self.test_enemy)

        self.test_enemy2 = Enemy1(300, 0, 2)
        self.all_enemies.add(self.test_enemy2)
        self.all_sprites_group.add(self.test_enemy2)

    def playercontrol(self, pressed_keys, time):

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
                    self._player.rect.x + 16, self._player.rect.y + 8)
                self.all_player_bullets_group.add(bullet)
                self.all_sprites_group.add(bullet)
            else:
                pass
        if self._player.rect.left < 0:
            self._player.rect.left = 0
        if self._player.rect.right > 512:
            self._player.rect.right = 512
        if self._player.rect.top <= 0:
            self._player.rect.top = 0
        if self._player.rect.bottom >= 856:
            self._player.rect.bottom = 856

    def Loop(self):

        run = True
        fps = 30

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            current_time = self._clock.get_ticks()

            for enemy in self.all_enemies:
                if enemy.canshoot(current_time):
                    bullet = EnemyBullet1(
                        enemy.rect.x + 30, enemy.rect.y + 30, 10)
                    self.enemy_bullets.add(bullet)
                    self.all_sprites_group.add(bullet)

            pressed_keys = pygame.key.get_pressed()
            self.playercontrol(pressed_keys, current_time)
            self.all_sprites_group.update()

            for bullet in self.all_player_bullets_group:
                enemy_hits = pygame.sprite.spritecollide(
                    bullet, self.all_enemies, True)
                for i in enemy_hits:
                    self.all_enemies.remove(i)
                    self.all_sprites_group.remove(i)

            for bullet in self.enemy_bullets:
                player_hit = pygame.sprite.spritecollide(
                    bullet, self.playergroup, True)
                if player_hit:
                    pygame.time.wait(2000)
                    run = False

            self._clock.tick(fps)
            self._renderer.render(self.all_sprites_group)
