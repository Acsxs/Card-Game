import pygame, sys
from UI.button import Button
from UI.mouse_tracker import Mouse, MouseTrackerGroup
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
