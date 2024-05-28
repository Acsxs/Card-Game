from pygame.color import Color


class UIComponent:
    surface = None
    rect = None

    def __init__(self, surface):
        self.surface = surface
        self.rect = self.surface.get_rect()

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

    def clear(self):
        self.surface.fill(Color(0, 0, 0, 0))
