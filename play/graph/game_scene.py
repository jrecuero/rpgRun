import pygame
from base_scene import BaseScene
from game import Game
from blayer import LType
from brender import BRender
from assets.graph.surfaces import GreenSurface
from assets.graph.bobjects import Pillar
from assets.graph.actors import PlayerActor, EnemyActor


class GameScene(BaseScene):

    def __init__(self):
        super(GameScene, self).__init__()
        self.board_width = 8
        self.board_height = 8
        self._game = Game(self.board_width, self.board_height)
        iheight = self.board_height
        self.sprites = pygame.sprite.Group()
        for row in self._game.board:
            iheight -= 1
            for iwidth in range(self.board_width):
                row.add_cell_to_layer(GreenSurface(iwidth, iheight), LType.SURFACE)
                # self.sprites.add(spr)
        pillar = Pillar(0, 6)
        self._game.board.get_row_from_cell(pillar).add_cell_to_layer(pillar, LType.OBJECT)
        player = PlayerActor(2, 5)
        self._game.add_actor(player, True)
        self._game.board.get_row_from_cell(player).add_cell_to_layer(player, LType.OBJECT)
        enemies = []
        enemies.append(EnemyActor(4, 6, 'GOBLIN'))
        enemies.append(EnemyActor(3, 5, 'ORC'))
        enemies.append(EnemyActor(1, 0, 'TROLL'))
        for x in enemies:
            self._game.add_actor(x)
            self._game.board.get_row_from_cell(x).add_cell_to_layer(x, LType.OBJECT)

    def process_input(self, events):
        pass

    def update(self):
        self.sprites.update()

    def render(self, screen):
        screen.fill((0, 0, 255))
        x, y = 32, 32
        render_board = self._game.board.render(render=BRender.GRAPH)
        for row in render_board:
            for key, sprite in row.items():
                # sprite.rect.x = x
                # sprite.rect.y = y
                screen.blit(sprite.image, (x, y))
                x += 34
            x = 32
            y += 34
