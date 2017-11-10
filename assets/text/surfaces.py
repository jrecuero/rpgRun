from rpgrun.board.bsprite import TextSprite
from rpgrun.board.bsurface import BSurface


class GreenSurface(BSurface):

    def __init__(self, x, y, width, **kwargs):
        super(GreenSurface, self).__init__(x, y, '*', **kwargs)
        self.sprite = TextSprite(sprite=' ', color='\x1b[42m', width=width)
