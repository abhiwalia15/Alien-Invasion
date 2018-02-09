import sys
#sys module is used to exit the game when the player exits.

import pygame

def run_game():
	
	#initialize game and create a screen object.
	
	pygame.init()
	#now to create a display called screen on which the game will run.
	screen = pygame.display.set_mode((1366,728))
	pygame.display.set_caption("Alien Invasion")
	
	#give background a color.
	bg_color = (230,230,230)
	
	#start the main loop for the program.
	while True:
		
		#watch for mouse and keyboard events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		#redraw the screen during each pass through the loop
		screen.fill(bg_color)
		
		#make the most recently drawn screen visible
		pygame.display.flip()

run_game()
