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

    def pick(self, card_index):
        return self.cards.pop(card_index)

    def pick_slice(self, start, stop, step=1):
        if stop > len(self.cards) - 1:
            stop = len(self.cards) - 1
        return [self.pick(0) for index in range(start, stop, step)]

    def to_string(self):
        return str([card.name for card in self.cards])

    def play(self, card_queue, player, card_index, target, position):
        if player.energy - self.cards[card_index].calculate('cost') <= 0:
            return None
        self.cards[card_index].target = target
        player.energy -= self.cards[card_index].calculate('cost')
        card_queue.submit(self.cards[card_index], position)
        return self.pick(card_index)
