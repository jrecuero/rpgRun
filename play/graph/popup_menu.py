import pygame


class PopUpMenu(pygame.sprite.Sprite):

    def __init__(self, game, pos, items, **kwargs):
        super(PopUpMenu, self).__init__()
        self.game = game
        self.pos = pos
        self.items = items

        font_name = kwargs.get('font_name', 'arial')
        font_size = kwargs.get('font_size', 20)
        font_fg_color = kwargs.get('font_fg_color', (255, 0, 0))
        font_bg_color = kwargs.get('font_bg_color', (0, 0, 255))
        menu_rect = kwargs.get('menu_rect', (200, 100))
        menu_color = kwargs.get('menu_color', (0, 255, 0))

        self.font = pygame.font.SysFont(font_name, font_size)
        self.surface = pygame.Surface(menu_rect)
        self.surface.fill(menu_color)

        self.menu_items = []
        self.menu_x, self.menu_y = 10, 10
        self.menu_inc = font_size * 3 / 2

        y = self.menu_y
        for item in items:
            entry = self.font.render(item, 0, font_fg_color, font_bg_color)
            self.menu_items.append(entry)
            self.surface.blit(entry, (self.menu_x, y))
            y += self.menu_inc
        self.image = self.surface
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.in_focus = True

    def update(self):
        if self.in_focus:
            mouse_pos = pygame.mouse.get_pos()
            boxes = []
            y = self.rect.y + self.menu_y
            for item in self.menu_items:
                boxes.append(item.get_rect().move(self.rect.x + self.menu_x, y))
                y += self.menu_inc

            left, middle, right = pygame.mouse.get_pressed()
            if left:
                for index, box in enumerate(boxes):
                    if box.collidepoint(mouse_pos):
                        self.in_focus = False
                        return index
        return None
