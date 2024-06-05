from src.UI.UI_component import UIComponent
import pygame


class CardUIComponent(UIComponent):
    def __init__(self, size, card, cost, name, description):
        UIComponent.__init__(self, size)
        # card.blit()

        self.surface = pygame.transform.scale(card, size)


