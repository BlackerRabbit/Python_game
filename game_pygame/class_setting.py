import sys
import pygame

class Setting():
	def __init__(self):
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		# 设置子弹
		self.bullet_speed_factor = 4
		self.bullet_width = 3
		self.bullet_height = 6
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 4

		# 设置外星人
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1 
		self.alien_points = 50
		self.score_scale = 1.5
		
		# 设置船
		self.ship_speed_factor = 3.5
		self.ship_limit = 3
		self.ship_left = self.ship_limit

		#游戏整体设置
		self.speedup_scale = 1.5
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)


