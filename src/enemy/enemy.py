import random
from cards.base_card import Card
from events import *
from effects.base_effect import EffectEnum
from cards.card_def import *


class Enemy:
    outgoing_modifiers = []
    incoming_modifiers = []

    def __init__(self, card_queue, health, initial_shield=0, initial_effects=()):
        self.health = health
        self.shield = initial_shield
        self.effects = EffectEnum(initial_effects)
        self.card_queue = card_queue

    def get_intent(self):
        return random.choice(['attack', 'defence'])

    def submit_intent(self, player):
        if len(self.card_queue.open) <= 0:
            return

        if self.get_intent() == 'attack':
            card = CARDS[-2].copy()
        else:
            card = CARDS[-1].copy()
        position = random.choice(self.card_queue.open)
        self.card_queue.submit(card, self, player, position)

    def start_combat(self, player):
        self.start_turn(player)

    def start_turn(self, player):
        self.shield = 0
        for i in range(random.randint(1, 3)):
            self.submit_intent(player)

    def end_turn(self, player): pass

    def receive_card_attributes(self, card_attributes):
        modified_attributes = card_attributes
        for transformation in self.incoming_modifiers:
            modified_attributes *= transformation

        unshielded = modified_attributes.damage - self.shield
        if unshielded < 0:
            self.shield = -unshielded
        else:
            self.health -= unshielded
            self.shield = 0

        self.shield += modified_attributes.shield
        self.health += modified_attributes.heal

        self.effects.append_effects(modified_attributes.effects)

    def send_card_attributes(self, card_attributes):
        modified_attributes = card_attributes
        for transformation in self.outgoing_modifiers:
            modified_attributes *= transformation
        return modified_attributes

