import pygame
from base_scene import BaseScene
from game import Game
from blayer import LType
from brender import BRender
from assets.graph.surfaces import GreenSurface
from assets.graph.bobjects import Pillar
from assets.graph.actors import PlayerActor, EnemyActor


class MenuItem(pygame.sprite.Sprite):

    def __init__(self):
        super(MenuItem, self).__init__()
        font = pygame.font.Font(None, 19)
        surface = pygame.Surface((200, 100))
        rendered = font.render('Right Click', 0, (255, 0, 0))
        surface.blit(rendered, (10, 10))
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 100

    def update(self):
        # self.sprites.update()
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            right, middle, left = pygame.mouse.get_pressed()
            if right:
                print('Click on Menu Item: {0} {1}'.format(self.rect, mouse_pos))


class GameScene(BaseScene):

    def __init__(self):
        super(GameScene, self).__init__()
        self.create_game()

    def create_game(self):
        self.board_width, self.board_height = 8, 8
        self.width, self.height = 64, 64
        self._game = Game(self.board_width, self.board_height)
        iheight = self.board_height
        # self.sprites = pygame.sprite.Group()
        for row in self._game.board:
            iheight -= 1
            for iwidth in range(self.board_width):
                row.add_cell_to_layer(GreenSurface(iwidth, iheight, self.width, self.height), LType.SURFACE)
        pillar = Pillar(0, 6, self.width, self.height)
        self._game.board.get_row_from_cell(pillar).add_cell_to_layer(pillar, LType.OBJECT)
        player = PlayerActor(2, 5, self.width, self.height)
        self._game.add_actor(player, True)
        self._game.board.get_row_from_cell(player).add_cell_to_layer(player, LType.OBJECT)
        enemies = []
        enemies.append(EnemyActor(4, 6, self.width, self.height, 'GOBLIN'))
        enemies.append(EnemyActor(3, 5, self.width, self.height, 'ORC'))
        enemies.append(EnemyActor(1, 0, self.width, self.height, 'TROLL'))
        for x in enemies:
            self._game.add_actor(x)
            self._game.board.get_row_from_cell(x).add_cell_to_layer(x, LType.OBJECT)
        self._game.run_init()
        self.menu_img = None

    def process_input(self, events):
        pass

    def update(self):
        # self.sprites.update()
        mouse_pos = pygame.mouse.get_pos()
        player_rect = self._game.player.sprite.graph.rect
        if self.menu_img:
            self.menu_img.update()
        if player_rect.collidepoint(mouse_pos):
            right, middle, left = pygame.mouse.get_pressed()
            if right:
                # self.menu_img = pygame.Surface((200, 200))
                # font = pygame.font.Font(None, 19)
                # rendered = font.render('Right Click', 0, (255, 0, 0))
                # self.menu_img.blit(rendered, (10, 10))
                self.menu_img = MenuItem()
                self._game.player.sprite.graph.image.fill((0, 0, 205))
            elif left:
                self.menu_img = None
                self._game.player.sprite.graph.image.fill((255, 165, 0))

    def render(self, screen):
        screen.fill((0, 0, 255))
        x, y = 32, 32
        render_board = self._game.board.render(render=BRender.GRAPH)
        for row in render_board:
            for key, sprite in row.items():
                sprite.rect.x = x
                sprite.rect.y = y
                screen.blit(sprite.image, (x, y))
                x += self.width + 2
            x = 32
            y += self.height + 2
        if self.menu_img:
            screen.blit(self.menu_img.image, (400, 100))
