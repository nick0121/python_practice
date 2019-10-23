import pygame as pg 
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #load the alien and set its rect attribute
        self.image = pg.image.load('D:\\programming\\Dev\\python\\practice\\Python_sandbox\\python_practice\\Part_2\\alien_invasion\\img\\alien.bmp')
        self.rect = self.image.get_rect()

        #start a new alien near the top of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact horizontal positoion
        self.x = float(self.rect.x)