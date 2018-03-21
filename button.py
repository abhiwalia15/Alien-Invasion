class Button():
	
	def __init__(self,ai_settings,screen,msg):
		'''initiliaze button attributes'''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#set the dimensions and property of the buttons.
		self.width , self.height = 200,50
		self.button_color =(0,255,0)
		self.test_color = (255,255,255)
		self.font = pygame.font.sysFont(none,48)
		
		#set the buttons rect and onject 
		self.rect = pygame(0,0,self_width,self_height)
		self.rect.center = self.screen_rect.centere
		
		#button message needs to be prep ony once
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
			
		'''turn msg into a rendered image and centrix text on the button'''
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect_center = self.rect.centrix
			
	def draw_button(self):
		#draw blank button and then draw message
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
