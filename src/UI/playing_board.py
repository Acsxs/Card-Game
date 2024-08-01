from consts import *


class PlayingBoard:
    cards = CARD_SLOTS * [None]

    def __init__(self):
        self.card_slot_surface = pygame.transform.scale(pygame.image.load("data/assets/card-slot.png"), CARD_SLOT_SIZE)
        self.playing_board_surface = pygame.Surface((CARD_SLOT_SIZE[0] * CARD_SLOTS + PIXEL_SIZE, CARD_SLOT_SIZE[1]))
        for i in range(CARD_SLOTS + 1):
            self.playing_board_surface.blit(self.card_slot_surface, (CARD_SLOT_SIZE[0] * i, 0))

        # self.playing_board_surface = pygame.transform.scale(pygame.image.load("data/assets/Playing Board.png"), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.rect = self.playing_board_surface.get_rect(center=PLAYING_BOARD_POS)

    def update_board(self):
        self.surface.fill(NO_COLOUR)
        self.surface.blit(self.playing_board_surface, self.rect)
        for index, card in enumerate(self.cards):
            if card is None:
                continue
            card.rect.topleft = self.rect.topleft[0] + CARD_POSITIONS[index][0], self.rect.topleft[1] + CARD_POSITIONS[index][1]
            card.draw(self.surface)

    def get_slot_centres(self):
        return [(CARD_SLOT_CENTRE[0] + i * CARD_SLOT_SIZE[0] + self.rect.left, CARD_SLOT_CENTRE[1] + self.rect.top) for i in range(CARD_SLOTS)]

    def pick_card(self, mouse_pos):
        for card in self.cards:
            if card is None:
                continue
            print(card.rect)
            if card.rect.collidepoint(mouse_pos):
                self.cards.remove(card)
                return card

    def draw(self, surface, pos=None):
        assert pos is None
        self.update_board()
        surface.blit(self.surface, (0, 0))
