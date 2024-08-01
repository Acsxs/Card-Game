from events import EventBroadcaster


class Discard:
    cards = []

    def discard(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def get_pile(self):
        return self.cards
