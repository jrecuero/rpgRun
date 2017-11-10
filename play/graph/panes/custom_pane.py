import pygame
from assets.graph.gsprite import GameSprite


class CustomPane(GameSprite):

    def __init__(self, game, pos, **kwargs):
        super(CustomPane, self).__init__()
        self.game = game
        self.pos = pos

        self.font_name = kwargs.get('font_name', 'arial')
        self.font_size = kwargs.get('font_size', 20)
        self.font_fg_color = kwargs.get('font_fg_color', (255, 255, 0))
        self.font_bg_color = kwargs.get('font_bg_color', (75, 75, 255))
        self.pane_size = kwargs.get('pane_size', (200, 100))
        self.pane_color = kwargs.get('pane_color', (125, 255, 125))

        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.surface = pygame.Surface(self.pane_size)
        self.surface.fill(self.pane_color)
        self.image = self.surface
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.in_focus = True

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))