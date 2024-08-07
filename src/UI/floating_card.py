import pygame.mask

from UI.card_UI_component import CardUIComponent
from collections.abc import Iterable
from input.mouse_tracker import MouseTracker


class FloatingCard(CardUIComponent, MouseTracker):
    def __init__(self, size, card, cost, name, description):
        CardUIComponent.__init__(self, size, card, cost, name, description)
        MouseTracker.__init__(self, rect=self.rect, mask=pygame.mask.from_surface(self.surface))
        self.offset = (0, 0)

    def on_hold(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.topleft = mouse_pos[0] + self.offset[0], mouse_pos[1] + self.offset[1]

    def draw(self, surface, pos=None):
        assert pos is None
        surface.blit(self.surface, self.rect)

    def change_size(self, new_size):
        self.size = new_size
        self.surface = pygame.Surface(new_size)
        self.update_card()
        self.rect = self.surface.get_rect(center=self.rect.center)

    def copy(self):
        return FloatingCard(self.size, self.card, self.cost, self.name, self.description)
