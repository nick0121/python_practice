import sys
import pygame as pg

from setting import Settings
from ship import Ship

class Rocket:

    def __init__(self):

        pg.init()

        self.settings = Settings()

        self.screen = pg.display.set_mode((1200, 800))
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pg.display.set_caption('Rocket')

        self.ship = Ship(self)
        

    def run_game(self):
        while True:
            self.check_events()
            
               
            self.screen.fill((230, 230, 230))
            self.ship.update()
            self.ship.blit_me()
            pg.display.flip()
            


    def check_events(self):
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pg.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pg.K_UP:
                    self.ship.moving_up = True
                elif event.key == pg.K_DOWN:
                    self.ship.moving_down = True

            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pg.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pg.K_UP:
                    self.ship.moving_up = False
                elif event.key == pg.K_DOWN:
                    self.ship.moving_down = False

if __name__ == '__main__':
    ai = Rocket()
    ai.run_game()
