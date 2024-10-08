from input.mouse_tracker import MouseTrackerGroup
from UI.playing_board import PlayingBoard
from UI.hand_UI_component import HandUIComponent
from consts import *


class PlayerUIController(MouseTrackerGroup):
    selected_card = None

    def __init__(self, mouse, interface):
        super().__init__(mouse)
        self.interface = interface
        self.playing_board = PlayingBoard()
        self.hand_ui = HandUIComponent()

    def on_mouse_down(self):
        if 0 > self.mouse.pos[0] > SCREEN_WIDTH or 0 > self.mouse.pos[1] > SCREEN_HEIGHT:
            return
        if self.hand_ui.rect.collidepoint(self.mouse.pos):
            self.interface.register_hand_pick(self.hand_ui.get_index(self.mouse.pos))
        elif self.playing_board.rect.collidepoint(self.mouse.pos):
            self.interface.register_hand_pick(self.playing_board.get_index(self.mouse.pos))
        if self.selected_card is None:
            return
        self.selected_card.change_size((CARD_SIZE[0] * 1.5, CARD_SIZE[1] * 1.5))
        self.selected_card.offset = (self.selected_card.rect.topleft[0] - self.mouse.pos[0], self.selected_card.rect.topleft[1] - self.mouse.pos[1])

    def on_mouse_up(self):
        if self.selected_card is None:
            return
        if self.playing_board.rect.collidepoint(self.mouse.pos):
            centres = self.playing_board.get_slot_centres()
            distances = [(x - self.mouse.pos[0], y - self.mouse.pos[1]) for x, y in centres]
            distances = [x * x + y * y for x, y in distances]
            index = distances.index(min(distances))
            if self.playing_board.cards[index] is None:
                self.interface.register_board_set(index)
                self.playing_board.cards[index] = self.selected_card
                self.selected_card.change_size(CARD_SIZE)
            else:
                self.interface.register_hand_set()
                self.selected_card.change_size(HAND_CARD_SIZE)
                self.hand_ui.cards.append(self.selected_card)
        else:
            self.interface.register_hand_set()
            self.selected_card.change_size(HAND_CARD_SIZE)
            self.hand_ui.cards.append(self.selected_card)
        self.selected_card = None

    def on_hold(self):
        if self.selected_card is None:
            return
        self.selected_card.on_hold()

    def draw(self, surface):
        self.update()
        self.playing_board.draw(surface)
        self.hand_ui.draw(surface)
        if self.selected_card:
            self.selected_card.draw(surface)
