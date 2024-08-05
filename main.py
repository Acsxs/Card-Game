import pygame

from player.player import Player
from events import EventHandler
from cards.base_card import Card
from combat.combat_handler import Combat

pygame.init()

player = Player()

event_handler = EventHandler()
#test

card1 = Card("Attack", 1, 0, 0, 4)
card2 = Card("Defence", 1, 4, 0, 0)

player.inventory.cards.append(card1)
player.inventory.cards.append(card1)
player.inventory.cards.append(card1)
player.inventory.cards.append(card1)
player.inventory.cards.append(card2)
player.inventory.cards.append(card2)
player.inventory.cards.append(card2)
player.inventory.cards.append(card2)

combat = Combat(player)


while combat.enemy.health > 0:
    print(f"Player Health: {combat.player.player.health}")
    print(f"Enemy Health: {combat.enemy.health}")
    combat.start_combat()
    combat.start_turn()
    while input("End Turn?  ").lower() == 'no':
        print(f"Energy: {combat.player.energy}")
        combat.player.select_card(int(input("Choose card by index\n"+combat.player.hand.to_string())))
        combat.player.play_card(combat.enemy, int(input("Choose position\n"+combat.card_queue.to_string())))
    combat.card_queue.play()

print("You Win")

