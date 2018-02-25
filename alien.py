import pygame 

from pygame.sprite import Sprite

class Alien(Sprite):
	'''a class to represent a single alien in the fleet'''
	
	def __init__(self,ai_settings,screen):
		'''initiliaze the aliens and set its starting positions'''
		super(Alien,self).__init__()
		
		self.screen = screen 
		self.ai_settings = ai_settings 
		
		#load the alien image adn set its rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#start each neew alien near the top
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store aliens exact location
		self.x = float(self.rect.x)
		
	def blitme(self):
		'''draw the alien at its current position'''
		self.screen.blit(self.image,self.rect)