import pygame
from playerbullet import PlayerBullet

class GameLoop:

	def __init__(self, clock, renderer, player):
		self._clock = clock
		self._renderer = renderer
		self._player = player
		self.all_sprites_group = pygame.sprite.Group()
		self.all_player_bullets_group = pygame.sprite.Group()
		self.all_sprites_group.add(self._player)

	def playercontrol(self, pressed_keys):
		
		if pressed_keys[pygame.K_w]:
			self._player.moveplayer(0, -self._player.speed)
		if pressed_keys[pygame.K_s]:
			self._player.moveplayer(0, self._player.speed)
		if pressed_keys[pygame.K_a]:
			self._player.moveplayer(-self._player.speed, 0)
		if pressed_keys[pygame.K_d]:
			self._player.moveplayer(self._player.speed, 0)
		if pressed_keys[pygame.K_SPACE]:
			bullet = PlayerBullet(self._player.rect.x + 16, self._player.rect.y + 8)
			self.all_player_bullets_group.add(bullet)
			self.all_sprites_group.add(bullet)

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
			
			pressed_keys = pygame.key.get_pressed()
				
			self.playercontrol(pressed_keys)
			self.all_sprites_group.update()
			self._clock.tick(fps)
			self._renderer.render(self.all_sprites_group)
			
			