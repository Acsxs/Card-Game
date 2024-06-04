import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
button_width, button_height = 200, 100
button_color = (169, 169, 169)  # Light grey
hover_color = (128, 128, 128)  # Grey
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RADIUS = 20

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Button Test')

# Button setup
button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2),
                          (button_width, button_height))

# Font setup
font = pygame.font.Font(None, 36)
button_text = font.render('Press me :P', True, BLACK)
button_text_rect = button_text.get_rect(center=button_rect.center)

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print('button pressed')

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Fill screen with white
    screen.fill(BLACK)

    # Change button color on hover
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, button_rect, border_radius=RADIUS)
    else:
        pygame.draw.rect(screen, button_color, button_rect, border_radius=RADIUS)

    # Draw button text
    screen.blit(button_text, button_text_rect)

    # Update display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
