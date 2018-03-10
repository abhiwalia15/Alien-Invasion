class GameStats():
	'''this class is for tracking statistics for the alien invasion'''
	
	def __init__(self, ai_settings):
		'''Initiliaze statistics'''
		self.ai_settings = ai_settings
		self.reset_stats()
		
		#START ALIEN INVASION IN AN ACTIVE STATE
		self.game_active = True
			
	def reset_stats(self):
		'''initiliaze statistics that can change during game'''
		self.ships_left = self.ai_settings.ship_limit
