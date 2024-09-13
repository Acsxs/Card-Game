from cards.base_card import Card
from consts import HAND_CARD_SIZE, CARD_SIZE
from cards.enemy_card import EnemyCard

CARDS = [
    Card("Lightning", cost=1, damage=3),
    Card("Shield", cost=1, shield=3),
    EnemyCard("Enemy Attack", damage_range=(3, 7)),
    EnemyCard("Enemy Block", shield_range=(3, 6))
]

