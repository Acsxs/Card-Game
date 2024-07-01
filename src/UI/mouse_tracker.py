import time
from consts import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame


class MouseTracker:
    def __init__(self, size=None, rect=None, mask=None):
        if size is not None:
            self.rect = pygame.Rect((0, 0), size)
        elif isinstance(rect, pygame.Rect):
            self.rect = rect
        else:
            raise NotImplemented
        self.hover = False
        self.mask = mask or pygame.mask.Mask(self.rect.size)

    def on_click(self):
        pass

    def on_hover(self, mouse_pos):
        if self.rect.collidepoint(*mouse_pos):
            self.hover = True
            return
        self.hover = False

    def on_hold(self):
        pass

class MouseTrackerGroup:
    def __init__(self, screen_size, *args):
        self.trackers = list(args)
        self.size = screen_size
        self.mask = pygame.Mask(screen_size)
        self.hold = False
        self.hold_timer = 0
        self.click_timer = 0
        self.previous_pos = (0, 0)
        self.hold_threshold = 0.15
        for tracker in self.trackers:
            self.mask.draw(tracker.mask, tracker.rect.topleft)

    def add(self, tracker):
        self.trackers.append(tracker)
        self.mask.draw(tracker.mask, tracker.rect.topleft)

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

    def check_hover(self, mouse_pos):
        if 0>mouse_pos[0]>self.size[0] or 0 > mouse_pos[1] > self.size[1]:
            return
        if self.mask.get_at(mouse_pos) == 0:
            return
        for tracker in self.trackers:
            tracker.on_hover(mouse_pos) # make this a var and only call when on 

    def check_hold(self):
        pressed = pygame.mouse.get_pressed()
        if self.hold is True:
            if not pressed[0]:
                self.hold = False
            for tracker in self.trackers:
                tracker.on_hold()
        if pressed[0] and self.hold_timer == 0:
            self.hold_timer = time.perf_counter()
            return
        if pressed[0]:
            if time.perf_counter()-self.hold_timer > 0.15:
                self.hold = True
            return
        self.hold_timer = 0


    def update(self):
        self.check_hold()
        self.check_click()
        self.check_hover(mouse_pos=pygame.mouse.get_pos())

    def draw(self, surface):
        for tracker in self.trackers:
            tracker.draw(surface)
