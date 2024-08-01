from cards.base_card import Card


class CardMessenger:
    def __init__(self, author, card, recipient):
        self.author = author
        self.card = card
        self.recipient = recipient

class CardQueue:
    def __init__(self, queue_length):
        self.queue = [None for i in range(queue_length)]
        self.open = [i for i in range(queue_length)]
        self.queue_length = queue_length

    def submit(self, card, author, recipient, position):
        if 0 >= position >= self.queue_length - 1:
            raise IndexError
        if not (self.queue[position] is None):
            raise NotImplemented
        self.open.remove(position)
        self.queue[position] = CardMessenger(author, card, recipient)

    def play(self):
        for index, card_messenger in enumerate(self.queue):
            if card_messenger is None:
                continue
            card_messenger.recipient.receive_card_attributes(card_messenger.author.send_card_attributes(card_messenger.card.get_attributes()))
            self.queue[index] = None
        self.open = [i for i in range(self.queue_length)]

    def to_string(self):
        return str([card.name if isinstance(card, Card) else card for card in self.queue])
