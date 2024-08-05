from events import *


class Hand:
    def __init__(self,  cards=None):
        self.cards = cards or []

    def draw(self, card):
        self.cards.append(card)

    def draw_slice(self, cards):
        self.cards.extend(cards)

    def pick(self, card_index):
        return self.cards.pop(card_index)

    def pick_slice(self, start, stop, step=1):
        if stop > len(self.cards) - 1:
            stop = len(self.cards) - 1
        return [self.pick(0) for index in range(start, stop, step)]

    def to_string(self):
        return str([card.name for card in self.cards])
