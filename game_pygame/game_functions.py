import sys
import pygame
from bullet import Bullet
from allion import Alion
		# gf.check_events(ai_setting, screen, ship, bullets)
		# ship.update()
		# bullets.update()
		# gf.update_screen(ai_setting, screen, ship, bullets)

def check_events(ai_setting, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.reset_moving()
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.reset_moving()
				ship.moving_left = True
			elif event.key == pygame.K_UP:
				ship.reset_moving()
				ship.moving_up = True
			elif event.key == pygame.K_DOWN:
				ship.reset_moving()
				ship.moving_down = True
			elif event.key == pygame.K_SPACE:
				new_bullet = Bullet(ai_setting, screen, ship)
				if len(bullets) <= ai_setting.bullet_allowed:
					bullets.add(new_bullet)
			elif event.key == pygame.K_q:
				quit()
		elif event.type == pygame.KEYUP:
			ship.reset_moving()


def get_allion_nmbers(ai_setting, allion_widt):
	avaliable_space_x = ai_setting.screen_width - 2 * allion_widt
	number_allion_x = int(avaliable_space_x / (2 * allion_widt))
	return number_allion_x

def get_allion_rows(ai_setting, allion_height, ship_height):
	avaliable_space_y = ai_setting.screen_height - 3 * allion_height - ship_height
	number_allion_y = int(avaliable_space_y / ( 2 * allion_height))
	return number_allion_y

def create_fleet(ai_setting, screen, allions, ship):
	allion = Alion(ai_setting, screen)
	number_allion_x = get_allion_nmbers(ai_setting, allion.rect.width)
	number_allion_row = get_allion_rows(ai_setting, allion.rect.height, ship.ship_height)
	for row_number in range(number_allion_row):
		for alien_number in range(number_allion_x):
			create_allion(ai_setting, screen, allions, alien_number, row_number)
		

def create_allion(ai_setting, screen, allions, allion_number, row_number):	
	allion = Alion(ai_setting, screen)
	allion_width = allion.rect.width
	allion.x = allion_width + 2 * allion_width * allion_number
	allion.rect.x = allion.x
	allion.rect.y = allion.rect.height + 2 * allion.rect.height * row_number
	allions.add(allion)


def update_screen(ai_setting, screen, ship, bullets, allions):	
	screen.fill(ai_setting.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
	ship.blitem()
	for allion in allions:
		allion.blitem()
	pygame.display.flip()
		
def update_bullet(bullets):
	for bullet in bullets:
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def update_aliens(ai_setting, allions):	
	check_fleet_edges(ai_setting, allions)
	allions.update()

def change_fleet_direction(ai_setting, allions):
	for alien in allions.sprites():
		alien.rect.y += ai_setting.fleet_drop_speed
	ai_setting.fleet_direction *= -1

def check_fleet_edges(ai_setting, allions):	
	for allion in allions.sprites():
		if allion.check_edges():
			change_fleet_direction(ai_setting, allions)
			break

		



























