import random
from cards.base_card import Card
from events import *


class Enemy(EventBroadcaster):
    def __init__(self,event_handler,card_queue, health,  damage_range, shielding_range):
        EventBroadcaster.__init__(self, event_handler)
        self.health = health
        self.damage_range = damage_range
        self.shielding_range = shielding_range
        self.card_queue = card_queue

    def get_intent(self):
        return random.choice(['attack', 'defence'])

    def submit_intent(self, player):
        if self.get_intent() == 'attack':
            card = Card(self.event_handler,"Enemy Attack", 0, 0,0, random.randint(self.damage_range[0], self.damage_range[1]))
            card.target = player
            self.card_queue.submit(card, random.randint(1,self.card_queue.queue_length-1))
        else:
            card = Card(self.event_handler, "Enemy Defence", 0, random.randint(self.shielding_range[0], self.shielding_range[1]), 0, 0)
            card.target = player
            self.card_queue.submit(card, random.randint(1,self.card_queue.queue_length-1))

    def start_turn(self, player):
        for i in range(random.randint(0,3)):
            self.submit_intent(player)

