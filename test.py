import pygame
import sys
import textwrap

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
font = pygame.font.SysFont('Minecraft', 40)
cost = font.render("2", 0, (0, 0, 0))
name = font.render("Lightning", 0, (0, 0, 0))
font = pygame.font.SysFont('Minecraft', 30)
description = "Deal 2 Damage, Temporarily stuns the enemy, disabling it from using attacking moves for the turn."
# text.fill((255,0,0))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

surface = pygame.image.load("data/assets/cards/Common Lightning.png")
surface_transformed = pygame.transform.scale(surface, (184, 165))


def drawText(surface, text, color, font, aa=False, bkg=None):
    rect = pygame.Rect(42, 297, 280, 160)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 2

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    screen.blit(surface, (0, 0))
    screen.blit(cost, (65, 58))
    screen.blit(name, (115, 59))
    # screen.blit(description, (42, 300))
    drawText(screen, description, (0,0,0), font)
    pygame.display.update()
pygame.quit()
sys.exit()
