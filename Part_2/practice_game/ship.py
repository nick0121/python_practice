import pygame as pg


class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Home workstation
        self.image = pg.image.load('D:\\programming\\Dev\\python\\practice\\Python_sandbox\\python_practice\\ship.bmp')

        # Work workstation
        # self.image = pg.image.load('C:\\Users\\nhartford\\Dev\\practice\\python\\python_book_sandbox\\python_practice\\ship.bmp')
        
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        # if self.moving_right:
        #     self.x += self.setting.ship_speed
        # if self.moving_left:
        #     self.x -= self.setting.ship_speed
        # if self.moving_up:
        #     self.y += self.setting.ship_speed
        # if self.moving_down:
        #     self.y -= self.setting.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y


    def blit_me(self):
        self.screen.blit(self.image, self.rect)