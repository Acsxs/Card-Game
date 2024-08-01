import pygame
import sys
from UI.card_UI_component import CardUIComponent
from consts import *
import numpy as np
from UI.hand_UI_component import HandUIComponent
from UI.button import Button
from UI.mouse_tracker import MouseTrackerGroup, Mouse
from UI.floating_card import FloatingCard
from UI.playing_board import PlayingBoard
from UI.player_UI_controller import PlayerUIController
pygame.init()

# b1 = pygame.Surface((200,100))
# b1.fill((0,0,0))
#
# b2 = pygame.Surface((200,100))
# b2.fill((0,0,255))
#
# button1 = Button(b1, (20,50), lambda:print('je'))
# button2 = Button(b2, (20, 300), lambda:print('ka'))
# button_group = MouseTrackerGroup((SCREEN_WIDTH, SCREEN_HEIGHT), button1, button2)
mouse = Mouse()
player_ui = PlayerUIController(mouse)
card1 = FloatingCard(HAND_CARD_SIZE, pygame.image.load("data/assets/cards/Common Lightning.png"), 1, "Lighting", "Does smthn i guess")
card2 = FloatingCard(HAND_CARD_SIZE, pygame.image.load("data/assets/cards/Common Shield.png"), 1, "Shield", "Does smthn i guess")
for i in range(6):
    player_ui.hand_ui.cards.append(card1.copy())
    player_ui.hand_ui.cards.append(card2.copy())

# floating = FloatingCard((CARD_SIZE[0]*3, CARD_SIZE[1]*3), pygame.image.load("data/assets/cards/Common Lightning.png"), 1, "Lighting", "Does smthn i guess")
# card_group = MouseTrackerGroup((SCREEN_WIDTH, SCREEN_HEIGHT), floating)


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

    # button_group.draw(screen)
    # button_group.update()
    # card_group.draw(screen)
    # card_group.update()

    # mouse = pygame.mouse.get_pos()
    # playing_board.draw(screen)
    # for i in playing_board.get_slot_centres():
    #     pygame.draw.circle(screen, (255, 0, 0), i, 5)
    # # hand.rect.topleft=(0, SCREEN_HEIGHT // 2)
    # hand.draw(screen)
    # card1.draw(screen, (297, 413))
    mouse.update()
    player_ui.draw(screen)

    pygame.display.update()
pygame.quit()
sys.exit()
