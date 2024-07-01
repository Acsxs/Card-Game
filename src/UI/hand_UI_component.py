from consts import *
import numpy as np
from UI.mouse_tracker import MouseTrackerGroup
import time

class HandUIComponent(MouseTrackerGroup):
    def __init__(self):
        self.surface = pygame.Surface((SCREEN_WIDTH * 3 / 5, CARD_SIZE[1] + CARD_PADDING), pygame.SRCALPHA)
        super().__init__((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.surface.get_rect()
        self.cards = []
        self.card_rects = []
        self.selected_card = None

    def update_hand(self):
        self.surface.fill(NO_COLOUR)
        self.card_rects = []
        card_offset = np.array(((self.rect.size[0] - CARD_SIZE[0]) / len(self.cards), 0))
        card_offset = card_offset if card_offset[0] < CARD_SIZE[0] else np.array((CARD_SIZE[0] + 1, 0))
        for index, card in enumerate(self.cards):
            if card == self.selected_card:
                continue
            self.card_rects.append(pygame.Rect(card_offset * index + self.rect.topleft, CARD_SIZE))
            card.rect.topleft = card_offset * index
            card.draw(self.surface)

    def check_click(self):
        pressed = pygame.mouse.get_pressed()
        if not (pressed[0] and not self.hold):
            self.click_timer = 0
            return
        if self.click_timer == 0:
            self.click_timer = time.perf_counter()
        if 1e-6 < time.perf_counter() - self.click_timer < 0.15:
            return
        for tracker in self.trackers:
            tracker.on_click()
        mouse_pos = pygame.mouse.get_pos()
        for card in list(reversed(self.cards)):
            if card.rect.collidepoint(mouse_pos):
                card.change_size((CARD_SIZE[0]*2, CARD_SIZE[1]*2))
                self.selected_card = card
                break

    def draw(self, surface, pos=None):
        self.update_hand()
        surface.blit(self.surface, pos if pos is not None else self.rect)

