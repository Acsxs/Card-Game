from UI.card_UI_component import CardUIComponent
from collections.abc import Iterable


class FloatingCard(CardUIComponent):
    def __init__(self, size, card, cost, name, description):
        super().__init__(size, card, cost, name, description)
        self.hover = False
        self.offset = (0, 0)

    def drag_pos(self, mouse_pos):
        self.rect.topleft = mouse_pos[0] + self.offset[0], mouse_pos[1] + self.offset[1]

    def draw(self, surface, pos=None):
        assert pos is None




