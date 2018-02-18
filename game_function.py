import sys
#sys module is used to exit the game when the player exits.

import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	'''respond to keypress.'''
	#when a KEYDOWN event is detected we need to check whether the key pressed is one that triggers a certain event.
	if event.key == pygame.K_RIGHT:
	#move the ship towards the right.
		ship.moving_right = True
		
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	
	elif event.key == pygame.K_SPACE:
		#create a new bullet and add it to the bullets group.
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
		
def check_keyup_events(event,ship):
	'''respond to key releases.'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
				
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
	
	#watch for mouse and keyboard events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,ai_settings,screen,ship,bullets)
				
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
						
def update_screen(ai_settings,screen,ship,bullets):
	'''update the images on the screen and flip to the new screen,'''
	
	#redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	
	#redraw all the bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	#draw the ship on the screen using the blit() method , and it is written after creating the background.
	ship.blitme()
	
	#make the most recently drawn screen visible.
	pygame.display.flip()
