import sys

from cards.card_def import *
from combat_interface import CombatInterface
from consts import *
from input.mouse_tracker import Mouse
from player.player import Player

if not pygame.get_init():
    pygame.init()

player = Player()
for i in range(24):
    player.inventory.cards.append(CARDS[0].copy())
    player.inventory.cards.append(CARDS[1].copy())

mouse = Mouse()
combat_interface = CombatInterface(mouse, player)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")


# indicator = StaminaIndicator(None, (100, 300), (20, 10))
# indicator.update_surf((50, 50))
# rect = pygame.Rect(40, 297, 300, 120)
combat_interface.combat.start_combat()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    mouse.update()
    combat_interface.update()
    combat_interface.update_surface()
    combat_interface.draw(screen)

    pygame.display.update()
pygame.quit()
sys.exit()
