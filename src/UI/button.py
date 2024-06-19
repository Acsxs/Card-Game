import pygame


class Button:
    def __init__(self, surface, pos, command=lambda: None):
        self.surface = surface
        self.rect = self.surface.get_rect(topleft=pos)
        self.command = command
        self.mask = pygame.mask.from_surface(self.surface)

    def on_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return self.command()
        return

    def render(self, surface):
        surface.blit(self.surface,self.rect)


class ButtonGroup:
    def __init__(self, screen_size, *args):
        self.buttons = list(args)
        self.mask = pygame.Mask(screen_size)
        for button in self.buttons:
            self.mask.draw(button.mask, button.rect.topleft)

    def add(self, button):
        self.buttons.append(button)
        self.mask.draw(button.mask, button.rect.topleft)

    def on_click(self, mouse_pos):
        if self.mask.get_at(mouse_pos) == 0:
            return
        for button in self.buttons:
            button.on_click(mouse_pos)

    def render(self, surface):
        for button in self.buttons:
            button.render(surface)