from cards.base_card import Card
from attributes import Attributes
import random


class EnemyCard(Card):
    def __init__(self, name, shield_range=(0, 0), heal_range=(0, 0), damage_range=(0, 0)):
        super().__init__(name, 0, 0, 0, 0)
        self.shield_range = shield_range
        self.heal_range = heal_range
        self.damage_range = damage_range

    def get_attributes(self):
        return Attributes(0, random.randint(*self.shield_range), random.randint(*self.heal_range), random.randint(*self.damage_range))

    def copy(self):
        return EnemyCard(self.name, self.shield_range, self.heal_range, self.damage_range)