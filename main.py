import pygame

from player.player import Player
from events import EventHandler
from cards.base_card import Card
from cards.card_def import CARDS
from combat.combat_handler import Combat

pygame.init()

player = Player()

for i in range(6):
    player.inventory.cards.append(CARDS[0].copy())
    player.inventory.cards.append(CARDS[1].copy())
combat = Combat(player)


while combat.enemy.health > 0:
    print(f"Player Health: {combat.player.player.health}")
    print(f"Enemy Health: {combat.enemy.health}")
    combat.start_combat()
    combat.start_turn()
    combat.player.draw_slice(0,5)
    while input("End Turn?  ").lower() == 'no':
        print(f"Energy: {combat.player.energy}")
        card_index = int(input("Choose card by index\n"+combat.player.hand.to_string()))
        combat.player.play_card(
            combat.player.hand.pick(card_index),
            combat.enemy,
            int(input("Choose position\n"+combat.card_queue.to_string()))
        )
    combat.card_queue.play()

print("You Win")

