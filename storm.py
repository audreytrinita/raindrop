import pygame
from pygame.sprite import Sprite 

class Storm(Sprite):
	def __init__(self, rain_drop):
		super().__init__()
		self.screen= rain_drop.screen

		self.image= pygame.image.load('C:/Dev/python_game/latihan/img/storm2.png')
		self.rect= self.image.get_rect()

		self.rect.midbottom= rain_drop.cloud.rect.midbottom

		self.x = float(self.rect.x)

	def blitme(self):
		self.screen.blit(self.image, self.rect)