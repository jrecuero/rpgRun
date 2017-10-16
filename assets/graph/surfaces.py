from bsprite import BSprite
from bsurface import BSurface
import pygame


class GreenSprite(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super(GreenSprite, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()


class GreenSurface(BSurface):

    def __init__(self, x, y, **kwargs):
        super(GreenSurface, self).__init__(x, y, 'GREEN', **kwargs)
        self.sprite = BSprite(spr_graph=GreenSprite(32, 32))
