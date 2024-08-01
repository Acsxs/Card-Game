import pygame


class CardUIComponent:
    def __init__(self, size, card, cost, name, description):
        self.surface = pygame.Surface(size)
        self.rect = self.surface.get_rect()
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
        self.blit_text(str(self.cost), pygame.Rect(64,58,40,40), "Minecraft",40)

        # Name Rendering
        self.blit_text(self.name, pygame.Rect(115, 59, 200, 40), "Minecraft", 40)

        # Description Rendering
        self.blit_text(self.description, pygame.Rect(40, 297, 300, 120), "Minecraft", 40)
        self.surface = pygame.transform.scale(self.card, self.size)

    def draw(self, surface, pos=None):
        surface.blit(self.surface, pos if pos is not None else self.rect)

    def get_surface_at_scale(self, size):
        return pygame.transform.scale(self.card, size)


    def blit_text(self, text, rect: pygame.Rect, font_name, default_size, color=pygame.Color('black')):
        words = text.split(' ')
        words = [word + ' ' for word in words]
        max_width, max_height = rect.size
        size = default_size + 1
        for font_size in reversed(range(size)):
            lines = [""]
            font = pygame.font.SysFont(font_name, font_size)
            word_surfaces = [font.render(word, 0, color) for word in words]
            word_height = word_surfaces[0].get_size()[1]
            word_widths = [word_surface.get_size()[0] for word_surface in word_surfaces]
            previous=0
            i=sum_binary_search(word_widths, max_width)
            while i is not None:
                lines.append(''.join(words[previous:i]))
                previous = i
                i = sum_binary_search(word_widths, max_width)
            lines.append(''.join(words[previous:]))
            total_height = word_height*len(lines)
            if total_height <= max_height:
                break
        x, y = rect.topleft
        for line in lines:
            text = font.render(line, 0, color)
            self.card.blit(text, (rect.left, y))
            y += word_height
        return text


def sum_binary_search(array, x):
    range_ = [0, len(array)-1]
    result = 0
    while range_[0] <= range_[1]:
        mid = sum(range_) // 2
        if sum(array[:mid]) <= x:
            if sum(array[:mid + 1]) > x:
                return mid
            range_[0] = mid + 1
            continue
        range_[1] = mid - 1
    return