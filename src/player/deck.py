import random
from events import *


class Deck(EventBroadcaster):
    def __init__(self, event_handler, cards):
        EventBroadcaster.__init__(self, event_handler)
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def pick(self, index):
        return self.cards.pop(index)

    def pick_slice(self, start, stop, step=1):
        if stop > len(self.cards)-1:
            stop = len(self.cards)-1
        return [self.pick(0) for index in range(start, stop, step)]

    def shuffle_discard(self, discard):
        self.cards = discard.cards.copy()
        discard.clear()
        self.shuffle()


