import pygame
import sys
import numpy as np
from src.UI.card_UI_component import CardUIComponent

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 680

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Untitled")

card = CardUIComponent((100,100), pygame.image.load("data/assets/cards/Common Lightning.png"), 2, "Lightning", "Deals {damage} damage")
card.update_card()
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    card.draw(screen,(0,0))

    pygame.display.update()

pygame.quit()
sys.exit()
