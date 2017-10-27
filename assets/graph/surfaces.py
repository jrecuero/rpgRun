from rpgrun.bsprite import BSprite
from rpgrun.bsurface import BSurface
from assets.graph.gsprite import GameSprite
import pygame


class GreenSprite(GameSprite):

    def __init__(self, width, height):
        super(GreenSprite, self).__init__()
        image = pygame.Surface((width, height))
        image.fill((255, 255, 0))
        self.image = image
        self.rect = self.image.get_rect()


class GreenSurface(BSurface):

    def __init__(self, x, y, width, height, **kwargs):
        super(GreenSurface, self).__init__(x, y, 'GREEN', **kwargs)
        self.sprite = BSprite(spr_graph=GreenSprite(width, height))
