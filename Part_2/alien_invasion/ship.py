import pygame as pg
from pygame import image

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Get the ships image and get its rect
        self.image = pg.image.load("D:\\programming\\Dev\\python\\practice\\Python_sandbox\\python_practice\\Part_2\\alien_invasion\\img\\ship.bmp")
        self.rect = self.image.get_rect()
        
        # Start each ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        # Draw the ship
        self.screen.blit(self.image, self.rect)
        