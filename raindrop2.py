import sys
import pygame
from raindrop_setting import Settings
from cloud import Cloud
from drop import Drop
from storm import Storm

class raindrop:
	def __init__(self):
		pygame.init()

		self.rd_setting= Settings()
		self.screen= pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.rd_setting.screen_width= self.screen.get_rect().width
		self.rd_setting.screen_height= self.screen.get_rect().height
		#self.screen = pygame.display.set_mode((1200,650))
		self.screen_rect = self.screen.get_rect()

		pygame.display.set_caption('RainDrop')


		self.bg_color= self.rd_setting.bg_color
		self.cloud = Cloud(self)
		self.storm = Storm(self)
		self.clouds= pygame.sprite.Group()
		self.drops = pygame.sprite.Group()
		self.storms= pygame.sprite.Group()
		self.cloud_fleet()

	def run(self):
		while True:
			self.check_event()
			self.drops.update() #kasih tau arah drop nya kemana

			for drop in self.drops.copy():
				if drop.rect.top >= self.screen_rect.bottom:
					self.drops.remove(drop)
			print(len(self.drops))

			self.update_screen()

	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self.respond_keydown(event)
			elif event.type == pygame.KEYUP:
				self.respond_keyup(event)

	def respond_keydown(self,event):
		if event.key == pygame.K_s:
			self.storm_fleet()
		elif event.key == pygame.K_SPACE:
			self.drop_fleet()
		elif event.key == pygame.K_q:
			sys.exit()

	def respond_keyup(self,event):
		if event.key == pygame.K_s:
			for storm in self.storms.copy():
				self.storms.remove(storm)

	def cloud_fleet(self):
		cloud= Cloud(self)
		cloud_width = cloud.rect.width
		number_cloud= self.rd_setting.screen_width // (1 * cloud_width)

		for cloud_number in range(number_cloud):
			self.create_cloud(cloud_number)

	def drop_fleet(self):
		cloud= Cloud(self)
		drop= Drop(self)
		drop_width, drop_height = drop.rect.size

		number_drop_x = 34

		for drop_number_x in range(number_drop_x):
			self.create_drop(drop_number_x)

	def storm_fleet(self):
		storm= Storm(self)
		storm_width = storm.rect.width
		number_storm = self.rd_setting.screen_width // (1* storm_width)
		
		for storm_number in range(number_storm):
			self.create_storm(storm_number)
	
	def create_cloud(self,cloud_number):
		cloud = Cloud(self)
		cloud_width = cloud.rect.width
		cloud.x = 1 * cloud_width * cloud_number
		cloud.rect.x = cloud.x
		self.clouds.add(cloud)

	def create_storm(self, storm_number):
		storm = Storm(self)
		storm_width, storm_height = storm.rect.size
		cloud= Cloud(self)

		storm.x = 1 * storm_width * storm_number
		storm.rect.y = 1 * storm_height
		storm.rect.x = storm.x
		self.storms.add(storm)

	def create_drop(self,drop_number_x):
		drop= Drop(self)
		drop_width, drop_height = drop.rect.size

		from random import randint
		random_number= randint(-30,30)

		drop.x =random_number +  2 * drop_width * drop_number_x
		drop.rect.x = drop.x
		self.drops.add(drop)

	def update_drop(self):
		for drop in self.drops.copy():
			if drop.rect.top > self.screen_rect.bottom:
				self.drops.remove(drop)
		print(len(self.drops))


	def update_screen(self):
		self.screen.fill(self.bg_color)
		self.clouds.draw(self.screen) #self.screen-nya si cloud.py
		for drop in self.drops.sprites():
			drop.blitme()
		self.storms.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	rd= raindrop()
	rd.run()