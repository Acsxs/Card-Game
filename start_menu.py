import pygame
import sys
from UI.button import *

pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 600
WHITE = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Start Menu Test')

button_surf1 = pygame.Surface((250, 50), pygame.SRCALPHA)
button_surf1.fill(pygame.Color(175, 175, 175))
button_surf2 = pygame.Surface((250, 50), pygame.SRCALPHA)
button_surf2.fill(pygame.Color(175, 175, 175))
button_surf3 = pygame.Surface((250, 50), pygame.SRCALPHA)
button_surf3.fill(pygame.Color(175, 175, 175))
button_surf4 = pygame.Surface((250, 50), pygame.SRCALPHA)
button_surf4.fill(pygame.Color(175, 175, 175))


# Font setup
font = pygame.font.SysFont('Arial', 36, bold=False)

text_surface = font.render('Card Game', True, WHITE, None)
text_rect = text_surface.get_rect(center=(WIDTH//2, 75))

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


button1 = Button(button_surf1, (50, 450), lambda: print("Settings"))
button2 = Button(button_surf2, (50, 375), lambda: print("Card Encyclopedia"))
button3 = Button(button_surf3, (50, 525), lambda: print("Quit"))
button4 = Button(button_surf4, (50, 300), lambda: print("Start"))

button_group = ButtonGroup((WIDTH, HEIGHT), button1, button2, button3, button4)

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
    screen.blit(text_surface, text_rect)
    button_group.render(screen)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
