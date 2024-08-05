from combat.card_queue import CardQueue
from player.player_combat_handler import PlayerCombatHandler
from enemy.enemy import Enemy
from consts import CARD_SLOTS


class Combat:
    def __init__(self, interface, player):
        self.card_queue = CardQueue(CARD_SLOTS)
        self.player = PlayerCombatHandler(self.card_queue, interface, player)
        self.enemy = Enemy(self.card_queue, interface, 15)

    def start_combat(self):
        self.player.start_combat()
        self.enemy.start_combat(self.player)

    def start_turn(self):
        self.player.start_turn()

    def end_turn(self):
        self.player.end_turn()
