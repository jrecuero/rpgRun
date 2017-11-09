import pygame
from scenes.base_scene import BaseScene
from scenes.game_scene import GameScene


class TitleScene(BaseScene):

    def __init__(self):
        super(TitleScene, self).__init__()
        self.font = pygame.font.SysFont("marion", 72)
        self.text = self.font.render('rpgRun', True, (0, 128, 0))

    def process_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(GameScene())

    def update(self):
        pass

    def render(self, screen):
        screen.fill((255, 0, 0))
        screen_width, screen_height = pygame.display.get_surface().get_size()
        text_width, text_height = self.text.get_size()
        screen.blit(self.text, ((screen_width - text_width) // 2,
                                (screen_height - text_height) // 2))
