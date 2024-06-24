import pygame
import sys

pygame.init()
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('image')

image = pygame.image.load("C:\\Users\\200142\\Documents\\Year 12\\Card-Game\\data\\assets\\Deck.png")
screen.blit(image (0, 0))




