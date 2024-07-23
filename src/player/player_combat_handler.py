from copy import copy
from events import *
from player.hand import Hand
from player.deck import Deck
from effects.base_effect import EffectEnum
from player.discard import Discard


class PlayerCombatHandler(EventBroadcaster, EventListener):
    starting_draw = 7
    selected_card = None
    energy = 5

    def __init__(self, event_handler, card_queue, player, starting_shield=0, initial_effects=()):
        EventBroadcaster.__init__(self, event_handler)
        EventListener.__init__(self, event_handler, ['CardAttackPlayer', 'CardDefendPlayer', 'CardEffectPlayer'])
        self.card_queue = card_queue
        self.player = player
        self.shield = starting_shield
        self.deck = Deck(event_handler, copy(player.inventory.cards))
        self.hand = Hand(event_handler)
        self.discard = Discard(event_handler)
        self.effects = EffectEnum(initial_effects)
        self.modifiers = {'attack': [a], 'defence': [d]}

    def start_combat(self):
        self.deck.shuffle()
        self.energy = 5
        self.draw_slice(0, self.starting_draw - 1)

    def start_turn(self):
        self.broadcast(Event("PlayerStartTurn"))
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

    def end_turn(self):
        self.broadcast(Event("PlayerEndTurn"))

    def select_card(self, index):
        self.selected_card = index

    def play_card(self, target, position):
        played_card = self.hand.play(self.card_queue, self, self.selected_card, target, position)
        if played_card is None:
            return
        self.discard.discard(played_card)

    def parse_event(self, event):
        if event.type == 'CardAttackPlayer':
            unshielded = event.content[0] - self.shield
            if unshielded < 0:
                self.shield = -unshielded
                return
            self.player.health -= unshielded
            self.shield = 0
            return
        elif event.type == 'CardDefendPlayer':
            self.shield += event.content[0]
            self.player.health += event.content[1]
            return
        elif event.type == 'CardEffectPlayer':
            self.effects.append_effects(event.content[0])
