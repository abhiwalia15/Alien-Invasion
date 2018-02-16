import pygame

form pygame.sprite import Sprite
#when you use sprites , you can group related elements in your game and act on all the grouped elements at once.

class Bullet(Sprite):
	'''a class to manage the bullets fired from the ships'''
	
	def __init__(self,ai_settings,screen,ship):
		'''create a bullet object at the ships current position.'''
		Super(Bullet,self).__init__()
		self.screen  = screen
		
		#create a bullet rect at (0,0) and then set correct positions
		self.rect = pygame.Rect(0,0,ai_settings.bullet_height,ai_settings.bullet_width)
		
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#store the bullets positions in a decimal value.
		
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
		def update(self):
			'''move the bullets up the screen'''
			#update the decimal position of the bullet.
			self.y -= self.speed_factor
			#update the rect position
			self.rect.y = self.y
			
		def draw_bullets9self):
			'''Draw the bullets to the screen'''
			pygame.draw.rect(self.screen,self.color,self.rect)
