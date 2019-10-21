import sys
import pygame as pg

from settings import Settings
from ship import Ship

class AlienInvasion:
    # create an alien invasion class
    # this will be the main game class
    def __init__(self):
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        # Strat the main loop for the game
        while True:
            # watch for keyboard and mouse events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pg.display.flip()

    
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
