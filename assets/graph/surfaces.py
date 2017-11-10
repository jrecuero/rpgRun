from rpgrun.board.bsprite import GraphSprite
from rpgrun.board.bsurface import BSurface
from assets.graph.gsprite import GameSprite
import pygame


class GreenSprite(GameSprite):

    def __init__(self, width, height):
        super(GreenSprite, self).__init__()
        image = pygame.Surface((width, height))
        image.fill((255, 255, 0))
        image_selected = pygame.Surface((width, height))
        image_selected.fill((245, 245, 245))
        self.set_image(image, image_selected)
        self.rect = self.image.get_rect()


class GreenSurface(BSurface):

    def __init__(self, x, y, width, height, **kwargs):
        super(GreenSurface, self).__init__(x, y, 'GREEN', **kwargs)
        self.sprite = GraphSprite(sprite=GreenSprite(width, height))
