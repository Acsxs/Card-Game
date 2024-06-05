from src.UI.UI_component import UIComponent
import pygame


class CardUIComponent(UIComponent):
    def __init__(self, size, card, cost, name, description):
        UIComponent.__init__(self, size)
        # card.blit()
        self.base_card = card
        self.cost = cost
        self.size = size
        self.name = name
        self.description = description

        self.card = card
        self.update_card()

    def update_card(self):
        # Cost Rendering
        font = pygame.font.SysFont('Minecraft', 40)
        cost_surface = font.render(str(self.cost), 0, (0, 0, 0))
        self.card.blit(cost_surface, (64, 58))

        # Name Rendering
        self.blit_text(self.name, pygame.Rect(115, 59, 200, 40), "Minecraft", 40)

        # Description Rendering
        self.blit_text(self.description, pygame.Rect(40, 297, 300, 120), "Minecraft", 40)

        self.surface = pygame.transform.scale(self.card, self.size)

    def blit_text(self, text, rect: pygame.Rect, font_, default_size, color=pygame.Color('black')):
        words = text.split(' ')  # 2D array where each row is a list of words.
        max_width, max_height = rect.size
        run = True
        lines = [""]
        size = default_size + 1
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
            self.card.blit(text, (rect.left, y))
            y += text.get_size()[1]
        return text
