from events import *
from player.player import Player
from dataclasses import dataclass
from typing import Callable
from typing import Collection


@dataclass
class CardAttributeTransformation:
    cost: Callable
    shield: Callable
    heal: Callable
    damage: Callable
    effects: Callable
    other: Callable


@dataclass
class CardAttributes:
    cost: int
    shield: int
    heal: int
    damage: int
    effects: Collection[object]
    other: Collection[Callable]

    def __imul__(self, other: CardAttributeTransformation):
        self.cost = other.cost(self.cost)
        self.shield = other.shield(self.shield)
        self.heal = other.heal(self.heal)
        self.damage = other.damage(self.damage)
        self.effects = other.effects(self.effects)
        self.other = other.other(self.other)

    def __mul__(self, other: CardAttributeTransformation):
        return CardAttributes(
            other.cost(self.cost),
            other.shield(self.shield),
            other.heal(self.heal),
            other.damage(self.damage),
            other.effects(self.effects),
            other.other(self.other),
        )


class Card(EventBroadcaster):
    target = None
    in_hand = False
    modifiers = []  # CardAttributeTransformation

    def __init__(self, event_handler, name, cost=0, shield=0, heal=0, damage=0, effects=(), other=()):
        EventBroadcaster.__init__(self, event_handler)
        self.name = name
        self.base_attributes = CardAttributes(cost, shield, heal, damage, effects, other)
        self.modified_attributes = self.base_attributes

    def change_target(self, target):
        self.target = target

    def calculate(self):
        for modifier in self.modifiers:
            self.modified_attributes *= modifier

    def apply_card_effects(self):
        self.calculate()
        target = 'Player' if issubclass(type(self.target), Player) else 'Enemy'
        if self.modified_attributes.damage != 0:
            self.broadcast(Event(f"CardAttack{target}", (self.modified_attributes.damage, self.target)))

        if (self.modified_attributes.shield != 0) or (self.modified_attributes.heal != 0):
            self.broadcast(Event(f"CardDefend{target}", (
                self.modified_attributes.shield,
                self.modified_attributes.heal,
                self.target
            )))

        if len(self.modified_attributes.effects) != 0:
            self.broadcast(Event(f"CardEffect{target}", (self.modified_attributes.effects, self.target)))

        if len(self.modified_attributes.other) != 0:
            self.broadcast(Event("CardFunction", self.modified_attributes.other))

    def to_string(self):
        return f"Name: {self}\n" \
            + "--------------------------------------\n" \
            + f"Attack: {self.modified_attributes.damage} ({self.base_attributes.damage})\n" \
            + (f"Defense: {self.modified_attributes.shield}/{self.modified_attributes.heal} "
               f"({self.base_attributes.shield}/{self.base_attributes.heal})\n") \
            + f"Effects: {self.modified_attributes.effects} ({self.base_attributes.effects})\n" \
            + f"other: {self.modified_attributes.other} ({self.base_attributes.other})\n"
