# from UI.floating_card import FloatingCard
from cards.base_card import Card
from consts import HAND_CARD_SIZE, CARD_SIZE
from cards.enemy_card import EnemyCard
# import pygame

# if not pygame.get_init():
#     pygame.init()

CARDS = [
    Card("Lightning", cost=1, damage=3),
    Card("Shield", cost=1, shield=3),
    EnemyCard("Enemy Attack", damage_range=(3, 7)),
    EnemyCard("Enemy Block", shield_range=(3, 6))
]

# CARD_UIS = [
#     FloatingCard(HAND_CARD_SIZE, pygame.image.load("data/assets/cards/Common Lightning.png"), 1, "Lighting", "Deals 3 damage"),
#     FloatingCard(HAND_CARD_SIZE, pygame.image.load("data/assets/cards/Common Shield.png"), 1, "Shield", "Shields 3 damage"),
#
#     FloatingCard(CARD_SIZE, pygame.image.load("data/assets/cards/Enemy Slash.png"), 0, "Enemy Attack", "Deals 3-7 damage"),
#     FloatingCard(CARD_SIZE, pygame.image.load("data/assets/cards/Enemy Block.png"), 0, "Enemy Block", "Shields 3-6 damage")
# ]

# CARDS_TO_UIS = {card.name: ui for card, ui in zip(CARDS, CARD_UIS)}
# UIS_TO_CARDS = {ui.name: card for card, ui in zip(CARDS, CARD_UIS)}
