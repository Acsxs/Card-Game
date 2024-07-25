from consts import *
import numpy as np
from UI.mouse_tracker import MouseTrackerGroup
import time


class HandUIComponent(MouseTrackerGroup):
    def __init__(self, mouse):
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        super().__init__((SCREEN_WIDTH, SCREEN_HEIGHT), mouse)
        area = (SCREEN_WIDTH * 3 / 5, CARD_SIZE[1] + CARD_PADDING)
        self.rect = pygame.Rect(SCREEN_WIDTH - area[0] / 2, 4 * SCREEN_HEIGHT / 5, area[0], area[1])
        self.selected_card = None

    def update_hand(self):
        self.surface.fill(NO_COLOUR)
        card_offset = np.array(((self.rect.size[0] - CARD_SIZE[0]) / len(self.trackers), 0))
        card_offset = card_offset if card_offset[0] < CARD_SIZE[0] else np.array((CARD_SIZE[0] + 1, 0))
        for index, card in enumerate(self.trackers):
            if card == self.selected_card:
                continue
            card.rect.topleft = card_offset * index + self.rect.topleft
            card.draw(self.surface)

    def on_mouse_down(self):
        self.selected_card = self.hover
        if self.selected_card is None:
            return
        self.selected_card.change_size((CARD_SIZE[0] * 1.5, CARD_SIZE[1] * 1.5))
        self.selected_card.rect.topleft = self.selected_card.rect.topleft[0] + self.rect.topleft[0], self.selected_card.rect.topleft[1] + self.rect.topleft[1]

    def on_mouse_up(self):
        self.selected_card.change_size((CARD_SIZE[0], CARD_SIZE[1]))
        self.selected_card = None

    def on_hold(self):
        if self.selected_card is None:
            return

    def check_hover(self, mouse_pos):
        if self.hover is not None:
            if 0 > mouse_pos[0] > self.size[0] or 0 > mouse_pos[1] > self.size[1] or self.mask.get_at(mouse_pos) == 0:
                self.hover = None
                return
        for tracker in reversed(self.trackers):
            if tracker.rect.collidepoint(*mouse_pos):
                self.hover = tracker
                break
        if self.hover is None:
            print('aaa')
            return
        self.hover.on_hold()

    def draw(self, surface, pos=None):
        assert pos is None
        self.update_hand()
        self.update()
        surface.blit(self.surface, (0, 0))
        if self.selected_card is not None:
            self.selected_card.draw(surface)
            # surface.blit(self.cards[self.selected_card_index], self.cards[self.selected_card_index].rect)
