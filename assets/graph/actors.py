from rpgrun.bsprite import BSprite
from rpgrun.actor import Actor
from rpgrun.pactor import PActor
from assets.graph.gsprite import GameSprite
import pygame

PLAYER_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                   {"str": {"base": 9, "delta": 1, "buffs": "None"}},
                   {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''

ACTOR_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                  {"str": {"base": 5, "delta": 1, "buffs": "None"}},
                  {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''

MAGE_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                 {"mp": {"base": 10, "delta": 1, "buffs": "None"}},
                 {"str": {"base": 5, "delta": 1, "buffs": "None"}},
                 {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''

BOSS_ATTRS = [("hp", 100, 10), ("mp", 10, 1), ("str", 10, 1), ("con", 10, 2)]


class PlayerSprite(GameSprite):

    def __init__(self, width, height):
        super(PlayerSprite, self).__init__()
        image = pygame.Surface((width, height))
        image.fill((255, 0, 255))
        self.image = image
        self.rect = self.image.get_rect()


class PlayerActor(PActor):

    def __init__(self, x, y, width, height, **kwargs):
        super(PlayerActor, self).__init__(x, y, 'PLAYER', **kwargs)
        self.sprite = BSprite(spr_graph=PlayerSprite(width, height))
        self.attrs.setup_attrs_from_json(PLAYER_ATTRS)


class EnemySprite(GameSprite):

    def __init__(self, width, height):
        super(EnemySprite, self).__init__()
        image = pygame.Surface((width, height))
        image.fill((55, 125, 55))
        image_selected = pygame.Surface((width, height))
        image_selected.fill((0, 0, 0))
        self.set_image(image, image_selected)
        self.rect = self.image.get_rect()


class EnemyActor(Actor):

    def __init__(self, x, y, width, height, name='ENEMY', **kwargs):
        super(EnemyActor, self).__init__(x, y, name, **kwargs)
        self.sprite = BSprite(spr_graph=EnemySprite(width, height))
        self.attrs.setup_attrs_from_json(ACTOR_ATTRS)
