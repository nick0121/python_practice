import sys
import pygame

class AlienInvasion:

    def __init__(self):

       pygame.init()
       window_width = 1200
       window_height = 800

       self.screen = pygame.display.set_mode((window_width, window_height))

       pygame.display.set_caption("Alien Invasion") 

       self.bg_color = (230, 230, 230)

    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.bg_color = (120, 120, 120)
                    elif event.key == pygame.K_LEFT:
                        self.bg_color = (20, 30, 200)
            
            self.screen.fill(self.bg_color)

            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
