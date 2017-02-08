import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, ship, bullets):
	#responds to keypresses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, ship)
			
def check_keydown_event(event, ai_settings, screen, ship, bullets):
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
			elif event.key == pygame.K_SPACE:
				fire_bullets(ai_settings, screen, ship, bullets)
			elif event.key == pygame.K_q:
				sys.exit()
		
def check_keyup_event(event, ship):
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False
			
def update_screen(ai_settings, screen, ship, aliens, bullets):
	#redraw screen during each pass through loop.
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		aliens.draw(screen)
		
		for bullet in bullets.sprites():
			bullet.draw_bullet()

	#redraw most recent screen
		pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
	bullets.update()
		
	#get rid of bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
	check_collisions(ai_settings, screen, ship, aliens, bullets)
	
def check_collisions(ai_settings, screen, ship, aliens, bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	if collisions:
		ai_settings.score += 1
	
	if len(aliens) == 0:
		bullets.empty()
		ai_settings.fleet_drop_speed += 2
		create_fleet(ai_settings, screen, ship, aliens)
		ai_settings.score += 15
		get_score(ai_settings)
	
	
def fire_bullets(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
		
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	
	aliens.add(alien)

def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - (2 * alien_width)
	number_aliens_x = (available_space_x / (2 * alien_width))
	
	return number_aliens_x
		
def create_fleet(ai_settings, screen, ship, aliens):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	
	number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def update_aliens(ai_settings, screen, ship, aliens, bullets):
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, ship, aliens, bullets)
	
	check_fleet_edges(ai_settings, screen, ship, aliens, bullets)
	aliens.update()

def ship_hit(ai_settings, screen, ship, aliens, bullets):
	lives = ai_settings.lives
	
	if lives > 0:
		ship.ai_settings.lives -= 1
		lives = ai_settings.lives
		
		aliens.empty()
		bullets.empty()
		
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center = ship.screen_rect.centerx
		
		print("Ship Hit you have: " + str(lives) + " lives left")
		get_score(ai_settings)
		sleep(3)
		
	elif lives < 1:
		ai_settings.alien_speed_factor = 0
		ai_settings.fleet_drop_speed = 0
		ai_settings.bullets_allowed = 0
		
		if ai_settings.score >= 50:
			print("Game over! You win!\n Score: " + str(ai_settings.score))
		else:
			print("Game over! You Lose.\n Score: " + str(ai_settings.score))
		
		play_again(ai_settings, screen, ship, aliens, bullets)
		

def play_again(ai_settings, screen, ship, aliens, bullets):
	try:
			play_again = input("Enter 'q' to quit, Enter anything else to play again:\n")
			if play_again == 'q':
				ai_settings.active = False
			else:
				reset(ai_settings)
			
	except Exception:
		reset(ai_settings)

def reset(ai_settings):
	ai_settings.alien_speed_factor = 1
	ai_settings.fleet_drop_speed = 10
	ai_settings.fleet_direction = 1
	ai_settings.lives = 4
	ai_settings.score = 0
	ai_settings.alien_speed_factor = 1

				
def check_fleet_edges(ai_settings, screen, ship, aliens, bullets):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
		if alien.rect.bottom >= screen.get_rect().bottom:
			ship_hit(ai_settings, screen, ship, aliens, bullets)
			break

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
def get_score(ai_settings):
	print("Score after the round: " + str(ai_settings.score))
	


	
	
	
	
	
	
