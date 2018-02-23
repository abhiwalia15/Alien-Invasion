
import pygame
from pygame.sprite import Group

from settings import Settings

from ship import Ship

from alien import Alien

import game_function as gf

def run_game():
	
	#initialize game and create a screen object.
	
	pygame.init()
	#now to create a display called screen on which the game will run.
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion-By MW")
	
	#make a ship
	ship = Ship(ai_settings,screen)
	
	#make an alien
	alien = Alien(ai_settings,screen)
	
	#make an empty group to store the bullets in.
	bullets = Group()
	
	#start the main loop for the program.
	while True:
		
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullet(bullets)
		gf.update_screen(ai_settings, screen, ship, alien, bullets)
		
run_game()
