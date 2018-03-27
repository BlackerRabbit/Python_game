import sys
import pygame
from class_setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from allion import Alion
from game_stats import Game_state as gs
from button import Button
from score_board import Scoreboard

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

	stats = gs(ai_setting)

	play_btn = Button(ai_setting, screen, 'Play')

	sb = Scoreboard(ai_setting, screen, stats)

# def update_bullet(bullets, allions, ai_setting, screen, ship):
	while 1:
		# def check_events(ai_setting, screen, ship, bullets, stats, play_button, allions):
		gf.check_events(ai_setting, screen, ship, bullets, stats, play_btn, allions)
		if stats.game_active:
			ship.update()
			bullets.update()
			gf.update_aliens(ai_setting, allions, ship, screen, stats, bullets)
			gf.update_bullet(bullets, allions, ai_setting, screen, ship, stats, sb)
		else :
			print('game is done')
		gf.update_screen(ai_setting, screen, ship, bullets, allions, stats, play_btn, sb)
run_game()
