import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
font = pygame.font.SysFont('Minecraft', 40)
cost = font.render("2", 0, (0, 0, 0))
name = "Lightning"
# font = pygame.font.SysFont('Minecraft', 26)
description = "Deal 2 Damage, Temporarily stuns the enemy, disabling it from using attacking moves for the turn."
# text.fill((255,0,0))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

surface = pygame.image.load("data/assets/cards/Common Lightning.png")
# surface_transformed = pygame.transform.scale(surface, (184, 165))

rect = pygame.Rect(40, 297, 300, 120)

def blit_text(surface, text, rect:pygame.Rect, font_, default_size, color=pygame.Color('black')):
    words = text.split(' ')  # 2D array where each row is a list of words.
    max_width, max_height = rect.size
    run = True
    lines = [""]
    size = default_size+1
    while run:
        size -= 1
        font1 = pygame.font.SysFont(font_, size)
        space = font1.size(' ')[0]  # The width of a space.
        lines = [""]
        index = 0
        x, y = (0, 0)
        for word in words:
            word_surface = font1.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width + space >= max_width:
                x = rect.topleft[0]  # Reset the x.
                y += word_height  # Start on new row.
                index += 1
                lines.append("")
            lines[index] += word + " "
            x += word_width + space
        if y <= rect.height:
            run = False
    x, y = rect.topleft
    for line in lines:
        text = font1.render(line, 0, color)
        surface.blit(text, (rect.left, y))
        y += text.get_size()[1]
    return text


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    screen.blit(surface, (0, 0))
    screen.blit(cost, (64, 58))
    blit_text(surface, name, pygame.Rect(115, 59, 200, 40), "Minecraft", 40)
    blit_text(surface, description, rect, "Minecraft", 26)
    pygame.display.update()
pygame.quit()
sys.exit()
