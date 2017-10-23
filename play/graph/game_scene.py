import pygame
from rpgrun.game import Game
from rpgrun.shapes import Quad, Rhomboid
from rpgrun.blayer import LType
from rpgrun.brender import BRender
from assets.graph.surfaces import GreenSurface
from assets.graph.bobjects import Pillar
from assets.graph.actors import PlayerActor, EnemyActor
from assets.graph.actions import WeaponAction, MoveAction, MeleAction, RangeAction
from assets.graph.equips import Weapon, Armor, Shield
from rpgrun.action import AType
from base_scene import BaseScene
from popup_menu import PopUpMenu
from console_display import ConsoleDisplay


class GameScene(BaseScene):
    def __init__(self):
        super(GameScene, self).__init__()
        self.create_game()
        self.command_display = ConsoleDisplay(self.game,
                                              (10, 600),
                                              sprite_size=(780, 275),
                                              font_size=12)

    def create_game(self):
        self.board_width, self.board_height = 8, 8
        self.width, self.height = 64, 64
        self.game = Game(self.board_width, self.board_height)
        iheight = self.board_height
        # self.sprites = pygame.sprite.Group()

        # Create all objects in the game here (cells, actors, ...)
        for row in self.game.board:
            iheight -= 1
            for iwidth in range(self.board_width):
                row.add_cell_to_layer(GreenSurface(
                    iwidth, iheight, self.width, self.height), LType.SURFACE)
        pillar = Pillar(0, 6, self.width, self.height)
        self.game.board.get_row_from_cell(
            pillar).add_cell_to_layer(pillar, LType.OBJECT)

        player = PlayerActor(2, 5, self.width, self.height)
        player.actions.append(WeaponAction('weapon', AType.WEAPONIZE))
        player.actions.append(MoveAction('move', AType.MOVEMENT))
        self.game.add_actor(player, True)
        self.game.board.get_row_from_cell(
            player).add_cell_to_layer(player, LType.OBJECT)

        sword = Weapon(name='sword', attr_buff={'str': 5})
        sword.actions.append(MeleAction(
            'mele', AType.WEAPONIZE, width=2, height=2, shape=Quad))
        bow = Weapon(name='bow', attr_buff={'str': 2})
        bow.actions.append(RangeAction(
            'range', AType.WEAPONIZE, width=3, height=3, shape=Rhomboid))
        armor = Armor(attr_buff={'hp': 10})
        shield = Shield(attr_buff={'hp': 7, 'str': 1})
        player.inventory.append(sword)
        player.inventory.append(bow)
        player.inventory.append(armor)
        player.inventory.append(shield)
        player.equipment.append(sword)
        player.equipment.append(armor)
        player.equipment.append(sword)

        enemies = []
        enemies.append(EnemyActor(4, 6, self.width, self.height, 'GOBLIN'))
        enemies.append(EnemyActor(3, 5, self.width, self.height, 'ORC'))
        enemies.append(EnemyActor(1, 0, self.width, self.height, 'TROLL'))
        for x in enemies:
            self.game.add_actor(x)
            self.game.board.get_row_from_cell(
                x).add_cell_to_layer(x, LType.OBJECT)

        self.game.run_init()
        self.menu_img = None
        self.left_disable = False
        self.selected = False

    def process_input(self, events):
        # FIXME If there is a menu active in the display it has to receive
        # control from the parent with remaining events.
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                player_rect = self.game.player.sprite.graph.rect
                if player_rect.collidepoint(mouse_pos):
                    if event.button == 1:
                        self.actions = [
                            x.name for x in self.game.player.all_actions]
                        self.left_disable = True
                        menu_pos = (player_rect.left, player_rect.bottom)
                        self.menu_img = PopUpMenu(
                            self.game, menu_pos, self.actions)
                    elif event.button == 3:
                        self.menu_img = None
                        self.left_disable = False
                        self.game.player.sprite.graph.image.fill((255, 165, 0))

    def update(self):
        if self.selected:
            return

        if self.menu_img:
            action = self.menu_img.update()
            if action is not None:
                # TODO: When action or movement are selected, they have to be
                # sent to the game to be prcessed.
                self.command_display.add_text(
                    'Player will {}'.format(self.actions[action]))
                self.menu_img = None
                self.left_disable = False
                self.game.player.sprite.graph.image.fill((255, 165, 0))
                # self.selected = True

        if self.command_display:
            self.command_display.update()

    def render(self, screen):
        screen.fill((0, 0, 255))
        x, y = 32, 32
        render_board = self.game.board.render(render=BRender.GRAPH)
        for row in render_board:
            for key, sprite in row.items():
                sprite.rect.x = x
                sprite.rect.y = y
                screen.blit(sprite.image, (x, y))
                x += self.width + 2
            x = 32
            y += self.height + 2
        # TODO: We have to create a display for logging information related with
        # the game for debugging purposes. That panel will be used in the
        # future to display information relevant to the player.
        if self.menu_img:
            self.menu_img.render(screen)
        if self.command_display:
            self.command_display.render(screen)
