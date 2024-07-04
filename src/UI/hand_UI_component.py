from consts import *
import numpy as np
from UI.mouse_tracker import MouseTrackerGroup
import time


class HandUIComponent(MouseTrackerGroup):
    def __init__(self):
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        super().__init__((SCREEN_WIDTH, SCREEN_HEIGHT))
        area = (SCREEN_WIDTH * 3 / 5, CARD_SIZE[1] + CARD_PADDING)
        self.rect = pygame.Rect(SCREEN_WIDTH - area[0] / 2, 4 * SCREEN_HEIGHT / 5, area[0], area[1])
        self.cards = self.trackers

    def update_hand(self):
        self.surface.fill(NO_COLOUR)
        card_offset = np.array(((self.rect.size[0] - CARD_SIZE[0]) / len(self.cards), 0))
        card_offset = card_offset if card_offset[0] < CARD_SIZE[0] else np.array((CARD_SIZE[0] + 1, 0))
        for index, card in enumerate(self.cards):
            if self.hover == card and self.hold:
                continue
            card.rect.topleft = card_offset * index + self.rect.topleft
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
        if self.hover is not None:
            self.hover.on_click()
        mouse_pos = pygame.mouse.get_pos()
        for card in reversed(self.trackers):
            if card.rect.collidepoint(mouse_pos):
                card.change_size((CARD_SIZE[0] * 1.5, CARD_SIZE[1] * 1.5))
                card.rect.topleft = card.rect.topleft[0] + self.rect.topleft[0], card.rect.topleft[1] + self.rect.topleft[1]
                break

    def check_hold(self):
        pressed = pygame.mouse.get_pressed()
        if self.hold is True:
            if not pressed[0]:
                self.on_mouse_up()
                self.hold = False
            # print(self.hover)
            if self.hover is not None:
                self.hover.on_hold()
                self.redraw_mask()
        if pressed[0] and self.hold_timer == 0:
            self.hold_timer = time.perf_counter()
            return
        if pressed[0]:
            if time.perf_counter() - self.hold_timer > 0.15:
                self.hold = True
            return
        self.hold_timer = 0

    def check_hover(self, mouse_pos):
        if self.hover is not None:
            if 0 > mouse_pos[0] > self.size[0] or 0 > mouse_pos[1] > self.size[1]:
                self.hover.change_size(CARD_SIZE)
                self.hover = None
                return
            print(self.mask.get_at(mouse_pos))
            if self.mask.get_at(mouse_pos) == 0:
                self.hover.change_size(CARD_SIZE)
                self.hover = None
                return
        for tracker in reversed(self.trackers):
            if tracker.rect.collidepoint(*mouse_pos):
                self.hover = tracker
                tracker.on_hover(mouse_pos)
                break

    def draw(self, surface, pos=None):
        assert pos is None
        self.update_hand()
        surface.blit(self.surface, (0,0))
        if self.hover is not None and self.hold:
            self.hover.draw(surface)
            # surface.blit(self.cards[self.selected_card_index], self.cards[self.selected_card_index].rect)
