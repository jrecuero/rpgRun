from bsprite import BSprite
from bsurface import BSurface
import pygame


class GreenSurface(BSurface):

    def __init__(self, x, y, width, **kwargs):
        super(GreenSurface, self).__init__(x, y, '*', **kwargs)
        self.sprite = BSprite(spr_text=' ', color='\x1b[42m', width=width)


class GreenSprite(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super(GreenSprite, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()


class GraphGreenSurface(BSurface):

    def __init__(self, x, y, **kwargs):
        super(GraphGreenSurface, self).__init__(x, y, 'GREEN', **kwargs)
        self.sprite = BSprite(spr_graph=GreenSprite(32, 32))
