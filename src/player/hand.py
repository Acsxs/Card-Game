from events import *


class Hand(EventBroadcaster):
    def __init__(self, event_handler, cards=None):
        EventBroadcaster.__init__(self, event_handler)
        self.cards = cards or []

    def draw(self, card):
        self.cards.append(card)
        self.broadcast_event(Event("PlayerDrawCard"))

    def draw_slice(self, cards):
        for card in cards:
            self.draw(card)

    def discard(self, card_index):
        self.cards.pop(card_index)
        self.broadcast_event(Event("PlayerDiscardCard"))

    def discard_slice(self, card_indices):
        for card in card_indices:
            self.discard(card)

    def play(self, card_queue, energy, card_index, target, position):
        self.cards[card_index].target = target
        card_queue.submit(self.cards[card_index], position)
        self.discard(card_index)
