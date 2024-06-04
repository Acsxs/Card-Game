import pygame
import sys

button_color = (100,100,100)


pygame.init()

def func(a,b):
    print(a+b)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
#text.fill((255,0,0))


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
sys.exit()
