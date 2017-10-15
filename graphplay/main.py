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

    def process_input_for_quit(self, event, pressed_keys):
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_ESCAPE:
                return True
            elif event.key == pygame.K_F4 and alt_pressed:
                return True
        return False

    def process_input(self):
        pressed_keys = pygame.key.get_pressed()
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if self.process_input_for_quit(event, pressed_keys):
                self.active_scene.terminate()
            else:
                filtered_events.append(event)
        self.active_scene.process_input(filtered_events, pressed_keys)

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
