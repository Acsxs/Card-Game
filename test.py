import sys

from cards.card_def import *
from combat_interface import CombatInterface
from consts import *
from input.mouse_tracker import Mouse
from player.player import Player
from UI.menu import Menu, MenuHandler
from UI.button import Button
from functools import partial

if not pygame.get_init():
    pygame.init()

def get_font(size):
    return pygame.font.SysFont('Upheaval TT -BRK-', size)

def quit():
    pygame.quit()
    sys.exit()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

BG = pygame.transform.scale(pygame.image.load("data/assets/background 2.png"),(SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
for i in range(24):
    player.inventory.cards.append(CARDS[0].copy())
    player.inventory.cards.append(CARDS[1].copy())

mouse = Mouse()
combat_interface = CombatInterface(mouse, player)

play_back_image = pygame.Surface((100, 100))
play_back_image.fill((255, 0, 0))

OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(500, 250))

MENU_TEXT = get_font(100).render("Tower Master", True, "#b576e7")
MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH//2, 75))

BG.blit(MENU_TEXT, MENU_RECT)
main_menu = Menu(mouse, BG)
options_menu = Menu(mouse, BG)
play_menu = combat_interface
menu_handler = MenuHandler(main_menu)

play_button = Button(pygame.image.load("data/assets/Start Button.png"), pos=(SCREEN_WIDTH//2- 100, 200),
                     command=partial(menu_handler.set_menu, play_menu))
options_button = Button(pygame.image.load("data/assets/Setting Wheel.png"), pos=(SCREEN_WIDTH-150, SCREEN_HEIGHT-150),
                        command=partial(menu_handler.set_menu, options_menu))
quit_button = Button(pygame.image.load("data/assets/Quit Button.png"), pos=(SCREEN_WIDTH//2- 100, 450), command=quit)

main_button = Button(play_back_image, pos=(0, 0), command=partial(menu_handler.set_menu, main_menu))

main_menu.register_button(play_button)
main_menu.register_button(options_button)
main_menu.register_button(quit_button)

play_menu.register_button(main_button)
options_menu.register_button(main_button)

menu_handler.set_menu(main_menu)

combat_interface.combat.start_combat()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    mouse.update()
    menu_handler.update()
    if menu_handler.menu == combat_interface:
        combat_interface.update()
        combat_interface.update_surface()
    menu_handler.draw(screen)

    pygame.display.flip()
pygame.quit()
sys.exit()
