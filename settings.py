class Settings():
	
	def __init__(self):
		'''initialize the game settings'''
		#screem resolution
		
		self.screen_width = 1200
		self.screen_height = 800
		
		#background color
		
		self.bg_color = (230,230,230)

		#ship speed settings
		self.ship_speed_factor = 2
		self.ship_limit = 3
		
		#settings for bullets,these will create bullets of dark grey color and will travel up untill it disappears.
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		#limit the number of bullets that ship fires at once.
		self.bullets_allowed =  3
		
		#Aliens settings 
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet directionof 1 represent right , -1 represents left
		self.fleet_direction = 1
 
