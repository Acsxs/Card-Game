from consts import *


class PlayingBoard:
    def __init__(self):
        self.card_slot_surface = pygame.transform.scale(pygame.image.load("data/assets/card-slot.png"), CARD_SLOT_SIZE)
        self.playing_board_surface = pygame.Surface((CARD_SLOT_SIZE[0]*CARD_SLOTS+10, CARD_SLOT_SIZE[1]))
        for i in range(CARD_SLOTS+1):
            self.playing_board_surface.blit(self.card_slot_surface, (CARD_SLOT_SIZE[0]*i, 0))

        # self.playing_board_surface = pygame.transform.scale(pygame.image.load("data/assets/Playing Board.png"), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))
        self.surface = self.playing_board_surface.copy()
        self.rect = self.surface.get_rect()
        self.cards = [] # CardUIComponent

    def update_surf(self):
        self.surface = self.playing_board_surface.copy()
        for index, card in enumerate(self.cards):
            card.draw(self.surface, CARD_POSITIONS[index])

    def draw(self, surface, pos=None):
        self.update_surf()
        surface.blit(self.surface, pos if pos is not None else self.rect)