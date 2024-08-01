from effects.base_effect import Effect


class Poison(Effect):
    type = "poison"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.health -= self.stack
        self.stack -= 1


class Weakness(Effect):
    type = "weakness"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.attack -= self.stack
        weakness = lambda damage: int(0.75 * damage)
        target.modifiers['attack'].append(weakness)
        self.stack -= 1


class Vulnerable(Effect):
    type = "vulnerable"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.vulnerable -= self.stack
        vulnerable = lambda shield: int(0.75 * shield)
        target.modifiers['shield'].append(vulnerable)
        self.stack -= 1


class Immunity(Effect):
    type = "immunity"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.immunity -= self.stack
        immunity = lambda damage: int(0 * damage)
        target.modifiers['damage'].append(immunity)
        self.stack -= 1


class Stun(Effect):
    type = "stun"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.stun -= self.stack
        stun = lambda damage: int(0 * damage)
        target.modifiers['attack'].append(stun)
        self.stack -= 1


class Poison(Effect):
    type = "poison"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply (self, target):
        target.poison -= self.stack
        poison = lambda health: int(1 * self.stack)
        target.modifiers['health'].append(poison)
        self.stack -= 1


class Strength(Effect):
    type = "strength"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.attack -= self.stack
        strength = lambda damage: int(1.25 * damage)
        target.modifiers['attack'].append(strength)
        self.stack -= 1


class Health_Pool(Effect):
    type = "health_pool"

    def __init__(self, stack):
        super().__init__()
        self.stack = stack

    def apply(self, target):
        target.health_pool -= self.stack
        health_pool = lambda health: (self.stack + health)
        target.modifiers['health'].append(health_pool)
        self.stack -= 1
