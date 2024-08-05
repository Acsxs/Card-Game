from typing import Callable
from typing import Collection


def no_transformation(x):
    return x


class AttributeTransformation:
    cost: Callable
    shield: Callable
    heal: Callable
    damage: Callable
    effects: Callable
    other: Callable

    def __init__(
            self,
            cost=no_transformation,
            shield=no_transformation,
            heal=no_transformation,
            damage=no_transformation,
            effects=no_transformation,
            other=no_transformation,
    ):
        self.cost = cost
        self.shield = shield
        self.heal = heal
        self.damage = damage
        self.effects = effects
        self.other = other


class Attributes:
    cost: int
    shield: int
    heal: int
    damage: int
    effects: Collection[object]
    other: Collection[Callable]

    def __init__(self, cost=0, shield=0, heal=0, damage=0, effects=(), other=(),):
        self.cost = cost
        self.shield = shield
        self.heal = heal
        self.damage = damage
        self.effects = effects
        self.other = other

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
