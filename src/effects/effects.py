from effects.base_effect import Effect
from attributes import AttributeTransformation


class Poison(Effect):
    type = "poison"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.health -= self.stack


class Weakness(Effect):
    type = "weakness"
    attribute_transformation = AttributeTransformation(damage=lambda damage: int(0.75 * damage))

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def start_effect(self, target):
        target.outgoing_modifiers.append(self.attribute_transformation)

    def end_effect(self, target):
        target.outgoing_modifiers.remove(self.attribute_transformation)


class Vulnerable(Effect):
    type = "vulnerable"
    attribute_transformation = AttributeTransformation(shield=lambda shield: int(0.75 * shield))

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def start_effect(self, target):
        target.outgoing_modifiers.append(self.attribute_transformation)

    def end_effect(self, target):
        target.outgoing_modifiers.remove(self.attribute_transformation)


class Immunity(Effect):
    type = "immunity"
    attribute_transformation = AttributeTransformation(damage=lambda damage: 0)

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def start_effect(self, target):
        target.incoming_modifiers.append(self.attribute_transformation)

    def end_effect(self, target):
        target.incoming_modifiers.remove(self.attribute_transformation)


class Stun(Effect):
    type = "stun"
    attribute_transformation = AttributeTransformation(damage=lambda damage: 0)

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def start_effect(self, target):
        target.outgoing_modifiers.append(self.attribute_transformation)

    def end_effect(self, target):
        target.outgoing_modifiers.remove(self.attribute_transformation)


class Strength(Effect):
    type = "strength"
    attribute_transformation = AttributeTransformation(damage=lambda damage: int(1.25 * damage))

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def start_effect(self, target):
        target.outgoing_modifiers.append(self.attribute_transformation)

    def end_effect(self, target):
        target.outgoing_modifiers.remove(self.attribute_transformation)


class Health_Pool(Effect):
    type = "health_pool"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.health_pool += self.stack
