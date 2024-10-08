import pygame

from UI.player_UI_controller import PlayerUIController
from combat.combat_handler import Combat
from UI.menu import Menu
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, NO_COLOUR
from UI.button import Button
from cards.card_def import *
from UI.stamina_indicator import StaminaIndicator


class CombatInterface(Menu):
    def __init__(self, mouse, player):
        super().__init__(mouse, pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA))
        end_turn_button_surface = pygame.Surface((100, 50))
        end_turn_button_surface.fill((255, 0, 0))
        self.register_button(Button(end_turn_button_surface, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 50), command=self.end_turn))
        self.selected_card = None
        self.combat = Combat(self, player)
        self.player_controller = PlayerUIController(mouse, self)
        self.player_stamina_indicator = StaminaIndicator((350, 200), (player.health, self.combat.player.shield), (105, 60))
        self.enemy_stamina_indicator = StaminaIndicator((750, 200), (self.combat.enemy.health, self.combat.enemy.shield), (105, 60))
        self.player_surface = pygame.transform.scale(pygame.image.load("data/assets/Test Character.png").convert_alpha(), (105,150))
        self.enemy_surface = pygame.transform.scale(pygame.image.load("data/assets/Edward.png").convert_alpha(), (105, 40))

    def enemy_set_card(self, card, position):
        self.player_controller.playing_board.cards[position] = CARDS_TO_UIS[card.name].copy()
        self.player_controller.playing_board.locked.append(position)

    def register_board_pick(self, index):
        if index is None:
            return
        self.player_controller.selected_card = self.player_controller.playing_board.pick_card(index)
        self.selected_card = self.combat.card_queue.pick(index)

    def register_hand_pick(self, index):
        if index is None:
            return
        self.player_controller.selected_card = self.player_controller.hand_ui.pick_card(index)
        self.selected_card = self.combat.player.pick_hand(index)

    def register_board_set(self, index):
        self.combat.card_queue.submit(self.selected_card, self.combat.player, self.combat.enemy, index)
        self.selected_card = None

    def register_hand_set(self):
        self.combat.player.hand.cards.append(self.selected_card)
        self.selected_card = None

    def register_hand_draw(self):
        card = self.combat.player.draw()
        self.player_controller.hand_ui.cards.append(CARDS_TO_UIS[card.name].copy())

    def register_hand_draw_slice(self, start, stop, step=1):
        cards = self.combat.player.draw_slice(start, stop, step)
        self.player_controller.hand_ui.cards.extend([CARDS_TO_UIS[card.name].copy() for card in cards])

    def end_turn(self):
        self.combat.end_turn()
        self.player_stamina_indicator.update_surf((self.combat.player.player.health, self.combat.player.shield))
        self.enemy_stamina_indicator.update_surf((self.combat.enemy.health, self.combat.enemy.shield))
        self.player_controller.playing_board.clear()
        self.discard()
        self.start_turn()

    def start_turn(self):
        self.combat.start_turn()

    def update_surface(self):
        self.surface.fill(NO_COLOUR)
        self.player_controller.draw(self.surface)
        self.player_stamina_indicator.draw(self.surface)
        self.enemy_stamina_indicator.draw(self.surface)
        self.surface.blit(self.player_surface, (350, 200))
        self.surface.blit(self.enemy_surface, (750, 200))

    def discard(self):
        self.player_controller.hand_ui.cards.clear()

