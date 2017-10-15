import pygame
from base_scene import BaseScene
from game import Game
from blayer import LType
from bcell import BCell, BSprite
from assets.surfaces import GreenSprite


class GameScene(BaseScene):

    def __init__(self):
        super(GameScene, self).__init__()
        self._width = 8
        self._height = 8
        self._game = Game(self._width, self._height)
        iheight = self._height
        self.sprites = pygame.sprite.Group()
        for row in self._game.board:
            iheight -= 1
            for iwidth in range(self._width):
                spr = GreenSprite(self._width, self._height)
                bspr = BSprite(spr_graph=spr)
                row.add_cell_to_layer(BCell(iwidth, iheight, 'None', sprite=bspr), LType.SURFACE)
                self.sprites.add(spr)

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        self.sprites.update()

    def render(self, screen):
        screen.fill((0, 0, 255))
