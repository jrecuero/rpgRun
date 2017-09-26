from bcell import BSprite
from bobject import BObject


class Pillar(BObject):

    def __init__(self, theX, theY, theWidth, **kwargs):
        super(Pillar, self).__init__(theX, theY, 'PILLAR', **kwargs)
        self.Sprite = BSprite(theSprText='|||||||', theWidth=theWidth, theColor="\x1b[44m")
