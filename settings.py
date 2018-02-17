class Settings():
	
	def __init__(self):
		'''initialize the game settings'''
		#screem resolution
		
		self.screen_width = 1200
		self.screen_height = 600
		
		#background color
		
		self.bg_color = (230,230,230)

		#ship speed settings
		self.ship_speed_factor = 1.5
		
		#settings for bullets,these will create bullets of dark grey color and will travel up untill it disappears.
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		
 
