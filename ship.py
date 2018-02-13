import pygame

class Ship():

	def __init__(self,ai_settings,screen):
		'''initialize the ship adn get its starting positions.'''
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load the ship image and get its rectangle.
		self.image = pygame.image.load('images/ship.bmp')
		
		#get_rect() is used to get the rectangle attribute of the image and screen
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect() 
		
		#to start each new ship at the bottom centre of the screen
		#Make the value of self.rect.bottom (the y-coordinate of the ship’s bottom) equal to the value of the screen rect’s bottom attribute)
		self.rect.center = self.screen_rect.center
		self.rect.bottom = self.screen_rect.bottom
		
		#store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)
		
		#Movement flag ,set the flag to false.
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		'''update the ships movement based on the movement flag.'''
		if self.moving_right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left:
			self.center -= self.ai_settings.ship_speed_factor
			
		# Update rect object from self.center.
		self.rect.centerx = self.center
		
	#to get the image on screen use blit()method
	def blitme(self):
		'''draw the sip at its current location'''
		self.screen.blit(self.image,self.rect)
