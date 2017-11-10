# import pygame
from panes.custom_pane import CustomPane


class ConsolePane(CustomPane):

    def __init__(self, game, pos, **kwargs):
        super(ConsolePane, self).__init__(game, pos, **kwargs)
        self.text = []
        self.add_text('Command Line Display')
        self.text_box_len = kwargs.get("text_box_len", 16)

    def add_text(self, message):
        self.text.append(message)

    def update(self):
        # TODO: Do we have to clear the pane every time before adding all text
        # or it is not required?
        if self.in_focus:
            x, y = 10, 10
            for text in self.text[-self.text_box_len:]:
                entry = self.font.render(
                    text, 0, self.font_fg_color, self.font_bg_color)
                self.surface.blit(entry, (x, y))
                y += self.font_size
