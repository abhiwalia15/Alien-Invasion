import sys
#sys module is used to exit the game when the player exits.

import pygame

from settings import Settings

from ship import Ship

def run_game():
	
	#initialize game and create a screen object.
	
	pygame.init()
	#now to create a display called screen on which the game will run.
	
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#make a ship
	ship = Ship(screen)
	
	#start the main loop for the program.
	while True:
		
		#watch for mouse and keyboard events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		#redraw the screen during each pass through the loop
		screen.fill(ai_settings.bg_color)
		
		#draw the ship on the screen using the blit() method , and it is written after creating the background.
		ship.blitme()
		
		#make the most recently drawn screen visible
		pygame.display.flip()

run_game()
