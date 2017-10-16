from bsprite import BSprite
from bobject import BObject
import pygame


class Pillar(BObject):

    def __init__(self, x, y, width, **kwargs):
        super(Pillar, self).__init__(x, y, 'PILLAR', **kwargs)
        self.sprite = BSprite(spr_text='|||||||', width=width, color="\x1b[44m")


class PillarSprite(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super(PillarSprite, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()


class GraphPillar(BObject):

    def __init__(self, x, y, **kwargs):
        super(GraphPillar, self).__init__(x, y, 'PILLAR', **kwargs)
        self.sprite = BSprite(spr_graph=PillarSprite(32, 32))
