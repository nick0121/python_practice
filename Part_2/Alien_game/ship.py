import pygame as pg

from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        self.image = pg.image.load("D:\\programming\\Dev\\python\\practice\\Python_sandbox\\python_practice\\ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False


    def update(self):

        # update ships x value not the rect

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        # update rect object from x
        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)