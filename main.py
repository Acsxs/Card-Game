from player.player import Player
from events import EventHandler
from cards.base_card import Card
from combat.combat_handler import Combat

player = Player()

event_handler = EventHandler()

card1 = Card(event_handler, "Attack", 1, 0, 0, 4)
card2 = Card(event_handler, "Defence", 1, 4, 0, 0)

player.inventory.cards.append(card1)
player.inventory.cards.append(card1)
player.inventory.cards.append(card1)
player.inventory.cards.append(card1)
player.inventory.cards.append(card2)
player.inventory.cards.append(card2)
player.inventory.cards.append(card2)
player.inventory.cards.append(card2)

combat = Combat(event_handler, player)


while True:
    combat.start_combat()
    combat.start_turn()
    if input("End Turn?  ").lower() == 'no':
        combat.player.select_card(int(input("Choose card by index\n"+combat.player.hand.to_string())))
        combat.player.play_card(combat.enemy, int(input("Choose position\n"+combat.card_queue.to_string())))
    else:
        combat.card_queue.play()

