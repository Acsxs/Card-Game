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
        self.mask = mask or pygame.mask.Mask(self.rect.size)

    def on_click(self):
        pass

    def on_hover(self, mouse_pos):
        pass

    def on_mouse_up(self):
        pass

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
        self.hover = None
        for tracker in self.trackers:
            self.mask.draw(tracker.mask, tracker.rect.topleft)

    def add(self, tracker):
        self.trackers.append(tracker)
        self.mask.draw(tracker.mask, tracker.rect.topleft)

    def redraw_mask(self):
        self.mask.clear()
        for tracker in self.trackers:
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
        if self.hover is not None:
            self.hover.on_click()

    def on_mouse_up(self):
        if self.hover is not None:
            self.hover.on_mouse_up()

    def check_hover(self, mouse_pos):
        if 0 > mouse_pos[0] > self.size[0] or 0 > mouse_pos[1] > self.size[1]:
            self.hover = None
            return
        if self.mask.get_at(mouse_pos) == 0:
            self.hover = None
            return
        for tracker in self.trackers:
            if tracker.rect.collidepoint(*mouse_pos):
                self.hover = tracker
                tracker.on_hover(mouse_pos)
                break

    def check_hold(self):
        pressed = pygame.mouse.get_pressed()
        if self.hold is True:
            if not pressed[0]:
                self.on_mouse_up()
                self.hold = False
            if self.hover is not None:
                self.hover.on_hold()
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
