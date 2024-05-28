from copy import copy
from events import *
from combat.hand import Hand
from combat.deck import Deck


class PlayerCombatHandler(EventBroadcaster):
    starting_draw = 7
    selected_card = None

    def __init__(self, event_handler, card_queue, player):
        EventBroadcaster.__init__(self, event_handler)
        self.card_queue = card_queue
        self.player = player
        self.hand = Hand(event_handler)
        self.deck = Deck(event_handler, copy(player.inventory.cards))

    def start_combat(self):
        self.deck.shuffle()
        self.hand.draw_slice(self.deck.pick_slice(0, self.starting_draw-1))

    def start_turn(self):
        self.broadcast_event(Event("PlayerStartTurn"))
        self.hand.draw(self.deck.pick(0))

    def end_turn(self):
        self.broadcast_event(Event("PlayerEndTurn"))

    def select_card(self, index):
        self.selected_card = index

    def play_card(self, target, position):
        self.hand.play(self.card_queue, self.selected_card, target, position)



