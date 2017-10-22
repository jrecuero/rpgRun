import pygame


class CustomSprite(pygame.sprite.Sprite):

    def __init__(self, game, pos, **kwargs):
        super(CustomSprite, self).__init__()
        self.game = game
        self.pos = pos

        self.font_name = kwargs.get('font_name', 'arial')
        self.font_size = kwargs.get('font_size', 20)
        self.font_fg_color = kwargs.get('font_fg_color', (255, 255, 0))
        self.font_bg_color = kwargs.get('font_bg_color', (75, 75, 255))
        self.sprite_size = kwargs.get('sprite_size', (200, 100))
        self.sprite_color = kwargs.get('sprite_color', (125, 255, 125))

        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.surface = pygame.Surface(self.sprite_size)
        self.surface.fill(self.sprite_color)
        self.image = self.surface
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.in_focus = True

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
