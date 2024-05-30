from events import EventBroadcaster


class Discard(EventBroadcaster):
    cards = []

    def __init__(self, event_handler):
        EventBroadcaster.__init__(self, event_handler)

    def discard(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def get_pile(self):
        return self.cards