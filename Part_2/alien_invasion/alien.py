import sys
import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet
from space import Space

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
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()

        self._create_fleet()


    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.update_bullets()

            # update screen last
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
            elif event.key == pg.K_SPACE:
                self.fire_bullet()
            elif event.key == pg.K_q:
                sys.exit()


    def _check_keyup_events(self, event):
            if event.key == pg.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pg.K_LEFT:
                self.ship.moving_left = False

    
    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien = Space(self)
        alien_width = alien.rect.width

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        for alien_number in range(number_aliens_x):
            print(alien_number)
            alien = Space(self)
            alien_x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)


    def _update_screen(self):
        # Update images on screen and flip to a new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        pg.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


    