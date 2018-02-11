import sys
#sys module is used to exit the game when the player exits.

import pygame

def check_events():
	#watch for mouse and keyboard events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
def update_screen(ai_settings,screen,ship):
	'''update the images on the screen and flip to the new screen,'''
	
	#redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	
	#draw the ship on the screen using the blit() method , and it is written after creating the background.
	ship.blitme()
	
	#make the most recently drawn screen visible.
	pygame.display.flip()
