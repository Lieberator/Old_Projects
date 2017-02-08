import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load ship image and get its rect.
		self.image = pygame.image.load('Images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Store decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
		self.moving_right = False
		self.moving_left = False
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.ai_settings.ship_speed_factor
			
