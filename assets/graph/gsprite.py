import pygame


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, **kwargs):
        super(GameSprite, self).__init__(**kwargs)
        self.selected = False
        self._image = None
        self._image_selected = None

    @property
    def image(self):
        if self.selected:
            return self._image_selected
        else:
            return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self._image_selected = value

    def set_image_selected(self, value):
        self._image_selected = value
