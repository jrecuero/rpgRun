import pygame
import os

image_library = {}


def get_image(path):
    global image_library
    image = image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        image_library[path] = image
    return image


pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(get_image('ball.png'), (20, 20))
    # surface = pygame.Surface((100, 100))
    # screen.blit(surface, (20, 20))
    pygame.display.flip()
    clock.tick(60)
