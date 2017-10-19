from rpgrun.bsprite import BSprite
from rpgrun.bobject import BObject


class Pillar(BObject):

    def __init__(self, x, y, width, **kwargs):
        super(Pillar, self).__init__(x, y, 'PILLAR', **kwargs)
        self.sprite = BSprite(spr_text='|||||||', width=width, color="\x1b[44m")
