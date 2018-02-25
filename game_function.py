import sys
#sys module is used to exit the game when the player exits.

import pygame

from alien import Alien 

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
		fire_bullet(ai_settings,screen,ship,bullets)
		
	#to quit the game.
	elif event.key == pygame.K_q:
		sys.exit()
		
def fire_bullet(ai_settings,screen,ship,bullets):
	'''fire a bullet if limit has not reached yet.'''
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
						
def update_screen(ai_settings,screen,ship,aliens,bullets):
	'''update the images on the screen and flip to the new screen,'''
	
	#redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	
	#redraw all the bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	#draw the ship on the screen using the blit() method , and it is written after creating the background.
	ship.blitme()
	
	#when you call draw() methon on a group , pygame automatically 
	#draws each elements in the group at that position defined
	#by its rect attribute
	aliens.draw(screen)
	
	#make the most recently drawn screen visible.
	pygame.display.flip()
	
def update_bullet(bullets):
	'''update positions of bullets and get rid of old bullets.'''
	#update bullets position.
	bullets.update()
	
	#get rid of the bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
def get_number_aliens_x(ai_settings,alien_width):
	'''determine the number of aliens that fit in a row'''
	#spacing between each alien is equal to one alien width.
	
	available_space_x = ai_settings.screen_width - (2*alien_width)
	number_aliens_x = int(available_space_x / (2*alien_width))
	return number_aliens_x
	
def get_number_rows(ai_settings,ship_height,alien_height):
	'''determine the number of rows of aliens that can fit on the screen'''
	available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(available_space_y / (2*alien_height) )
	return number_rows
	
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	'''create an alien and place it in a row'''
	#create an alien and place it in the row.
	
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2* alien.rect.height*row_number
	aliens.add(alien)
			
def create_fleet(ai_settings,screen,ship,aliens):
	'''create a full fleet of aliens.'''
	
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	
	#create the fleet of aliens.
	for row_number in range (number_rows):
		
		#create the first row of aliens.
		for alien_number in range(number_aliens_x):
			
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
		
		
