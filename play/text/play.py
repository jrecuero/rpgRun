from jc2cli.namespace import Handler
from jc2cli.decorators import command, argo
from jc2cli.builtin.argos import Int
import jc2cli.tools.loggerator as loggerator
import rpgrun.game.game as game
from rpgrun.board.blayer import LType
from rpgrun.board.bpoint import Point, Location
from rpgrun.board.bshapes import Quad, Rhomboid
from rpgrun.board.brow import BRow
from rpgrun.game.action import AType
from rpgrun.game.actor import Actor
from assets.text.surfaces import GreenSurface
from assets.text.actors import PlayerActor, EnemyActor, MageActor, BossActor
from assets.text.bobjects import Pillar
from assets.text.actions import WeaponAction, MeleAction, RangeAction, MoveAction
from assets.text.equips import Weapon, Armor, Shield
from targs import T_Target, T_Actor, T_Equip, T_Attr, T_Action, T_Location, T_Step

MODULE = 'Play'
EXPORT = 'Play'


data_cache = {}


class Play(object):

    SYSTEM = ['exit', 'help', 'syntax', 'debug', 'HIT']
    COMMON = ['PRINT', 'ACTORS', 'PLAYER',
              'EQUIPMENT', 'INVENTORY', 'EQUIP', 'UNEQUIP']
    STAGES = {'wait': ['INIT'],
              'init': ['RUN'] + COMMON,
              'run': ['ACTION'] + COMMON,
              'target': ['TARGET'] + COMMON,
              'move': ['MOVEMENT'] + COMMON, }

    def __init__(self):
        super(Play, self).__init__()
        self._game = None
        self._logger = loggerator.getLoggerator(MODULE)
        self._stage = 'wait'

    def precmd(self, cmd, line):
        if cmd in self.STAGES[self._stage] + self.SYSTEM:
            return True
        else:
            print('command <{0}> not valid in stage <{1}>'.format(
                cmd, self._stage))
            return False

    def _new_row(self):
        """Scroll Board.
        """
        width = self._game.board.width
        row = BRow(width)
        newHeight = self._game.board.top_cell_row + 1
        for iwidth in range(width):
            row.add_cell_to_layer(GreenSurface(
                iwidth, newHeight, self._spr_width), LType.SURFACE)
        return row

    def _scroll(self):
        """Scroll Board.
        """
        row = self._new_row()
        self._game.scroll_board(row)

    def set_toolbar(self):
        return " | ".join(self.STAGES[self._stage])

    def set_rprompt(self):
        return "<{0}>".format(self._stage)

    def run(self, **kwargs):
        super(Play, self).run(prompt='rpgRun> ',
                              toolbar=self.set_toolbar,
                              rprompt=self.set_rprompt,
                              precmd=True)


play = Play()


@command('INIT')
def do_init():
    """Initialize rpgRUN game.
    """
    play._width = 7
    play._height = 7
    play._spr_width = 7
    play._game = game.Game(play._width, play._height)
    data_cache['game'] = play._game
    iheight = play._height
    for row in play._game.board:
        iheight -= 1
        for iwidth in range(play._width):
            row.add_cell_to_layer(GreenSurface(
                iwidth, iheight, play._spr_width), LType.SURFACE)

    Actor.LIFE = 'hp'
    player = PlayerActor(2, 4, play._spr_width)
    player.actions.append(WeaponAction('weapon', AType.WEAPONIZE))
    player.actions.append(MoveAction('move', AType.MOVEMENT))
    enemies = []
    enemies.append(EnemyActor(4, 6, play._spr_width, 'GOBLIN'))
    enemies.append(EnemyActor(3, 5, play._spr_width, 'ORC'))
    enemies.append(EnemyActor(1, 0, play._spr_width, 'TROLL'))
    enemies.append(MageActor(0, 5, play._spr_width, 'MAGE'))
    enemies.append(BossActor(1, 5, play._spr_width))
    enemies[-1].Life = 'mp'
    pillar = Pillar(0, 6, play._spr_width)

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
    player.equipment.append(shield)

    play._game.add_actor(player, True)
    for x in enemies:
        play._game.add_actor(x)

    play._game.board.get_row_from_cell(
        player).add_cell_to_layer(player, LType.OBJECT)
    play._game.board.get_row_from_cell(
        pillar).add_cell_to_layer(pillar, LType.OBJECT)
    for x in enemies:
        play._game.board.get_row_from_cell(
            x).add_cell_to_layer(x, LType.OBJECT)

    play._logger.display('Init rpgRun')

    # Run the game engine.
    play._game.run_init()
    play._stage = 'init'
    return True


@command("MOVE loc pos")
@argo('loc', T_Location(), None)
@argo('pos', Int(), None)
def do_move_player(loc, pos):
    """Move player a number of positions to given location.
    """
    play._game.move_player(loc, pos)
    if loc == Location.FRONT:
        play._scroll()
    return True


@command("PLAYER [name]?")
@argo('name', T_Actor(data_cache), 'PLAYER')
def do_print_player(name):
    """Print player information.
    """
    actor = play._game.find_actor_by_name(name)
    play._logger.display("Data for  : {0}".format(name))
    play._logger.display("Name      : {0}".format(actor.name))
    play._logger.display("Position  : {0}".format(actor.get_point()))
    play._logger.display("Attributes:\n{0}".format(actor.attrs))
    return True


@command("INVENTORY name")
@argo('name', T_Actor(data_cache), None)
def do_print_inventory(name):
    """Prints player inventory.
    """
    actor = play._game.find_actor_by_name(name)
    play._logger.display("Inventory for  : {0}".format(name))
    for x in actor.inventory:
        play._logger.display(">> {0}".format(x))
    return True


@command("EQUIPMENT name")
@argo('name', T_Actor(data_cache), None)
def do_print_equipment(name):
    """Prints player equipment.
    """
    actor = play._game.find_actor_by_name(name)
    play._logger.display("Equipment for  : {0}".format(name))
    for x in actor.equipment:
        play._logger.display(">> {0}".format(x))
    return True


@command('ACTORS')
def do_print_actors():
    """Print actors attributes.
    """
    for actor in play._game.actors:
        play._logger.display("Data for  : {0}".format(actor.name))
        play._logger.display(
            "Position  : {0}".format(Point.__repr__(actor)))
        play._logger.display("Attributes:\n{0}".format(actor.attrs))
    return True


@command('PRINT')
def do_print_board():
    """Print rpgRUN game board.
    """
    play._logger.display(play._game.board.render(width=7))
    return True


@command('SCROLL')
def do_scroll_board():
    """Scroll Board.
    """
    play._scroll()
    return True


@command('RUN')
def do_run():
    """Run a cycle
    """
    print('select action (use command: ACTION <name>) ')
    for i, x in enumerate(play._game.player.all_actions):
        print('{0} : {1}'.format(i, x.name))
    play.prompt_str = '[ACTION <name>] rpgRun> '
    play._stage = 'run'
    return True


@command("ACTION name")
@argo('name', T_Action(data_cache), None)
def do_action(name):
    """Select action to run.
    """
    for action in play._game.player.actions:
        if action.name == name:
            break
    else:
        return True
    action.originator = play._game.player
    # play._game.run_init()
    action_type = play._game.run_select_action(action)
    if action_type == AType.WEAPONIZE:
        print('select target (use command: TARGET <name>)')
        for i, x in enumerate(play._game.target_choice):
            print('{0} : {1}'.format(i, x))
        play.prompt_str = '[TARGET <name>] rpgRun> '
        play._stage = 'target'
    elif action_type == AType.MOVEMENT:
        print('select player movement (use command: MOVEMENT <loc> <pos>)')
        play.prompt_str = '[MOVEMENT <loc> <pos>] rpgRun> '
        play._stage = 'move'
    return True


@command("TARGET name")
@argo('name', T_Target(data_cache), None)
def do_target(name):
    """Select target for the action to run.
    """
    for _target in play._game.target_choice:
        if _target.name == name:
            break
    else:
        return True
    play._game.run_select_target(_target)
    play.prompt_str = 'rpgRun> '
    play._stage = 'init'
    return True


@command("MOVEMENT loc pos")
@argo('loc', T_Location(), None)
@argo('pos', T_Step(), None)
def do_select_movement(loc, pos):
    """Select location and steps for the player to move.
    """
    print('player moves {0} to {1}'.format(pos, loc))
    play._game.run_select_movement(loc, pos)
    play._game.run_scroll(play._new_row())
    # play._scroll()
    play._stage = 'init'
    return True


@command("EQUIP aname equip")
@argo('aname', T_Actor(data_cache), None)
@argo('equip', T_Equip(data_cache), None)
def do_equip_actor(aname, equip):
    """Equip an item in an actor.
    """
    actor = play._game.find_actor_by_name(aname)
    if actor:
        equip = actor.inventory[equip]
        if equip:
            print('Equip {0} in {1}'.format(equip, aname))
            actor.equipment.append(equip)
    return True


@command("UNEQUIP aname equip")
@argo('aname', T_Actor(data_cache), None)
@argo('equip', T_Equip(data_cache, equip=False), None)
def do_unequip_actor(aname, equip):
    """Equip an item in an actor.
    """
    actor = play._game.find_actor_by_name(aname)
    if actor:
        equip = actor.equipment[equip]
        if equip:
            print('Unequip {0} in {1}'.format(equip, aname))
            actor.equipment.remove(equip)
    return True


@command("debug aname attr value")
@argo('aname', T_Actor(data_cache), None)
@argo('attr', T_Attr(data_cache), None)
@argo('value', Int(), None)
def do_debug_player(aname, attr, value):
    """Updates actor attribute.
    """
    actor = play._game.find_actor_by_name(aname)
    if actor:
        actor.attrs[attr].Base = value
        play.do_print_player("name={}".format(aname))
    return True


@command('REFRESH')
def do_refresh():
    """Refreshes board game.
    """
    play._game._updateActors()
    return True


@command('HIT')
def do_hit():
    """Just a hit.
    """
    import time
    import shutil
    import os
    import sys
    import termios
    import fcntl

    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    # rows, columns = os.popen('stty size', 'r').read().split()
    columns, rows = shutil.get_terminal_size()
    t = 0
    inc = 1
    delay = 0.02
    line = ['.'] * columns
    line[10] = '['
    line[20] = ']'
    line[30] = '<'
    line[40] = '>'
    line[54] = '<'
    line[55] = '('
    line[58] = ')'
    line[59] = '>'
    print(''.join(line), end='\r', flush=True)
    try:
        while True:
            # st = '.' * t
            # st = line[:t] + '|'
            save = line[t]
            line[t] = '|'
            print(''.join(line), end='\r', flush=True)
            line[t] = save
            t += inc
            time.sleep(delay)
            if ' ' == sys.stdin.read(1):
                print('\nstop at {}'.format(t - 1))
                break
            if t == columns - 1 or t == 0:
                # print(line, end='\r', flush=True)
                # t = 0
                inc *= -1
    except Exception:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        return True


if __name__ == '__main__':

    # cli = Play()
    # cli.run(prompt='rpgRun> ',
    #         toolbar=cli.set_toolbar,
    #         rprompt=cli.set_rprompt,
    #         precmd=True)
    h = Handler()
    h.create_namespace('__main__')
    h.switch_and_run_namespace('__main__')
