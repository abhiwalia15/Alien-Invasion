import sys
#sys module is used to exit the game when the player exits.

import pygame

def check_events(ship):
	#watch for mouse and keyboard events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	
			elif event.type == pygame.KEYDOWN:
				#when a KEYDOWN event is detected we need to check whether the key pressed is one that triggers a certain event.
				if event.key == pygame.K_RIGHT:
					#move the ship towards the right.
					ship.moving_right = True
					
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = False
						
def update_screen(ai_settings,screen,ship):
	'''update the images on the screen and flip to the new screen,'''
	
	#redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	
	#draw the ship on the screen using the blit() method , and it is written after creating the background.
	ship.blitme()
	
	#make the most recently drawn screen visible.
	pygame.display.flip()
