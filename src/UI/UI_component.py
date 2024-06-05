from pygame.color import Color
import pygame


class UIComponent:
    surface = None
    rect = None

    def __init__(self, size):
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

    def clear(self):
        self.surface.fill(Color(0, 0, 0, 0))
