from cards.base_card import Card

class CardQueue:
    def __init__(self, queue_length):
        self.queue = [None for i in range(queue_length)]
        self.open = [i for i in range(queue_length)]
        self.queue_length = queue_length

    def submit(self, card, position):
        if 0 >= position >= self.queue_length-1:
            raise IndexError
        if not (self.queue[position] is None):
            raise NotImplemented
        self.open.remove(position)
        self.queue[position] = card

    def play(self):
        for index, card in enumerate(self.queue):
            if card is None:
                continue
            card.apply_card_effects()
            self.queue[index] = None

    def to_string(self):
        return str([card.name if isinstance(card, Card) else card for card in self.queue])