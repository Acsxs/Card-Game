import pygame
import sys
from src.UI.card_UI_component import CardUIComponent

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

image = pygame.image.load("data/assets/cards/Common Lightning.png")

card = CardUIComponent((342, 479), image, 2, "Lightning", "Deal 2 Damage, Temporarily stuns the enemy, disabling it "
                                                          "from using attacking moves for the turn.")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    card.draw(screen, (300,50))
    pygame.display.update()
pygame.quit()
sys.exit()
