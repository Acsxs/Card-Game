import pygame
import sys
from UI.card_UI_component import CardUIComponent
from consts import *
import numpy as np
from UI.hand_UI_component import HandUIComponent
from UI.button import Button
from input.mouse_tracker import Mouse, MouseTrackerGroup
from consts import *
from functools import partial


class Menu:
    def __init__(self, mouse, surface, *args):
        self.surface = surface
        self.mouse = mouse
        self.button_group = MouseTrackerGroup((SCREEN_WIDTH, SCREEN_HEIGHT), mouse, *args)

    def update(self):
        self.button_group.update()

    def draw(self, surface):
        surface.blit(self.surface, (0, 0))
        self.button_group.draw(surface)

    def register_button(self, button):
        self.button_group.add(button)


class MenuHandler:
    def __init__(self, *args):

        self.menu = None
        self.menus = args
        assert self.menus is not None
        for menu in self.menus:
            for button in menu.button_group.trackers:
                button.command = partial(set_menu, menu)

    def update(self):
        if self.menu is None:
            return
        self.menu.update()

    def draw(self, surface):
        if self.menu is None:
            return
        self.menu.draw(surface)

    def set_menu(self, menu):
        self.menu = menu


def get_font(size):
    return pygame.font.SysFont('Upheaval TT -BRK-', size)


def set_menu():
    global current_screen
    current_screen = "main menu"


def set_play():
    global current_screen
    current_screen = "play"


def set_options():
    global current_screen
    current_screen = "options"


def set_quit():
    pygame.quit()
    sys.exit()


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("data/assets/background 2.png")

mouse = Mouse()

play_back_image = pygame.Surface((100, 100))
play_back_image.fill((255, 0, 0))
PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "Black")
PLAY_RECT = PLAY_TEXT.get_rect(center=(500, 250))
# play_buttons = MouseTrackerGroup(SCREEN.get_size(), mouse, PLAY_BACK)

OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 250))
# options_buttons = MouseTrackerGroup(SCREEN.get_size(), mouse, OPTIONS_BACK)

MENU_TEXT = get_font(100).render("Tower Master", True, "#b576e7")
MENU_RECT = MENU_TEXT.get_rect(center=(650, 100))

# main_menu_buttons = MouseTrackerGroup(SCREEN.get_size(), mouse, play_button, options_button, quit_button)
BG.blit(MENU_TEXT, MENU_RECT)
main_menu = Menu(mouse, BG)
options_menu = Menu(mouse, BG)
play_menu = Menu(mouse, BG)
menu_handler = MenuHandler(main_menu)

play_button = Button(pygame.image.load("data/assets/Start Button.png"), pos=(500, 250),
                     command=partial(menu_handler.set_menu, play_menu))
options_button = Button(pygame.image.load("data/assets/Setting Wheel.png"), pos=(1150, 580),
                        command=partial(menu_handler.set_menu, options_menu))
quit_button = Button(pygame.image.load("data/assets/Quit Button.png"), pos=(500, 450), command=set_quit)

main_button = Button(play_back_image, pos=(500, 250), command=partial(menu_handler.set_menu, main_menu))

main_menu.register_button(play_button)
main_menu.register_button(options_button)
main_menu.register_button(quit_button)

play_menu.register_button(main_button)
options_menu.register_button(main_button)

menu_handler.set_menu(main_menu)

# def play(screen):
#     screen.fill((255, 255, 255))
#     mouse.update()
#     play_buttons.update()
#     play_buttons.draw(screen)
#     screen.blit(PLAY_TEXT, PLAY_RECT)
#
#
# def options(screen):
#     screen.fill((255, 255, 255))
#     mouse.update()
#     options_buttons.update()
#     options_buttons.draw(screen)
#     screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
#
#
# def main_menu(screen):
#     screen.blit(BG, (0, 0))
#     mouse.update()
#     main_menu_buttons.update()
#     main_menu_buttons.draw(screen)
#     screen.blit(MENU_TEXT, MENU_RECT)


current_screen = "main menu"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mouse.update()
    menu_handler.update()
    menu_handler.draw(SCREEN)
    # if current_screen == "main menu":
    #     main_menu(SCREEN)
    # if current_screen == "play":
    #     play(SCREEN)
    # if current_screen == "options":
    #     options(SCREEN)
    pygame.display.flip()

