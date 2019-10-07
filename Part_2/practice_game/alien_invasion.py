import sys
import pygame

class AlienInvasion:

    def __init__(self):

       pygame.init()
       window_width = 1200
       window_height = 800

       self.screen = pygame.display.set_mode(window_width, window_height)

       pygame.display.set_caption("Alien Invasion") 

    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type() == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(230,230,230)

            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
