from rpgrun.bsprite import GraphSprite
from rpgrun.bobject import BObject
import pygame


class PillarSprite(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super(PillarSprite, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()


class Pillar(BObject):

    def __init__(self, x, y, width, height, **kwargs):
        super(Pillar, self).__init__(x, y, 'PILLAR', **kwargs)
        self.sprite = GraphSprite(sprite=PillarSprite(width, height))
