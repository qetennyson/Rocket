
import pygame

import game_functions as gf
from settings import Settings
from rocket import Rocket


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Rocket Launcher")

    # Make a rocket.
    rocket = Rocket(ai_settings, screen)

    while True:

        # Redraw the screen during each pass through the loop
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)


run_game()
