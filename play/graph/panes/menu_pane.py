import pygame
from panes.custom_pane import CustomPane


class MenuPane(CustomPane):

    def __init__(self, game, pos, items, **kwargs):
        super(MenuPane, self).__init__(game, pos, **kwargs)
        self.items = {}
        self.menu_items = []
        self.menu_x, self.menu_y = 10, 10
        self.menu_inc = self.font_size * 3 / 2

        y = self.menu_y
        for item in items:
            self.items.update({item: True})
            entry = self.font.render(item, 0, self.font_fg_color, self.font_bg_color)
            self.menu_items.append(entry)
            self.surface.blit(entry, (self.menu_x, y))
            y += self.menu_inc

    def _set_item(self, item, flag):
        if self.items.get(item, None) is not None:
            return False
        self.items[item] = flag
        return True

    def disable_item(self, item):
        return self._set_item(item, False)

    def enable_item(self, item):
        return self._set_item(item, True)

    def update(self):
        # FIXME: This has to be moved to process_input method.
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
                        # self.in_focus = False
                        return index
        return None
