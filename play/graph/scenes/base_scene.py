class BaseScene(object):

    def __init__(self):
        self._next = self

    def process_input(self, events, pressed_keys):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def render(self, screen):
        raise NotImplementedError

    def switch_to_scene(self, next_scene):
        self._next = next_scene

    def terminate(self):
        self.switch_to_scene(None)

    def next_scene(self):
        return self._next

    def run(self, **kwargs):
        return True
