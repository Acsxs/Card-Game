import pygame
from UI.UI_component import UIComponent
from consts import *
import numpy as np


class PlayingBoard(UIComponent):
    def __init__(self):
        super().__init__()
        self.surface = pygame.image.load("data/assets/Playing Board.png")
        self.card_positions = [(PLAYING_BOARD_POS[0] + i * CARD_SIZE[0] + CARD_PADDING, PLAYING_BOARD_POS[1]) for i in range(CARD_SLOTS)]
    # def