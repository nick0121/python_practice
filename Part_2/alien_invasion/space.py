import pygame as pg

from pygame.sprite import Sprite

class Space(Sprite):



    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.image = pg.image.load("D:\\programming\\Dev\\python\\practice\\Python_sandbox\\python_practice\\Part_2\\alien_invasion\\img\\alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)