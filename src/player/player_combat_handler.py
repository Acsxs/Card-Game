from copy import copy
from events import *
from player.hand import Hand
from player.deck import Deck
from effects.base_effect import EffectEnum
from player.discard import Discard


class PlayerCombatHandler:
    starting_draw = 7
    selected_card = None
    energy = 5
    outgoing_modifiers = []
    incoming_modifiers = []

    def __init__(self, card_queue, player, starting_shield=0, initial_effects=()):
        self.card_queue = card_queue
        self.player = player
        self.shield = starting_shield
        self.deck = Deck(copy(player.inventory.cards))
        self.hand = Hand()
        self.discard = Discard()
        self.effects = EffectEnum(initial_effects)
        self.modifiers = {'attack': [a], 'defence': [d]}

    def start_combat(self):
        self.deck.shuffle()
        self.energy = 5
        self.draw_slice(0, self.starting_draw - 1)

    def start_turn(self):
        self.shield = 0
        self.energy = 5
        self.draw()

    def draw(self):
        if len(self.deck.cards) <= 0:
            self.deck.shuffle_discard(self.discard)
        self.hand.draw(self.deck.pick(0))

    def draw_slice(self, start, stop, step=1):
        if len(self.deck.cards) <= 0:
            self.deck.shuffle_discard(self.discard)
        self.hand.draw_slice(self.deck.pick_slice(start, stop, step))

    def end_turn(self): pass

    def select_card(self, index):
        self.selected_card = index

    def play_card(self, target, position):
        cost = self.send_card_attributes(self.hand.cards[self.selected_card].get_attributes()).cost
        if self.energy - cost <=0:
            return
        self.energy -= cost
        played_card = self.hand.play(self.card_queue, self, self.selected_card, target, position)
        self.discard.discard(played_card)

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
