import random
from cards.base_card import Card
from events import *
from effects.base_effect import EffectEnum


class Enemy:
    outgoing_modifiers = []
    incoming_modifiers = []

    def __init__(self, card_queue, health, damage_range, shielding_range, initial_shield=0, initial_effects=()):
        self.health = health
        self.shield = initial_shield
        self.effects = EffectEnum(initial_effects)
        self.damage_range = damage_range
        self.shielding_range = shielding_range
        self.card_queue = card_queue
        self.modifiers = {'attack': [a], 'defence': []}

    def get_intent(self):
        return random.choice(['attack', 'defence'])

    def submit_intent(self, player):
        if len(self.card_queue.open) <= 0:
            return
        if self.get_intent() == 'attack':
            card = Card("Enemy Attack", 0, 0, 0, random.randint(self.damage_range[0], self.damage_range[1]))
            self.card_queue.submit(card, self, player, random.choice(self.card_queue.open))
        else:
            card = Card("Enemy Defence", 0, random.randint(self.shielding_range[0], self.shielding_range[1]), 0, 0)
            self.card_queue.submit(card, self, player, random.choice(self.card_queue.open))

    def start_combat(self, player):
        for i in range(random.randint(0, 3)):
            self.submit_intent(player)

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

