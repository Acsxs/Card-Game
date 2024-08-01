import pygame


class StaminaIndicator:
    health_value_surf = None
    shield_value_surf = None
    health_final = None
    shield_final = None

    def __init__(self, master, bottom_left, stamina):
        self.surface = pygame.Surface((350,200))
        self.rect = self.surface.get_rect()
        self.master = master
        self.stamina = stamina
        self.rect = self.surface.get_rect(bottomleft=bottom_left)
        self.health_rect, self.shield_rect = self.health_base.get_rect(), self.shield_base.get_rect()
        self.font = pygame.font.SysFont('Minecraft', 80)
        self.update_surf(stamina)

    def update_surf(self, stamina=None):
        self.stamina = stamina if stamina is not None else self.stamina
        self.clear()
        self.health_final = self.health_base.copy()
        self.shield_final = self.shield_base.copy()
        self.health_value_surf = self.font.render(str(self.stamina[0]), True, (255, 255, 255))
        self.health_final.blit(self.health_value_surf, self.health_value_surf.get_rect(center=self.health_rect.center))
        self.shield_value_surf = self.font.render(str(self.stamina[1]), True, (255, 255, 255))
        self.shield_final.blit(self.shield_value_surf, self.shield_value_surf.get_rect(center=self.shield_rect.center))
        self.surface.blit(self.health_final, (0, 0))
        self.surface.blit(self.shield_final, (175, 0))

    def clear(self):
        self.surface.fill(pygame.Color(0, 0, 0, 0))

    def draw(self, surface, pos=None):
        self.update_surf()
        surface.blit(self.surface, pos if pos is not None else self.rect)

    def update_pos(self, bottom_left):
        self.rect.bottomleft = bottom_left
