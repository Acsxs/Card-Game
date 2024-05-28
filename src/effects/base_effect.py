
class Effect:
    type = None # Name string literal i.e. "poison", "weak"
    stack = 1
    def __init__(self): pass

    def apply(self, target): pass


class EffectEnum:
    def __init__(self, effects=()):
        self.iterable = list(effects)

    def append_effect(self, effect: Effect):
        types = [i[0].type for i in self.iterable]
        if effect.type in types:
            self.iterable[types.index(effect.type)].stack += effect.stack
            return
        self.iterable.append(effect)

    def append_effects(self, effects):
        for effect in effects:
            self.append_effect(effect)

    def resolve_effects(self, target):
        for effect in self.iterable:
            effect.apply(target)

    def tick_counters(self):
        for index in range(len(self.iterable)):
            self.iterable[index].stack -= 1
            if self.iterable[index].stack <= 0:
                self.iterable.pop(index)
