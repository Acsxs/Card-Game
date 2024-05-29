from events import *


class Hand(EventBroadcaster):

    def __init__(self, event_handler, cards=None):
        EventBroadcaster.__init__(self, event_handler)
        self.cards = cards or []

    def draw(self, card):
        self.cards.append(card)
        self.broadcast(Event("PlayerDrawCard"))

    def draw_slice(self, cards):
        for card in cards:
            self.draw(card)

    def discard(self, card_index):
        self.cards.pop(card_index)
        self.broadcast(Event("PlayerDiscardCard"))

    def discard_slice(self, card_indices):
        for card in card_indices:
            self.discard(card)

    def to_string(self):
        return str([card.name for card in self.cards])

    def play(self, card_queue, player, card_index, target, position):
        if player.energy - self.cards[card_index].calculate('cost') <=0:
            return
        self.cards[card_index].target = target
        player.energy -= self.cards[card_index].calculate('cost')
        card_queue.submit(self.cards[card_index], position)
        self.discard(card_index)
