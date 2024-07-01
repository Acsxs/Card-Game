import pygame
import sys
from UI.card_UI_component import CardUIComponent
from consts import *
import numpy as np
from UI.hand_UI_component import HandUIComponent




pygame.init()
hand = HandUIComponent()
card1 = CardUIComponent(CARD_SIZE, pygame.image.load("data/assets/cards/Common Lightning.png"), 1, "Lighting", "Does smthn i guess")
card2 = CardUIComponent(CARD_SIZE, pygame.image.load("data/assets/cards/Common Shield.png"), 1, "Shelid", "Does smthn i guess")
hand.cards.append(card1)
hand.cards.append(card2)
hand.cards.append(card1)
hand.cards.append(card2)
hand.cards.append(card1)
hand.cards.append(card2)
hand.cards.append(card1)
hand.cards.append(card2)
hand.cards.append(card1)
hand.cards.append(card2)
hand.cards.append(card1)
hand.cards.append(card2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

# indicator = StaminaIndicator(None, (100, 300), (20, 10))
# indicator.update_surf((50, 50))
# rect = pygame.Rect(40, 297, 300, 120)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    # indicator.draw(screen)
    mouse = pygame.mouse.get_pos()
    hand.card_hover(mouse)
    hand.rect.topleft=(0, SCREEN_HEIGHT // 2)
    hand.draw(screen)
    # card1.draw(screen, (297, 413))

    pygame.display.update()
pygame.quit()
sys.exit()
