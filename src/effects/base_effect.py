from attributes import AttributeTransformation

class Effect:
    type = None # Name string literal i.e. "poison", "weak"
    stack = 1
    attribute_transformation: AttributeTransformation
    def __init__(self): pass

    def start_effect(self, target): pass

    def apply(self, target): pass

    def end_effect(self, target): pass


class EffectEnum:
    def __init__(self, master, effects=()):
        self.master = master
        self.iterable = list(effects)

    def append_effect(self, effect: Effect):
        types = [i[0].type for i in self.iterable]
        if effect.type in types:
            self.iterable[types.index(effect.type)].stack += effect.stack
            return
        effect.start_effect(self.master)
        self.iterable.append(effect)

    def append_effects(self, effects):
        for effect in effects:
            self.append_effect(effect)

    def tick_counters(self):
        for index, effect in enumerate(self.iterable):
            effect.apply(self.master)
            self.iterable[index].stack -= 1
            if effect.stack <= 0:
                effect.end_effect(self.master)
                self.iterable.pop(index)
