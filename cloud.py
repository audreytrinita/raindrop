import pygame
from pygame.sprite import Sprite

class Cloud(Sprite):
	def __init__(self,rain_drop):
		super().__init__()
		self.screen= rain_drop.screen
		self.screen_rect= rain_drop.screen.get_rect()

		self.image= pygame.image.load('C:/Dev/python_game/latihan/img/cloud2.png')
		self.rect= self.image.get_rect()

		self.rect.topleft = self.screen_rect.topleft

		self.widthmid = self.rect.width / 2

		self.x = float(self.rect.x)

	#def blitme(self):
	#	self.screen.blit(self.image, self.rect)