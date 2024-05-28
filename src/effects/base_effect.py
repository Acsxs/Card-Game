
class Effect:
    type = None # Name string literal i.e. "poison", "weak"
    def __init__(self): pass

    def apply(self, target): pass


class EffectEnum:
    def __init__(self):
        self.iterable = []

    def append_effect(self, effect: Effect, count=None):
        types = [i[0].type for i in self.iterable]
        if effect.type in types:
            self.iterable[types.index(effect.type)][1] += effect
            return
        self.iterable.append([effect, count or 1])

    def resolve_effects(self, target):
        for effect in self.iterable:
            effect[0].apply(target)

    def tick_counters(self):
        for index in range(len(self.iterable)):
            self.iterable[index][1] -= 1
            if self.iterable[index][1] <= 0:
                self.iterable.pop(index)
