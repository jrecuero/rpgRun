import pygame
from custom_sprite import CustomSprite


class PopUpMenu(CustomSprite):

    def __init__(self, game, pos, items, **kwargs):
        super(PopUpMenu, self).__init__(game, pos, **kwargs)
        self.items = items

        self.menu_items = []
        self.menu_x, self.menu_y = 10, 10
        self.menu_inc = self.font_size * 3 / 2

        y = self.menu_y
        for item in items:
            entry = self.font.render(
                item, 0, self.font_fg_color, self.font_bg_color)
            self.menu_items.append(entry)
            self.surface.blit(entry, (self.menu_x, y))
            y += self.menu_inc

    def update(self):
        # FIXME: This has to be moved to process_input method.
        if self.in_focus:
            mouse_pos = pygame.mouse.get_pos()
            boxes = []
            y = self.rect.y + self.menu_y
            for item in self.menu_items:
                boxes.append(item.get_rect().move(
                    self.rect.x + self.menu_x, y))
                y += self.menu_inc

            left, middle, right = pygame.mouse.get_pressed()
            if left:
                for index, box in enumerate(boxes):
                    if box.collidepoint(mouse_pos):
                        self.in_focus = False
                        return index
        return None
