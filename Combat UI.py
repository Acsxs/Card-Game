import pygame
import sys

pygame.init()
WIDTH = 1280
HEIGHT = 720
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('image')

imp = pygame.image.load("data/assets/Deck.png")

imp_position = (250, 250)

imp = pygame.transform.scale(imp, imp_position)


status = True
while status:
    for i in pygame.event.get():
        if i.type == pygame.quit:
            status = False
    screen.fill(BLACK)
    screen.blit(imp, imp_position)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
