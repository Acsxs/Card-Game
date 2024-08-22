from player.player import Player
from player.player_combat_handler import PlayerCombatHandler
from combat.card_queue import CardQueue
from cards.card_def import *


class Enemy:
    def receive_card_attributes(self, _): pass


enemy = Enemy()

card_queue = CardQueue(6)

player = Player()

for i in range(3):
    player.inventory.cards.append(CARDS[0])
    player.inventory.cards.append(CARDS[1])

player_combat_handler = PlayerCombatHandler(card_queue, player)

player_combat_handler.start_combat()
while input("End?").lower() == 'no':
    player_combat_handler.start_turn()
    for i in range(5):
        player_combat_handler.draw()
    while input("End Turn?  ").lower() == 'no':
        print(f"Energy: {player_combat_handler.energy}")
        card_index = int(input("Choose card by index\n" + player_combat_handler.hand.to_string()))
        player_combat_handler.play_card(
            player_combat_handler.hand.pick(card_index),
            enemy,
            int(input("Choose position\n" + card_queue.to_string()))
        )
    card_queue.play()
