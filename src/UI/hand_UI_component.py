from consts import *
import numpy as np


class HandUIComponent:
    def __init__(self):
        self.surface = pygame.Surface((SCREEN_WIDTH * 3/5, CARD_SIZE[1] + CARD_PADDING), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.cards = []
        self.card_rects = []
        self.highlight_surface = pygame.Surface((SCREEN_HEIGHT*10/52, SCREEN_HEIGHT/4), pygame.SRCALPHA)

    def update_hand(self):
        self.surface.fill(NO_COLOUR)
        self.card_rects = []
        card_offset = np.array(((self.rect.size[0]-CARD_SIZE[0]) / len(self.cards), 0))
        card_offset = card_offset if card_offset[0] < CARD_SIZE[0] else np.array((CARD_SIZE[0]+1, 0))
        for index, card in enumerate(self.cards):
            self.card_rects.append(pygame.Rect(card_offset*index+self.rect.topleft, CARD_SIZE))
            card.draw(self.surface, card_offset * index)

    def draw(self, surface, pos=None):
        self.update_hand()
        surface.blit(self.surface, pos if pos is not None else self.rect)
        surface.blit(self.highlight_surface, self.highlight_surface.get_rect(center=surface.get_rect().center))

    def card_hover(self, mouse_pos):
        if not self.rect.collidepoint(mouse_pos):
            return
        for index, card_rects in reversed(list(enumerate(self.card_rects))):
            card_hover = card_rects.collidepoint(mouse_pos)
            if card_hover:
                self.highlight_surface = self.cards[index].get_surface_at_scale((SCREEN_HEIGHT*10/28, SCREEN_HEIGHT/2))
                return index
        self.highlight_surface = pygame.Surface((SCREEN_HEIGHT*10/28, SCREEN_HEIGHT/2), pygame.SRCALPHA)
        return False