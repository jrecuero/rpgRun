# import pygame
from custom_sprite import CustomSprite


class PaneDisplay(CustomSprite):

    def __init__(self, game, pos, **kwargs):
        super(PaneDisplay, self).__init__(game, pos, **kwargs)
