import sys
import pygame
from class_setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from allion import Alion

def run_game():
	pygame.init()
	ai_setting = Setting()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption('alien invasion')

	bg_color = ai_setting.bg_color

	ship = Ship(screen,ai_setting)
	bullets = Group()

	allion = Alion(ai_setting, screen)
	allions = Group()
	gf.create_fleet(ai_setting, screen, allions, ship)

	while 1:
		gf.check_events(ai_setting, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_aliens(ai_setting, allions)
		gf.update_bullet(bullets)
		gf.update_screen(ai_setting, screen, ship, bullets, allions)

run_game()
