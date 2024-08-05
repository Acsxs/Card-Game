

class Discard:
    cards = []

    def discard(self, card):
        self.cards.append(card)

    def discard_slice(self, cards):
        self.cards.extend(cards)

    def clear(self):
        self.cards = []

    def get_pile(self):
        return self.cards
