from bcell import BSprite
from bsurface import BSurface


class GreenSurface(BSurface):

    def __init__(self, theX, theY, theWidth, **kwargs):
        super(GreenSurface, self).__init__(theX, theY, '*', **kwargs)
        self.Sprite = BSprite(theSprText=' ', theColor='\x1b[42m', theWidth=theWidth)
