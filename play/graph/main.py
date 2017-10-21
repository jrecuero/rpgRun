from main_scene import MainScene
from title_scene import TitleScene


if __name__ == '__main__':
    game = MainScene(800, 600)
    game.run(60, TitleScene())
