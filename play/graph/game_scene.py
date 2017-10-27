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
        self.resources = {}
        self.resources['menu'] = self._create_res()
        command_display = ConsoleDisplay(
            self.game, (10, 600), sprite_size=(780, 275), font_size=12)
        self.resources['command'] = self._create_res(command_display)
        pane_display = ConsoleDisplay(
            self.game, (600, 10), sprite_size=(190, 700), font_size=12)
        self.resources['pane'] = self._create_res(pane_display)
        self._get_res('pane').add_text('Player Information')

    def _create_res(self, instance=None, update_resource=None):
        resource = {'instance': instance, 'update': update_resource}
        return resource

    def _get_res(self, name):
        return self.resources[name]['instance']

    def _get_res_update(self, name):
        return self.resources[name]['update']

    def _traverse_res(self):
        for resource in [x for _, x in self.resources.items() if x['instance']]:
            yield (resource['instance'], resource['update'])

    def create_game(self):
        self.board_width, self.board_height = 8, 8
        self.width, self.height = 64, 64
        self.game = Game(self.board_width, self.board_height)
        iheight = self.board_height

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
                        menu = PopUpMenu(self.game, menu_pos, self.actions)
                        self.resources['menu'] = self._create_res(
                            menu, self._update_menu)
                    elif event.button == 3:
                        self.resources['menu'] = self._create_res()
                        self.left_disable = False
                        self.game.player.sprite.graph.image.fill((255, 165, 0))

    def _update_menu(self, action_index):
        if action_index is not None:
            # TODO: When action or movement are selected, they have to be
            # sent to the game to be prcessed.
            action_name = self.actions[action_index]
            self._get_res('command').add_text('Action {}'.format(action_name))
            action = self.game.player.get_action_by_name(action_name)
            action.originator = self.game.player
            action_type = self.game.run_select_action(action)
            if action_type == AType.WEAPONIZE:
                self._get_res('command').add_text('Action is {}'.format(AType.WEAPONIZE))
                self._get_res('command').add_text('Targets: {}'.format(self.game.target_choice))
                for target in self.game.target_choice:
                    target.selected = True
                    # target_sprite = target.sprite.get(BRender.GRAPH)
                    # target_sprite.image.fill((255, 255, 255))
            self.resources['menu'] = self._create_res()
            self.left_disable = False
            self.game.player.sprite.graph.image.fill((255, 165, 0))
            # self.selected = True

    def update(self):
        if self.selected:
            return

        for res_instance, res_update in self._traverse_res():
            result = res_instance.update()
            if res_update:
                res_update(result)

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
        for res_instance, _ in self._traverse_res():
            res_instance.render(screen)
