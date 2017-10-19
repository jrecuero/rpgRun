import pygame
from base_scene import BaseScene
from rpgrun.game import Game
from rpgrun.blayer import LType
from rpgrun.brender import BRender
from assets.graph.surfaces import GreenSurface
from assets.graph.bobjects import Pillar
from assets.graph.actors import PlayerActor, EnemyActor


class PopUpMenu(pygame.sprite.Sprite):

    def __init__(self, pos, items):
        super(PopUpMenu, self).__init__()
        self.pos = pos
        self.items = items
        self.font = pygame.font.SysFont('arial', 20)
        self.surface = pygame.Surface((200, 100))
        self.surface.fill((0, 255, 0))
        self.menu_items = []
        self.menu_item_x, self.menu_item_y = 10, 10
        self.menu_item_y_inc = 25
        y = self.menu_item_y
        for item in items:
            entry = self.font.render(item, 0, (255, 0, 0), (0, 0, 255))
            self.menu_items.append(entry)
            self.surface.blit(entry, (self.menu_item_x, y))
            y += self.menu_item_y_inc
        self.image = self.surface
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.in_focus = True

    def update(self):
        if self.in_focus:
            mouse_pos = pygame.mouse.get_pos()
            boxes = []
            y = self.rect.y + self.menu_item_y
            for item in self.menu_items:
                boxes.append(item.get_rect().move(self.rect.x + self.menu_item_x, y))
                y += self.menu_item_y_inc
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                for index, box in enumerate(boxes):
                    print('Click on Item: {0} {1}'.format(box, mouse_pos))
                    if box.collidepoint(mouse_pos):
                        print('Selection: {0}'.format(self.items[index]))
                        self.in_focus = False
                        return False
        return True


class MenuItem(pygame.sprite.Sprite):
    """MenuItem class provides a graphical menu to the program.

    TODO: This has to be created as a Generic Class to be used as a menu.
    """

    def __init__(self, pos):
        super(MenuItem, self).__init__()
        self.font = pygame.font.SysFont("arial", 20)
        # FIXME: Menu pane size is fixed at this time.
        self.surface = pygame.Surface((200, 100))
        self.surface.fill((0, 250, 0))
        self.action_item = self.font.render('Action     ', 0, (255, 0, 0), (0, 0, 255))
        self.move_item = self.font.render('Move       ', 0, (255, 0, 0), (0, 0, 255))
        self.surface.blit(self.action_item, (10, 10))
        self.surface.blit(self.move_item, (10, 35))
        self.image = self.surface
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def update(self):
        # self.sprites.update()
        mouse_pos = pygame.mouse.get_pos()
        # action_box = self.action_item.get_rect().move(self.rect.x + 10, self.rect.y + 10)
        # move_box = self.action_item.get_rect().move(self.rect.x + 10, self.rect.y + 35)
        action_box = self.action_item.get_rect().move(self.rect.x + 10, self.rect.y + 10)
        move_box = self.action_item.get_rect().move(self.rect.x + 10, self.rect.y + 35)
        left, middle, right = pygame.mouse.get_pressed()
        if left:
            print('self.rect: {}'.format(self.rect))
            if action_box.collidepoint(mouse_pos):
                print('Click on Action Item: {0} {1}'.format(action_box, mouse_pos))
                self.surface.fill((0, 250, 0))
                self.action_item = self.font.render('Action <---', 0, (255, 0, 0), (0, 0, 255))
                self.move_item = self.font.render('Move       ', 0, (255, 0, 0), (0, 0, 255))
                self.surface.blit(self.action_item, (10, 10))
                self.surface.blit(self.move_item, (10, 35))
                self.image = self.surface
            elif move_box.collidepoint(mouse_pos):
                print('Click on Move Item: {0} {1}'.format(move_box, mouse_pos))
                self.surface.fill((0, 250, 0))
                self.action_item = self.font.render('Action     ', 0, (255, 0, 0), (0, 0, 255))
                self.move_item = self.font.render('Move <-----', 0, (255, 0, 0), (0, 0, 255))
                self.surface.blit(self.action_item, (10, 10))
                self.surface.blit(self.move_item, (10, 35))
                self.image = self.surface


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
        self.left_disable = False
        self.selected = False

    def process_input(self, events):
        # FIXME If there is a menu active in the display it has to receive
        # control from the parent with remaining events.
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                player_rect = self._game.player.sprite.graph.rect
                if player_rect.collidepoint(mouse_pos):
                    if event.button == 1:
                        self.left_disable = True
                        self.menu_pos = (player_rect.left, player_rect.bottom)
                        self.menu_img = PopUpMenu(self.menu_pos, ['Action', 'Movement'])
                    elif event.button == 3:
                        self.menu_img = None
                        self.menu_pos = None
                        self.left_disable = False
                        self._game.player.sprite.graph.image.fill((255, 165, 0))

    def update(self):
        if self.selected:
            return

        if self.menu_img:
            if not self.menu_img.update():
                # TODO: When action or movement are selected, they have to be
                # sent to the game to be prcessed.
                self.menu_img = None
                self.menu_pos = None
                self.left_disable = False
                self._game.player.sprite.graph.image.fill((255, 165, 0))
                # self.selected = True

        # mouse_pos = pygame.mouse.get_pos()
        # player_rect = self._game.player.sprite.graph.rect
        # left, middle, right = pygame.mouse.get_pressed()
        # if not self.left_disable and left:
        #     if player_rect.collidepoint(mouse_pos):
        #         self.left_disable = True
        #         # self.menu_pos = mouse_pos
        #         self.menu_pos = (player_rect.left, player_rect.bottom)
        #         # self.menu_img = MenuItem(self.menu_pos)
        #         self.menu_img = PopUpMenu(self.menu_pos, ['Action', 'Movement'])
        #         # self._game.player.sprite.graph.image.fill((0, 0, 205))
        # elif right:
        #     if player_rect.collidepoint(mouse_pos):
        #         self.menu_img = None
        #         self.menu_pos = None
        #         self.left_disable = False
        #         self._game.player.sprite.graph.image.fill((255, 165, 0))

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
            screen.blit(self.menu_img.image, (self.menu_pos[0], self.menu_pos[1]))
