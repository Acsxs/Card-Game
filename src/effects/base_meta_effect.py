

class MetaEffect:
    def __init__(self, queue_positions, subject, function):
        self.queue_positions = queue_positions
        self.subject = subject
        self.function = function

    def apply_meta_effect(self, queue):
        affected_cards = queue[self.queue_positions]
        for card in affected_cards:
            card.modifiers[self.subject].append(self.function)