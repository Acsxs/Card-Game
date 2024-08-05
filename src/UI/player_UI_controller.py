from input.mouse_tracker import MouseTrackerGroup
from UI.playing_board import PlayingBoard
from UI.hand_UI_component import HandUIComponent
from consts import *


class PlayerUIController(MouseTrackerGroup):
    selected_card = None

    def __init__(self, mouse):
        super().__init__(mouse)
        self.playing_board = PlayingBoard()
        self.hand_ui = HandUIComponent()

    def on_mouse_down(self):
        if 0 > self.mouse.pos[0] > SCREEN_WIDTH or 0 > self.mouse.pos[1] > SCREEN_HEIGHT:
            return
        if self.hand_ui.rect.collidepoint(self.mouse.pos):
            self.selected_card = self.hand_ui.pick_card(self.mouse.pos)
        elif self.playing_board.rect.collidepoint(self.mouse.pos):
            self.selected_card = self.playing_board.pick_card(self.mouse.pos)
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
            distances = [x*x + y*y for x,y in distances]
            index = distances.index(min(distances))
            if self.playing_board.cards[index] is None:
                self.playing_board.cards[index] = self.selected_card
                self.selected_card.change_size(CARD_SIZE)
            else:
                self.hand_ui.cards.append(self.selected_card)
                self.selected_card.change_size(HAND_CARD_SIZE)
        else:
            self.hand_ui.cards.append(self.selected_card)
            self.selected_card.change_size(HAND_CARD_SIZE)
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
