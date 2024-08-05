from attributes import Attributes


class Card:
    def __init__(self,  name, cost=0, shield=0, heal=0, damage=0, effects=(), other=()):
        self.name = name
        self.base_attributes = Attributes(cost, shield, heal, damage, effects, other)

    def get_attributes(self):
        return self.base_attributes

    def to_string(self):
        return f"Name: {self}\n" \
            + "--------------------------------------\n" \
            + f"Attack: {self.base_attributes.damage} \n" \
            + f"Defense: {self.base_attributes.shield}/{self.base_attributes.heal}\n" \
            + f"Effects: {self.base_attributes.effects}\n" \
            + f"other: {self.base_attributes.other}\n"

    def copy(self):
        return Card(
            self.name,
            self.base_attributes.cost,
            self.base_attributes.shield,
            self.base_attributes.heal,
            self.base_attributes.damage,
            self.base_attributes.effects,
            self.base_attributes.other
        )
