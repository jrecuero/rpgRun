import pygame
from base_scene import BaseScene


class Car(pygame.sprite.Sprite):

    def __init__(self):
        super(Car, self).__init__()
        self.image = pygame.image.load('examples/racecar.png')
        self.rect = self.image.get_rect()
        width, height = pygame.display.get_surface().get_size()
        self.rect.x = width * 0.45
        self.rect.y = height * 0.8


class GameScene(BaseScene):

    def __init__(self):
        super(GameScene, self).__init__()
        # self.car_image = pygame.image.load('examples/racecar.png')
        width, height = pygame.display.get_surface().get_size()
        self.x = width * 0.45
        self.y = height * 0.8
        self.x_change = 0
        self.sprites = pygame.sprite.Group()
        self.car = Car()
        self.sprites.add(self.car)

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
        # screen.blit(self.car_image, (self.x, self.y))
        # self.y -= 1
        self.car.rect.x = self.x
        self.car.rect.y = self.y
        self.y -= 1
        self.sprites.draw(screen)
