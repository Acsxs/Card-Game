import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
font = pygame.font.SysFont('Minecraft', 40)
cost = font.render("2", 0, (0, 0, 0))
name = font.render("Lightning", 0, (0, 0, 0))
font = pygame.font.SysFont('Minecraft', 30)
description = font.render.autofit.text("Deal 2 Damage, Temporarily stuns the enemy, disabling it from using attacking "
                                       "moves for the turn.", 0, (0, 0, 0))
# text.fill((255,0,0))
#test

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

surface = pygame.image.load("data/assets/cards/Common Lightning.png")
surface_tranformed = pygame.transform.scale(surface, (184, 165))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    screen.blit(surface, (0, 0))
    screen.blit(cost, (65, 58))
    screen.blit(name, (115, 59))
    screen.blit(description, (42, 300))
    pygame.display.update()
pygame.quit()
sys.exit()
