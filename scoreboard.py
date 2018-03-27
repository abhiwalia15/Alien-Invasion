import pygame.font

class Scoreboard():
	'''a class to report scoring information'''
	
	def __init__(self,ai_settings,screen,stats):
		'''initiliaze scorekeeping attributes'''
		
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		#font settings for scoring information.
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		
		#prepare the initial scoring image.
		self.prep_score()
		
