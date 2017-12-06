import pygame
from rpgrun.game.game import Game
from rpgrun.board.bpoint import Location
from rpgrun.board.bshapes import Quad, Rhomboid
from rpgrun.board.blayer import LType
from rpgrun.board.brow import BRow
from rpgrun.board.brender import BRender
from assets.graph.surfaces import GreenSurface
from assets.graph.bobjects import Pillar
from assets.graph.actors import PlayerActor, EnemyActor
from assets.graph.actions import WeaponAction, MoveAction, MeleAction, RangeAction
from assets.graph.equips import Weapon, Armor, Shield
from rpgrun.game.action import AType
from rpgrun.game.actor import Actor
from scenes.base_scene import BaseScene
from panes.menu_pane import MenuPane
from panes.console_pane import ConsolePane
# from panes.stat_pane import StatPane
# from panes.action_pane import ActionPane


class GameScene(BaseScene):
    def __init__(self):
        """GameScene class initialization method.
        """
        super(GameScene, self).__init__()
        # "_out_buffer" buffer is used to redirect the logger output to the
        # console pane.
        self._out_buffer = []
        # There are several attributes created in create_game() method.
        self._create_game()
        self.resources = {}
        self.resources['menu'] = self._new_resource()
        command_pane = ConsolePane(self.game, (32, 600), pane_size=(528, 275), font_size=12, title='Console')
        self.resources['command'] = self._new_resource(command_pane)
        stat_pane = ConsolePane(self.game, (580, 32), pane_size=(590, 526), font_size=12, title='Player Stats')
        self.resources['stat'] = self._new_resource(stat_pane)
        # action_pane = ConsolePane(self.game, (580, 600), pane_size=(590, 275), font_size=12, title='Player Actions')
        # self.resources['action'] = self._new_resource(action_pane)
        self.actions = [x.name for x in self.game.player.all_actions]
        action_pane = MenuPane(self.game,
                               (580, 600),
                               self.actions,
                               pane_size=(590, 275),
                               post_update_cb=self._post_update_menu)
        # self.resources['action'] = self._new_resource(action_pane, self._post_update_menu, True)
        self.resources['action'] = self._new_resource(action_pane, None, True)

    def _create_environment(self):
        """
        """
        iheight = self.board_height
        for row in self.game.board:
            iheight -= 1
            for iwidth in range(self.board_width):
                row.add_cell_to_layer(GreenSurface(iwidth, iheight, self.width, self.height), LType.SURFACE)
        pillar = Pillar(0, 6, self.width, self.height)
        self.game.board.get_row_from_cell(pillar).add_cell_to_layer(pillar, LType.OBJECT)

    def _create_player(self):
        """
        """
        player = PlayerActor(2, 5, self.width, self.height)
        player.actions.append(WeaponAction('weapon', AType.WEAPONIZE))
        player.actions.append(MoveAction('move', AType.MOVEMENT, width=2, height=2, shape=Rhomboid))
        self.game.add_actor(player, True)
        self.game.board.get_row_from_cell(player).add_cell_to_layer(player, LType.OBJECT)

        sword = Weapon(name='sword', attr_buff={'str': 5})
        sword.actions.append(MeleAction('mele', AType.WEAPONIZE, width=2, height=2, shape=Quad))
        bow = Weapon(name='bow', attr_buff={'str': 2})
        bow.actions.append(RangeAction('range', AType.WEAPONIZE, width=3, height=3, shape=Rhomboid))
        armor = Armor(attr_buff={'hp': 10})
        shield = Shield(attr_buff={'hp': 7, 'str': 1})
        player.inventory.append(sword)
        player.inventory.append(bow)
        player.inventory.append(armor)
        player.inventory.append(shield)
        player.equipment.append(sword)
        player.equipment.append(armor)
        player.equipment.append(sword)

    def _create_enemies(self):
        """
        """
        enemies = []
        enemies.append(EnemyActor(4, 6, self.width, self.height, 'GOBLIN'))
        enemies.append(EnemyActor(3, 5, self.width, self.height, 'ORC'))
        enemies.append(EnemyActor(1, 0, self.width, self.height, 'TROLL'))
        for x in enemies:
            self.game.add_actor(x)
            self.game.board.get_row_from_cell(x).add_cell_to_layer(x, LType.OBJECT)

    def _create_game(self):
        """Create game instances. It creates and initializes some instance attributes.
        """
        # number of rows and columns for the board.
        self.board_width, self.board_height = 8, 8
        # sprite size (in pixels) for every cell in the board.
        self.width, self.height = 64, 64
        self.game = Game(self.board_width,
                         self.board_height,
                         capture=self._out_buffer)

        # Create all objects in the game here (cells, actors, ...)
        self._create_environment()

        Actor.LIFE = 'hp'
        self._create_player()
        self._create_enemies()

        self.game.run_init()
        self.left_disable = False

    def _new_row(self):
        """Scroll Board.
        """
        width = self.game.board.width
        row = BRow(width)
        newHeight = self.game.board.top_cell_row + 1
        for iwidth in range(width):
            row.add_cell_to_layer(GreenSurface(iwidth, newHeight, self.width, self.height), LType.SURFACE)
        return row

    def _new_resource(self, instance=None, post_update_cb=None, on_click=False):
        """
        """
        resource = {'instance': instance, 'pos-update': post_update_cb, 'onclick': on_click}
        return resource

    def _get_resource(self, name):
        """
        """
        return self.resources[name]['instance']

    def _get_resource_post_update(self, name):
        """
        """
        return self.resources[name]['pos-update']

    def _traverse_resource(self):
        """
        """
        for resource in [x for _, x in self.resources.items() if x['instance']]:
            yield (resource['instance'], resource['pos-update'], resource['onclick'])

    def _traverse_resource_on_click(self):
        """
        """
        for resource in [x for _, x in self.resources.items() if x['instance'] and x['onclick']]:
            yield (resource['instance'], resource['pos-update'], resource['onclick'])

    def _click_on_pane(self, pane, event, mouse_pos):
        """ TODO: Locate menu items in the pane in order to be selected.
        """
        pane_rect = pane.rect
        if event.button == 1 and pane_rect.collidepoint(mouse_pos):
            self._get_resource('command').add_text('Click on {}'.format("pane"))
            return True
        return False

    def _click_on_actor(self, actor, event, mouse_pos):
        """
        """
        actor_rect = actor.sprite.sprite.rect
        if event.button == 1 and actor_rect.collidepoint(mouse_pos):
            self._get_resource('command').add_text('Click on {}'.format(actor.name))
            self.game.run_select_target(actor)
            return True
        return False

    def _process_input_click_on_player(self, event, mouse_pos):
        """
        """
        player_rect = self.game.player.sprite.sprite.rect
        if event.button == 1 and player_rect.collidepoint(mouse_pos):
            self.actions = [x.name for x in self.game.player.all_actions]
            self.left_disable = True
            menu_pos = (player_rect.left, player_rect.bottom)
            menu = MenuPane(self.game, menu_pos, self.actions)
            self.resources['menu'] = self._new_resource(menu, self._post_update_menu)
            return True
        return False

    def _process_input_all_actors(self, event, mouse_pos):
        """
        """
        for actor in self.game.other_actors():
            if self._click_on_actor(actor, event, mouse_pos):
                for target in self.game.target_choice:
                    target.selected = (target == actor)
                return True
        return False

    def _process_input_move_choice(self, event, mouse_pos):
        """
        """
        if self.game.move_choice:
            clicked = False
            for point in self.game.move_choice:
                for cell in self.game.board.get_cells_at(point):
                    cell_rect = cell.sprite.sprite.rect
                    if event.button == 1 and cell_rect.collidepoint(mouse_pos):
                        self._get_resource('command').add_text('Click for move  at {}'.format(cell))
                        clicked = True
                        # FIXME: This is just a fixed location movement
                        self.game.run_select_movement(Location.FRONT, 1)
            if clicked:
                for point in self.game.move_choice:
                    for cell in self.game.board.get_cells_at(point):
                        cell.selected = False
                self.game.run_scroll(self._new_row())
                return True
        return False

    def _process_input_click_on_pane(self, event, mouse_pos):
        """
        """
        for resource_instance, _, on_click in self._traverse_resource_on_click():
            self._click_on_pane(resource_instance, event, mouse_pos)
            pass
        return False

    def process_input(self, events):
        """
        """
        for event in events:
            if event.type == (pygame.USEREVENT + 1):
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)
                self.left_disable = False

            if event.type == pygame.MOUSEBUTTONUP and not self.left_disable:
                mouse_pos = pygame.mouse.get_pos()
                if self._process_input_click_on_player(event, mouse_pos):
                    return

                if self._process_input_all_actors(event, mouse_pos):
                    return

                if self._process_input_move_choice(event, mouse_pos):
                    return

                if self._process_input_click_on_pane(event, mouse_pos):
                    return

    def _post_update_menu(self, action_index):
        """
        """
        if action_index is not None:
            action_name = self.actions[action_index]
            action = self.game.player.get_action_by_name(action_name)
            action.originator = self.game.player
            action_type = self.game.run_select_action(action)
            if action_type == AType.WEAPONIZE:
                self._get_resource('command').add_text('Action is {}'.format(AType.WEAPONIZE))
                for target in self.game.target_choice:
                    target.selected = True
            elif action_type == AType.MOVEMENT:
                self._get_resource('command').add_text('Action is {}'.format(AType.MOVEMENT))
                for point in self.game.move_choice:
                    for cell in self.game.board.get_cells_at(point):
                        cell.selected = True
            # self.resources['menu'] = self._new_resource()
            # pygame.time.set_timer(pygame.USEREVENT + 1, 500)
            self.game.player.sprite.sprite.image.fill((255, 165, 0))

    def update(self):
        """
        """
        if self._out_buffer:
            # for entry in self._out_buffer[-1].split('\n'):
            for entry in self._out_buffer:
                self._get_resource('command').add_text(entry)
            self._out_buffer.clear()

        for resource_instance, post_update_cb, _ in self._traverse_resource():
            result = resource_instance.update()
            # TODO: We shoudl move this post-update to the update callback per
            # se.
            if post_update_cb:
                post_update_cb(result)

    def render(self, screen):
        """
        """
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
        for resource_instance, _, _ in self._traverse_resource():
            resource_instance.render(screen)
