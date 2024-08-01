import pygame


class Controller:
    controls = {
        "pos1": pygame.K_1,
        "pos2": pygame.K_2,
        "pos3": pygame.K_3,
        "pos4": pygame.K_4,
        "pos5": pygame.K_5,
        "pos6": pygame.K_6,
        "pos7": pygame.K_7,
        "pos8": pygame.K_8,
        "pos9": pygame.K_9,
        "pos10": pygame.K_0,
        "return": pygame.K_RETURN,
    }

    def __init__(self):
        self.parser = {}
        for control, key in self.controls.items():
            if key not in self.parser.keys():
                self.parser[key] = []
            self.parser[key].append(control)

    def parse_keydown_event(self, events):
        active_controls = []
        for event in events:
            if event.key in self.parser.keys():
                active_controls += self.parser[event.key]
                continue
        if len(active_controls) == 0:
            return None
        return active_controls
