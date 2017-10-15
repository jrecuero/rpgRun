import pygame


class SceneBase(object):

    def __init__(self):
        self.next = self

    def process_input(self, events, pressed_keys):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def render(self, screen):
        raise NotImplementedError

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)


def run_game(width, height, fps, starting_scene):
    pygame.init()
    pygame.display.set_caption('Basic Scene')
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    active_scene = starting_scene
    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)
        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(screen)
        active_scene = active_scene.next
        pygame.display.flip()
        clock.tick(fps)


# The rest is code where you implement your game using the Scenes model.

class TitleScene(SceneBase):

    def __init__(self):
        super(TitleScene, self).__init__()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(GameScene())

    def update(self):
        pass

    def render(self, screen):
        screen.fill((255, 0, 0))


class GameScene(SceneBase):

    def __init__(self):
        super(GameScene, self).__init__()
        self.car_image = pygame.image.load('racecar.png')
        width, height = pygame.display.get_surface().get_size()
        self.x = width * 0.45
        self.y = height * 0.8
        self.x_change = 0

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_change -= 5
                elif event.key == pygame.K_RIGHT:
                    self.x_change += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.x_change = 0
        self.x += self.x_change

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 255))
        screen.blit(self.car_image, (self.x, self.y))
        self.y -= 1


run_game(800, 600, 60, TitleScene())
