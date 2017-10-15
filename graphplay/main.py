import pygame
from title_scene import TitleScene


class GameRun(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        pygame.display.set_caption('Basic Scene')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def process_input_for_quit(self, event):
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True
        return False

    def process_input(self):
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if self.process_input_for_quit(event):
                self.active_scene.terminate()
            else:
                filtered_events.append(event)
        self.active_scene.process_input(filtered_events)

    def update(self):
        self.active_scene.update()

    def render(self):
        self.active_scene.render(self.screen)

    def run(self, fps, starting_scene):
        self.active_scene = starting_scene
        while self.active_scene is not None:
            # Process all input events.
            self.process_input()

            # Update any resource.
            self.update()

            # Render all required objects on screen.
            self.render()

            self.active_scene = self.active_scene.next_scene()
            pygame.display.flip()
            self.clock.tick(fps)


if __name__ == '__main__':
    game = GameRun(800, 600)
    game.run(60, TitleScene())
