
from dataclasses import dataclass
from typing import Callable
from typing import Collection

@dataclass
class AttributeTransformation:
    cost: Callable
    shield: Callable
    heal: Callable
    damage: Callable
    effects: Callable
    other: Callable

@dataclass
class Attributes:
    cost: int
    shield: int
    heal: int
    damage: int
    effects: Collection[object]
    other: Collection[Callable]

    def __imul__(self, other):
        self.cost = other.cost(self.cost)
        self.shield = other.shield(self.shield)
        self.heal = other.heal(self.heal)
        self.damage = other.damage(self.damage)
        self.effects = other.effects(self.effects)
        self.other = other.other(self.other)

    def __mul__(self, other):
        return Attributes(
            other.cost(self.cost),
            other.shield(self.shield),
            other.heal(self.heal),
            other.damage(self.damage),
            other.effects(self.effects),
            other.other(self.other),
        )
