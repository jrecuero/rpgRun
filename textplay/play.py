# import sys
# sys.path.append('../jc2li')

import game
from blayer import LType
from bpoint import Point, Location
from shapes import Quad, Rhomboid
from base import Cli
from decorators import argo, syntax, setsyntax
from argtypes import Int
from brow import BRow
from action import AType
from actor import Actor
from assets.surfaces import GreenSurface
from assets.actors import PlayerActor, EnemyActor, MageActor, BossActor
from assets.bobjects import Pillar
from assets.actions import WeaponAction, MeleAction, RangeAction, MoveAction
from assets.equips import Weapon, Armor, Shield
from targs import T_Target, T_Actor, T_Equip, T_Attr, T_Action, T_Location, T_Step
import loggerator


class Play(Cli):

    SYSTEM = ['exit', 'help', 'syntax', 'debug', 'HIT']
    COMMON = ['PRINT', 'ACTORS', 'PLAYER', 'EQUIPMENT', 'INVENTORY', 'EQUIP', 'UNEQUIP']
    STAGES = {'wait': ['INIT'],
              'init': ['RUN'] + COMMON,
              'run': ['ACTION'] + COMMON,
              'target': ['TARGET'] + COMMON,
              'move': ['MOVEMENT'] + COMMON, }

    def __init__(self):
        super(Play, self).__init__()
        self._game = None
        self._logger = loggerator.getLoggerator('PLAY')
        self._stage = 'wait'

    def precmd(self, theCmd, theLine):
        if theCmd in self.STAGES[self._stage] + self.SYSTEM:
            return True
        else:
            print('command <{0}> not valid in stage <{1}>'.format(theCmd, self._stage))
            return False

    def _newRow(self):
        """Scroll Board.
        """
        width = self._game.Board.Width
        row = BRow(width)
        newHeight = self._game.Board.TopCellRow + 1
        for iwidth in range(width):
            row.addCellToLayer(GreenSurface(iwidth, newHeight, self._sprWidth), LType.SURFACE)
        return row

    def _scroll(self):
        """Scroll Board.
        """
        row = self._newRow()
        self._game.scrollBoard(row)

    @Cli.command('INIT')
    def do_init(self, *args):
        """Initialize rpgRUN game.
        """
        self._width = 7
        self._height = 7
        self._sprWidth = 7
        self._game = game.Game(self._width, self._height)
        self.Journal.setToCache('game', self._game)
        iheight = self._height
        for row in self._game.Board:
            iheight -= 1
            for iwidth in range(self._width):
                row.addCellToLayer(GreenSurface(iwidth, iheight, self._sprWidth), LType.SURFACE)

        Actor.LIFE = 'hp'
        player = PlayerActor(2, 4, self._sprWidth)
        player.Actions.append(WeaponAction('weapon', AType.WEAPONIZE))
        player.Actions.append(MoveAction('move', AType.MOVEMENT))
        enemies = []
        enemies.append(EnemyActor(4, 6, self._sprWidth, 'GOBLIN'))
        enemies.append(EnemyActor(3, 5, self._sprWidth, 'ORC'))
        enemies.append(EnemyActor(1, 0, self._sprWidth, 'TROLL'))
        enemies.append(MageActor(0, 5, self._sprWidth, 'MAGE'))
        enemies.append(BossActor(1, 5, self._sprWidth))
        enemies[-1].Life = 'mp'
        pillar = Pillar(0, 6, self._sprWidth)

        sword = Weapon(theName='sword', theAttrBuff={'str': 5})
        sword.Actions.append(MeleAction('mele', AType.WEAPONIZE, theWidth=2, theHeight=2, theShape=Quad))
        bow = Weapon(theName='bow', theAttrBuff={'str': 2})
        bow.Actions.append(RangeAction('range', AType.WEAPONIZE, theWidth=3, theHeight=3, theShape=Rhomboid))
        armor = Armor(theAttrBuff={'hp': 10})
        shield = Shield(theAttrBuff={'hp': 7, 'str': 1})
        player.Inventory.append(sword)
        player.Inventory.append(bow)
        player.Inventory.append(armor)
        player.Inventory.append(shield)
        player.Equipment.append(sword)
        player.Equipment.append(armor)
        player.Equipment.append(shield)

        self._game.addActor(player, True)
        for x in enemies:
            self._game.addActor(x)

        self._game.Board.getRowFromCell(player).addCellToLayer(player, LType.OBJECT)
        self._game.Board.getRowFromCell(pillar).addCellToLayer(pillar, LType.OBJECT)
        for x in enemies:
            self._game.Board.getRowFromCell(x).addCellToLayer(x, LType.OBJECT)

        self._logger.display('Init rpgRun')

        # Run the game engine.
        self._game.runInit()
        self._stage = 'init'

    @Cli.command()
    @setsyntax
    @syntax("MOVE loc pos")
    @argo('loc', T_Location, None)
    @argo('pos', Int, None)
    def do_move_player(self, loc, pos):
        """Move player a number of positions to given location.
        """
        self._game.movePlayer(loc, pos)
        if loc == Location.FRONT:
            self._scroll()

    @Cli.command()
    @setsyntax
    @syntax("PLAYER [name]?")
    @argo('name', T_Actor, 'PLAYER')
    def do_print_player(self, name):
        """Print player information.
        """
        _actor = self._game.findActorByName(name)
        self._logger.display("Data for  : {0}".format(name))
        self._logger.display("Name      : {0}".format(_actor.Name))
        self._logger.display("Position  : {0}".format(_actor.getPoint()))
        self._logger.display("Attributes:\n{0}".format(_actor.Attrs))

    @Cli.command()
    @setsyntax
    @syntax("INVENTORY name")
    @argo('name', T_Actor, None)
    def do_print_inventory(self, name):
        """Prints player inventory.
        """
        _actor = self._game.findActorByName(name)
        self._logger.display("Inventory for  : {0}".format(name))
        for x in _actor.Inventory:
            self._logger.display(">> {0}".format(x))

    @Cli.command()
    @setsyntax
    @syntax("EQUIPMENT name")
    @argo('name', T_Actor, None)
    def do_print_equipment(self, name):
        """Prints player equipment.
        """
        _actor = self._game.findActorByName(name)
        self._logger.display("Equipment for  : {0}".format(name))
        for x in _actor.Equipment:
            self._logger.display(">> {0}".format(x))

    @Cli.command('ACTORS')
    def do_print_actors(self, *args):
        """Print actors attributes.
        """
        for _actor in self._game.Actors:
            self._logger.display("Data for  : {0}".format(_actor.Name))
            self._logger.display("Position  : {0}".format(Point.__repr__(_actor)))
            self._logger.display("Attributes:\n{0}".format(_actor.Attrs))

    @Cli.command('PRINT')
    def do_print_board(self, *args):
        """Print rpgRUN game board.
        """
        self._logger.display(self._game.Board.render(theWidth=7))

    @Cli.command('SCROLL')
    def do_scroll_board(self, *args):
        """Scroll Board.
        """
        self._scroll()

    @Cli.command('RUN')
    def do_run(self, *args):
        """Run a cycle
        """
        print('select action (use command: ACTION <name>) ')
        for i, x in enumerate(self._game.Player.AllActions):
            print('{0} : {1}'.format(i, x.Name))
        self.Prompt = '[ACTION <name>] rpgRun> '
        self._stage = 'run'

    @Cli.command()
    @setsyntax
    @syntax("ACTION name")
    @argo('name', T_Action, None)
    def do_action(self, name):
        """Select action to run.
        """
        for _action in self._game.Player.Actions:
            if _action.Name == name:
                break
        else:
            return
        _action.Originator = self._game.Player
        # self._game.runInit()
        _actionType = self._game.runSelectAction(_action)
        if _actionType == AType.WEAPONIZE:
            print('select target (use command: TARGET <name>)')
            for i, x in enumerate(self._game.TargetChoice):
                print('{0} : {1}'.format(i, x))
            self.Prompt = '[TARGET <name>] rpgRun> '
            self._stage = 'target'
        elif _actionType == AType.MOVEMENT:
            print('select player movement (use command: MOVEMENT <loc> <pos>)')
            self.Prompt = '[MOVEMENT <loc> <pos>] rpgRun> '
            self._stage = 'move'

    @Cli.command()
    @setsyntax
    @syntax("TARGET name")
    @argo('name', T_Target, None)
    def do_target(self, name):
        """Select target for the action to run.
        """
        for _target in self._game.TargetChoice:
            if _target.Name == name:
                break
        else:
            return
        self._game.runSelectTarget(_target)
        self.Prompt = 'rpgRun> '
        self._stage = 'init'

    @Cli.command()
    @setsyntax
    @syntax("MOVEMENT loc pos")
    @argo('loc', T_Location, None)
    @argo('pos', T_Step, None)
    def do_select_movement(self, loc, pos):
        """Select location and steps for the player to move.
        """
        print('player moves {0} to {1}'.format(pos, loc))
        self._game.runSelectMovement(loc, pos)
        self._game.runScroll(self._newRow())
        # self._scroll()
        self._stage = 'init'

    @Cli.command()
    @setsyntax
    @syntax("EQUIP aname equip")
    @argo('aname', T_Actor, None)
    @argo('equip', T_Equip, None)
    def do_equip_actor(self, aname, equip):
        """Equip an item in an actor.
        """
        _actor = self._game.findActorByName(aname)
        if _actor:
            _equip = _actor.Inventory[equip]
            if _equip:
                print('Equip {0} in {1}'.format(equip, aname))
                _actor.Equipment.append(_equip)

    @Cli.command()
    @setsyntax
    @syntax("UNEQUIP aname equip")
    @argo('aname', T_Actor, None)
    @argo('equip', T_Equip, None, theCompleterKwargs={'equip': False})
    def do_unequip_actor(self, aname, equip):
        """Equip an item in an actor.
        """
        _actor = self._game.findActorByName(aname)
        if _actor:
            _equip = _actor.Equipment[equip]
            if _equip:
                print('Unequip {0} in {1}'.format(equip, aname))
                _actor.Equipment.remove(_equip)

    @Cli.command()
    @setsyntax
    @syntax("debug aname attr value")
    @argo('aname', T_Actor, None)
    @argo('attr', T_Attr, None)
    @argo('value', Int, None)
    def do_debug_player(self, aname, attr, value):
        """Updates actor attribute.
        """
        _actor = self._game.findActorByName(aname)
        if _actor:
            _actor.Attrs[attr].Base = value
            self.do_print_player("name={}".format(aname))

    @Cli.command('REFRESH')
    def do_refresh(self, *args):
        """Refreshes board game.
        """
        self._game._updateActors()

    @Cli.command('HIT')
    def do_hit(self, *args):
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

    def set_toolbar(self):
        return " | ".join(cli.STAGES[cli._stage])

    def set_rprompt(self):
        return "<{0}>".format(self._stage)


if __name__ == '__main__':

    cli = Play()
    try:
        # cli.Prompt = 'rpgRun> '
        cli.cmdloop(thePrompt='rpgRun> ',
                    theToolBar=cli.set_toolbar,
                    theRPrompt=cli.set_rprompt,
                    thePreCmd=True)
    except KeyboardInterrupt:
        cli._logger.display("")
        pass
