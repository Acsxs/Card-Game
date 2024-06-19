import pygame
import sys
from UI.button import *

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Start Menu Test')

button_surf1 = pygame.Surface((300, 100))
button_surf1.fill((255, 255, 255))
button_surf2 = pygame.Surface((200, 75))
button_surf2.fill((255, 255, 255))

# Font setup
font = pygame.font.SysFont('Arial', 36)
button_text1 = font.render('Hello, World', True, (0, 0, 0))
button_text_rect1 = button_text1.get_rect(center=button_surf1.get_rect().center)
button_surf1.blit(button_text1, button_text_rect1)
button_text2 = font.render('Start', True, (0, 0, 0))
button_text_rect2 = button_text2.get_rect(center=button_surf2.get_rect().center)
button_surf2.blit(button_text2, button_text_rect2)

button1 = Button(button_surf1, (200, 400), lambda: print("Hello, World"))
button2 = Button(button_surf2, (200, 100), lambda: print("Start"))
button_group = ButtonGroup((WIDTH, HEIGHT), button1, button2)

# Main loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_group.on_click(event.pos)
    screen.fill((0, 0, 0))
    button_group.render(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
