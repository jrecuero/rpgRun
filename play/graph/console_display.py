# import pygame
from custom_sprite import CustomSprite


class ConsoleDisplay(CustomSprite):

    def __init__(self, game, pos, **kwargs):
        super(ConsoleDisplay, self).__init__(game, pos, **kwargs)
        self.text = []
        self.add_text('Command Line Display')

    def add_text(self, message):
        self.text.append(message)

    def update(self):
        if self.in_focus:
            x, y = 10, 10
            for text in self.text:
                entry = self.font.render(
                    text, 0, self.font_fg_color, self.font_bg_color)
                self.surface.blit(entry, (x, y))
                y += self.font_size
