import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Get the ships image and get its rect
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draw the ship
        self.screen.blit(self.image, self.rect)
        