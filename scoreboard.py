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
		self.prep_high_score()
		
	def prep_score(self):
		'''turn the score into a rendered image'''
		rounded_score = int(round(self.stats.score,-1))
		score_str = "{:,}".format(rounded_score)
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
		
		#Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def show_score(self):
		'''Draw score to the screen'''
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		
	def prep_high_score(self):
		'''turn the high score into a rendered image.'''
		high_score = int(round(self.stats.high_score , -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
		
		#center the high score at thte top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
		





