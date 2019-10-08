import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption('BlueSky')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((230, 230, 230))
    image = pygame.image.load("D:\\programming\\Dev\\python\\practice\\Python_sandbox\\python_practice\\Part_2\\alien_invasion\\rocket.png")
    rect = image.get_rect()

    # rect.midbottom = screen.midbottom

    screen.blit(image, rect)

    pygame.display.flip()

