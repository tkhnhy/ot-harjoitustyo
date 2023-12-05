import pygame
from sprites.enemies import Enemy1
from sprites.enemybullet import EnemyBullet1
from sprites.playerbullet import PlayerBullet
from enemy_spawns import Enemy_Spawns


class GameLoop:

    def __init__(self, clock, renderer, player):
        self._clock = clock
        self._renderer = renderer
        self._player = player
        
        self.playergroup = pygame.sprite.Group()
        self.playergroup.add(self._player)
        self.all_enemies = pygame.sprite.Group()
        self.all_sprites_group = pygame.sprite.Group()
        self.all_player_bullets_group = pygame.sprite.Group()
        self.all_sprites_group.add(self._player)
        self.enemy_bullets = pygame.sprite.Group()

        self.enemy_spawns = Enemy_Spawns()

        self.score = 0

    def spawn(self, time):
        try:
            for enemy in self.enemy_spawns.spawn(time):
                self.all_sprites_group.add(enemy)
                self.all_enemies.add(enemy)
        except:
            pass
	
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
                    self._player.rect.x + 10, self._player.rect.y + 20)
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

    def loop(self):

        run = True
        fps = 30

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            current_time = self._clock.get_ticks()
            if current_time > 50000:
                run = False
            self.spawn(current_time)

            #Enemy shooting
            for enemy in self.all_enemies:
                if enemy.canshoot(current_time):
                    bullet = EnemyBullet1(
                        enemy.rect.x + 14, enemy.rect.y + 30, 8)
                    self.enemy_bullets.add(bullet)
                    self.all_sprites_group.add(bullet)

            pressed_keys = pygame.key.get_pressed()
            self.playercontrol(pressed_keys, current_time)
            self.all_sprites_group.update()

            #Collisions
            for bullet in self.all_player_bullets_group:
                enemy_hits = pygame.sprite.spritecollide(
                    bullet, self.all_enemies, True)
                for i in enemy_hits:
                    self.all_enemies.remove(i)
                    self.all_sprites_group.remove(i)
                    self.score += 10
                if enemy_hits:
                    self.all_player_bullets_group.remove(bullet)
                    self.all_sprites_group.remove(bullet)
            
            for bullet in self.enemy_bullets:
                player_hit = pygame.sprite.spritecollide(
                    bullet, self.playergroup, True)
                if player_hit:
                    pygame.time.wait(1000)
                    run = False

            for enemy in self.all_enemies:
                enemy_player = pygame.sprite.spritecollide(
                    enemy, self.playergroup, True)
                if enemy_player:
                    pygame.time.wait(1000)
                    run = False

            self._clock.tick(fps)
            self._renderer.render(self.all_sprites_group)