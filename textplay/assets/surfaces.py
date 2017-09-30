from bcell import BSprite
from bsurface import BSurface


class GreenSurface(BSurface):

    def __init__(self, x, y, width, **kwargs):
        super(GreenSurface, self).__init__(x, y, '*', **kwargs)
        self.sprite = BSprite(spr_text=' ', color='\x1b[42m', width=width)
