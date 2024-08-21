from copy import copy
from events import *
from player.hand import Hand
from player.deck import Deck
from effects.base_effect import EffectEnum
from player.discard import Discard


class PlayerCombatHandler:
    draw_amount = 5
    energy = 5
    outgoing_modifiers = []
    incoming_modifiers = []

    def __init__(self, card_queue, interface, player, starting_shield=0, initial_effects=()):
        self.card_queue = card_queue
        self.interface = interface
        self.player = player
        self.shield = starting_shield
        self.deck = Deck(copy(player.inventory.cards))
        self.hand = Hand()
        self.discard = Discard()
        self.effects = EffectEnum(initial_effects)

    def start_combat(self):
        self.deck.shuffle()
        self.energy = 5
        self.interface.register_hand_draw_slice(0, self.draw_amount - 1)

    def start_turn(self):
        self.shield = 0
        self.energy = 5
        self.interface.register_hand_draw_slice(0, self.draw_amount - 1)

    def draw(self):
        if len(self.deck.cards) <= 0:
            self.deck.shuffle_discard(self.discard)
        card = self.deck.pick(0)
        self.hand.draw(self.deck.pick(0))
        return card

    def draw_slice(self, start, stop, step=1):
        if len(self.deck.cards) <= 0:
            self.deck.shuffle_discard(self.discard)
        cards = self.deck.pick_slice(start, stop, step)
        self.hand.draw_slice(cards)
        return cards

    def end_turn(self):
        self.discard.discard_slice(self.hand.pick_slice(0, 1e6))

    def pick_hand(self, index):
        return self.hand.pick(index)

    def return_card(self, card):
        self.energy += card.get_attributes().energy
        self.hand.cards.append(card)

    def play_card(self, card, target, position):
        cost = self.send_card_attributes(card.get_attributes()).cost
        if self.energy - cost <= 0:
            return
        self.energy -= cost
        self.card_queue.submit(card, self, target, position)
        self.discard.discard(card)

    def receive_card_attributes(self, card_attributes):
        modified_attributes = card_attributes
        for transformation in self.incoming_modifiers:
            modified_attributes *= transformation

        unshielded = modified_attributes.damage - self.shield
        if unshielded < 0:
            self.shield = -unshielded
        else:
            self.player.health -= unshielded
            self.shield = 0

        self.shield += modified_attributes.shield
        self.player.health += modified_attributes.heal

        self.effects.append_effects(modified_attributes.effects)

    def send_card_attributes(self, card_attributes):
        modified_attributes = card_attributes
        for transformation in self.outgoing_modifiers:
            modified_attributes *= transformation
        return modified_attributes
