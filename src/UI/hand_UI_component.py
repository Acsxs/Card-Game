import pygame.draw

from consts import *
import numpy as np


class HandUIComponent:
    def __init__(self):
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.cards = []
        self.rect = pygame.Rect(HAND_UI_POS, HAND_UI_AREA)

    def update_hand(self):
        self.surface.fill(NO_COLOUR)
        if len(self.cards) == 0:
            return
        card_offset = np.array(((self.rect.size[0] - HAND_CARD_SIZE[0]) / len(self.cards), 0))
        card_offset = card_offset if card_offset[0] < HAND_CARD_SIZE[0] else np.array((HAND_CARD_SIZE[0] + 1, 0))
        for index, card in enumerate(self.cards):
            card.rect.topleft = card_offset * index + self.rect.topleft
            card.draw(self.surface)

    def pick_card(self, mouse_pos):
        for index, card in enumerate(reversed(self.cards)):
            print(card.rect)
            if card.rect.collidepoint(*mouse_pos):
                self.cards.remove(card)
                return index, card
        return None, None

    def draw(self, surface, pos=None):
        assert pos is None
        self.update_hand()
        surface.blit(self.surface, (0, 0))
