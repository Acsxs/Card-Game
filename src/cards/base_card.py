from events import *
from player.player import Player


class Card(EventBroadcaster):
    target = None
    in_hand = False
    modifiers = {
        'cost': [],
        'shield': [],
        'heal': [],
        'damage': [],
        'effects': [],
        'meta': []
    }

    def __init__(self, event_handler, name, cost=0, shield=0, heal=0, damage=0, effects=(), meta=()):
        EventBroadcaster.__init__(self, event_handler)
        self.name = name
        self.base_attributes = {
            'cost': cost,
            'shield': shield,
            'heal': heal,
            'damage': damage,
            'effects': effects,
            'meta': meta
        }

    def change_target(self, target):
        self.target = target

    def queue_card(self, queue):
        if not self.in_hand:
            return
        if self.target is None:
            return
        queue.append(self)

    def calculate(self, dtype):
        result = self.base_attributes[dtype]
        for function in self.modifiers[dtype]:
            result = function(result)
        return result

    def apply_card_effects(self):
        target = 'Player' if issubclass(self.target, Player) else 'Enemy'
        if self.calculate('damage') != 0:
            self.broadcast_event(Event(f"CardAttack{target}", (self.calculate('damage'), self.target)))

        if (self.calculate('shield') != 0) and (self.calculate('heal') != 0):
            self.broadcast_event(Event(f"CardDefend{target}", (self.calculate('shield'), self.calculate('heal'), self.target)))

        if len(self.calculate('effects')) != 0:
            self.broadcast_event(Event(f"CardEffect{target}", (self.calculate('effects'), self.target)))

        if len(self.calculate('meta')) != 0:
            self.broadcast_event(Event("CardMetaEffectCard", self.calculate('meta')))

        return True

    def to_string(self):
        return f"Name: {self}\n" \
            + "---------------\n" \
            + f"Attack: {self.calculate("damage")}\n" \
            + f"Defense: {self.calculate('shield')}/{self.calculate('heal')}" \
            + f"Effects: {self.calculate('effects')}" \
            + f"Meta: {self.calculate('meta')}"
