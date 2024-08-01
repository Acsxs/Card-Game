import time
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, HOLD_WINDOW
import pygame


class Mouse:
    button_states = [0, 0, 0]
    """
    keydown: 1
    keyup: 2
    hold: 3
    none: 0
    """
    pos = []
    hold_window = HOLD_WINDOW
    button_hold_timers = [None, None, None]

    def update(self):
        self.pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        current_time = time.perf_counter()
        for index, button_state in enumerate(mouse_buttons):
            current_button = self.button_states[index]
            if current_button == 3 and button_state is True:
                continue
            if self.button_hold_timers[index] is not None:
                if 1e-6 < current_time-self.button_hold_timers[index] < 0.15 and button_state is True:
                    self.button_states[index] = 0
                    continue
                elif button_state is False:
                    self.button_states[index] = 2
                    self.button_hold_timers[index]=None
                    continue
                if current_button == 0 and button_state is True and current_time - self.button_hold_timers[index] >= 0.15:
                    self.button_states[index] = 3
                    continue
            if (current_button == 2 or current_button == 0) and button_state is True:
                self.button_states[index] = 1
                self.button_hold_timers[index] = time.perf_counter()
                continue
            if (current_button == 1 or current_button == 3) and button_state is False:
                self.button_states[index] = 2
                self.button_hold_timers[index] = None
                continue
            if current_button == 1 or current_button == 2:
                self.button_states[index] = 0
                continue






class MouseTracker:
    def __init__(self, size=None, rect=None, mask=None):
        if size is not None:
            self.rect = pygame.Rect((0, 0), size)
        elif isinstance(rect, pygame.Rect):
            self.rect = rect
        else:
            raise NotImplemented
        self.mask = mask or pygame.mask.Mask(self.rect.size)

    def on_mouse_down(self):
        pass

    def on_hover(self, mouse_pos):
        pass

    def on_mouse_up(self):
        pass

    def on_hold(self):
        pass


class MouseTrackerGroup:
    def __init__(self, mouse, *args):
        self.trackers = list(args)
        self.size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.mask = pygame.Mask(self.size)
        self.mouse = mouse
        self.hover = None
        for tracker in self.trackers:
            self.mask.draw(tracker.mask, tracker.rect.topleft)

    def add(self, tracker):
        self.trackers.append(tracker)
        self.mask.draw(tracker.mask, tracker.rect.topleft)


    def remove(self, tracker):
        self.trackers.remove(tracker)
        self.redraw_mask()

    def redraw_mask(self):
        self.mask.clear()
        for tracker in self.trackers:
            self.mask.draw(tracker.mask, tracker.rect.topleft)

    def on_mouse_down(self):
        if self.hover is not None:
            self.hover.on_mouse_down()

    def on_mouse_up(self):
        if self.hover is not None:
            self.hover.on_mouse_up()

    def check_hover(self, mouse_pos):
        if 0 > mouse_pos[0] > self.size[0] or 0 > mouse_pos[1] > self.size[1] or self.mask.get_at(mouse_pos) == 0:
            self.hover = None
            return
        for tracker in self.trackers:
            if tracker.rect.collidepoint(*mouse_pos):
                self.hover = tracker
                tracker.on_hover(mouse_pos)
                break

    def on_hold(self):
        for tracker in self.trackers:
            tracker.on_hold()

    def update(self):
        self.check_hover(mouse_pos=self.mouse.pos)
        if self.mouse.button_states[0] == 2:
            self.on_mouse_up()
        if self.mouse.button_states[0] == 1:
            self.on_mouse_down()
        if self.mouse.button_states[0] == 3:
            self.on_hold()

    def draw(self, surface):
        for tracker in self.trackers:
            tracker.draw(surface)
