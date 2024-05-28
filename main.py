from player.player import Player
from events import EventHandler
from cards.base_card import Card
from combat.combat_handler import Combat

player = Player()

event_handler = EventHandler()

card1 = Card(event_handler, "Attack", 1, 0, 0, 4)
card2 = Card(event_handler, "Defence", 1, 4, 0, 0)

player.inventory.cards.append(card1)
player.inventory.cards.append(card2)

combat = Combat(event_handler, player)


while True:
    combat.start_turn()