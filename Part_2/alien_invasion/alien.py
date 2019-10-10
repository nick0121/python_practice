import sys
import pygame as pg

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pg.init()
        

        self.settings = Settings()

        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        # self.screen = pg.display.set_mode((
        #     self.settings.screen_width, self.settings.screen_height))

        pg.display.set_caption('Alien Invasion')

        self.ship = Ship(self)


    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            

    def _check_events(self):
        # responds to key presses and mouse events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
            if event.key == pg.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pg.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pg.K_q:
                sys.exit()


    def _check_keyup_events(self, event):
            if event.key == pg.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pg.K_LEFT:
                self.ship.moving_left = False


    def _update_screen(self):
        # Update images on screen and flip to a new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pg.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


     