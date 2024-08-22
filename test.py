import sys

from cards.card_def import *
from combat_interface import CombatInterface
from consts import *
from input.mouse_tracker import Mouse
from player.player import Player

if not pygame.get_init():
    pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

player = Player()
for i in range(24):
    player.inventory.cards.append(CARDS[0].copy())
    player.inventory.cards.append(CARDS[1].copy())

mouse = Mouse()
combat_interface = CombatInterface(mouse, player)


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

    pygame.display.flip()
pygame.quit()
sys.exit()
