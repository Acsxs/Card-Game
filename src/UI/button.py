import pygame
from input.mouse_tracker import MouseTracker


class Button(MouseTracker):
    def __init__(self, surface, pos, command=lambda: None):
        self.surface = surface
        self.rect = self.surface.get_rect(topleft=pos)
        self.command = command
        self.mask = pygame.mask.from_surface(self.surface)
        super().__init__(rect=self.rect, mask=self.mask)

    def on_mouse_down(self):
        return self.command()

    def draw(self, surface):
        surface.blit(self.surface,self.rect)

