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
        return [self.pick(index) for index in range(start, stop, step)]

