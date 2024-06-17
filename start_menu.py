import pygame
import sys


class Button:
    def __init__(self, colour, rect, text=None, border_radius=20):
        self.text = text or pygame.font.SysFont('Arial', 36).render('', True, (0, 0, 0))
        self.colour = colour
        self.rect = rect
        self.text_rect = self.text.get_rect(center=self.rect.center)
        self.border_radius = border_radius

    def hover_function(self, surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, [component - 40 for component in self.colour], self.rect,
                             border_radius=self.border_radius)
        else:
            pygame.draw.rect(surface, self.colour, self.rect, border_radius=self.border_radius)
        # Draw button text
        screen.blit(self.text, self.text_rect)


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
pygame.display.set_caption('Start Menu Test')

# Fill screen with black
screen.fill(BLACK)

# Button setup
button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2),
                          (button_width, button_height))

# Font setup
font = pygame.font.SysFont('Arial', 36)
button_text = font.render('Press me :P', True, BLACK)

button = Button(button_color, 20, 'Press me :P', 20)

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
    mouse = pygame.mouse.get_pos()

    # Update display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
