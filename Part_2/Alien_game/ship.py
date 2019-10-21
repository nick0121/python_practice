import pygame as pg

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pg.image.load("D:\\programming\\Dev\\python\\practice\\Python_sandbox\\python_practice\\Part_2\\alien_invasion\\img\\ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        self.screen.blit(self.image, self.rect)