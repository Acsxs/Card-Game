import pygame
import sys
from UI.card_UI_component import CardUIComponent
from UI.UI_component import UIComponent
from consts import *
import numpy as np

class PlayingBoard(UIComponent):
    def __init__(self):
        super().__init__()
        self.card_slot_surface = pygame.transform.scale(pygame.image.load("data/assets/card-slot.png"), CARD_SLOT_SIZE)
        self.playing_board_surface = pygame.Surface((CARD_SLOT_SIZE[0]*CARD_SLOTS+10, CARD_SLOT_SIZE[1]))
        for i in range(CARD_SLOTS+1):
            self.playing_board_surface.blit(self.card_slot_surface, (CARD_SLOT_SIZE[0]*i, 0))

        # self.playing_board_surface = pygame.transform.scale(pygame.image.load("data/assets/Playing Board.png"), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))
        self.surface = self.playing_board_surface.copy()
        self.rect = self.surface.get_rect()
        self.cards = [] # CardUIComponent

    def update_surf(self):
        self.surface = self.playing_board_surface.copy()
        for index, card in enumerate(self.cards):
            card.draw(self.surface, CARD_POSITIONS[index])

    def draw(self, surface, pos=None):
        self.update_surf()
        surface.blit(self.surface, pos if pos is not None else self.rect)


pygame.init()
playing_board = PlayingBoard()
card1 = CardUIComponent(CARD_SIZE, pygame.image.load("data/assets/cards/Common Lightning.png"), 1, "Lighting", "Does smthn i guess")
playing_board.cards.append(card1)
font = pygame.font.SysFont('Minecraft', 80)

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
    playing_board.draw(screen, (0, SCREEN_HEIGHT // 2))
    # card1.draw(screen, (297, 413))

    pygame.display.update()
pygame.quit()
sys.exit()
