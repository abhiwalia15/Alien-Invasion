import sys
#sys module is used to exit the game when the player exits.

import pygame

def check_events():
	#watch for mouse and keyboard events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
