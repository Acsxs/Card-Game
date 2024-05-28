import pygame
from UI.UI_component import UIComponent


class CardUI(UIComponent):
    cost = 0
    damage = 0
    shield = 0
    heal = 0
    effects = []

    def __init__(self, base_image, description):
        self.base_image = base_image
        super().__init__(pygame.Surface(base_image.get_rect().size))
        self.description = description

    def update_card(self):
        self.clear()
        self.surface.blit(self.base_image, (0, 0))


