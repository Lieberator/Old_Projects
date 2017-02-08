import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
	
	def __init__(self, ai_settings, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen
		
		#parameters for rect are (top, left, width, height)
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#store bullets position as a decimal value
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		
		#update decimal postion of the bullet.
		self.y -= self.speed_factor
		#update the rect postion
		self.rect.y = self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
