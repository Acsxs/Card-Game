from combat.card_queue import CardQueue
from player.player_combat_handler import PlayerCombatHandler
from enemy.enemy import Enemy


class Combat:
    def __init__(self, player):
        self.card_queue = CardQueue(6)
        self.player = PlayerCombatHandler( self.card_queue, player)
        self.enemy = Enemy(self.card_queue, 15, (3,7), (3,6))

    def start_combat(self):
        self.player.start_combat()
        self.enemy.start_combat(self.player)

    def start_turn(self):
        self.player.start_turn()

    def end_turn(self):
        self.player.end_turn()

