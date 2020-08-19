import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
	def __init__(self,rain_drop):
		super().__init__()
		self.screen= rain_drop.screen
		self.drop_setting= rain_drop.rd_setting

		self.image= pygame.image.load('C:/Dev/python_game/latihan/img/drop2.png')
		self.rect= self.image.get_rect()
		self.rect.topleft = rain_drop.cloud.rect.topleft

		#penempatan drop
		self.rect.x = rain_drop.cloud.widthmid
		self.rect.y= rain_drop.cloud.rect.height

		self.y = float(self.rect.y)
		self.x = float(self.rect.x)

	def update(self):
		self.y += self.drop_setting.drop_speed
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)