import pygame
import sys
from UI.button import *

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Start Menu Test')

button_surf1 = pygame.Surface((250, 50))
button_surf1.fill((255, 255, 255))
button_surf2 = pygame.Surface((250, 50))
button_surf2.fill((255, 255, 255))
button_surf3 = pygame.Surface((250, 50))
button_surf3.fill((255, 255, 255))
button_surf4 = pygame.Surface((250, 50))
button_surf4.fill((255, 255, 255))
button_surf5 = pygame.Surface((400, 100))
button_surf5.fill((255, 255, 255))

# Font setup
font = pygame.font.SysFont('Arial', 36)

button_text1 = font.render('Settings', True, (0, 0, 0))
button_text_rect1 = button_text1.get_rect(center=button_surf1.get_rect().center)
button_surf1.blit(button_text1, button_text_rect1)
button_text2 = font.render('Card Encyclopedia', True, (0, 0, 0))
button_text_rect2 = button_text2.get_rect(center=button_surf2.get_rect().center)
button_surf2.blit(button_text2, button_text_rect2)
button_text3 = font.render('Quit', True, (0, 0, 0))
button_text_rect3 = button_text3.get_rect(center=button_surf3.get_rect().center)
button_surf3.blit(button_text3, button_text_rect3)
button_text4 = font.render('Start', True, (0, 0, 0))
button_text_rect4 = button_text4.get_rect(center=button_surf4.get_rect().center)
button_surf4.blit(button_text4, button_text_rect4)
button_text5 = font.render('Card Game', True, (0, 0, 0))
button_text_rect5 = button_text5.get_rect(center=button_surf5.get_rect().center)
button_surf5.blit(button_text5, button_text_rect5)

button1 = Button(button_surf1, (50, 450), lambda: print("Settings"))
button2 = Button(button_surf2, (50, 375), lambda: print("Card Encyclopedia"))
button3 = Button(button_surf3, (50, 525), lambda: print("Quit"))
button4 = Button(button_surf4, (50, 300), lambda: print("Start"))
button5 = Button(button_surf5, (200, 50), lambda: print("Card Game"))
button_group = ButtonGroup((WIDTH, HEIGHT), button1, button2, button3, button4, button5)

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
