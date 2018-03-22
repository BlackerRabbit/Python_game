import pygame
import sys

class Ship():
	"""docstring for Ship"""
	def __init__(self, screen, ai_settings):
		self.screen = screen
		self.rect = screen.get_rect()
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.ai_settings = ai_settings
		self.ship_height = self.rect.height


	def blitem(self):
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.left > 0 :
			self.rect.centerx -= self.ai_settings.ship_speed_factor
		elif self.moving_up and self.rect.top > 0 :
			self.rect.centery -= self.ai_settings.ship_speed_factor
		elif self.moving_down and self.rect.bottom < self.screen_rect.height:
			self.rect.centery += self.ai_settings.ship_speed_factor

	def reset_moving(self):
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		pass
	
	def center_ship(self):
		self.rect.bottom = self.screen_rect.bottom
		self.rect.centerx = self.screen_rect.centerx