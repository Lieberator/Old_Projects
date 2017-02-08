import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	#initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
		
	pygame.display.set_caption("Alien Invasion")
	
	#make ship
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#set background color
	bg_color = (230, 230, 230)
	
	#Start the main loop for the game.
	while True:
		
		gf.check_events(ai_settings, screen, ship, bullets)
		
		if ai_settings.active:
			ship.update()
			gf.update_aliens(ai_settings, screen, ship, aliens, bullets)
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		else:
			break
				
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
			
		

run_game()
