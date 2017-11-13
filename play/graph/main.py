from scenes.main_scene import MainScene
from scenes.title_scene import TitleScene


if __name__ == '__main__':
    game = MainScene(1200, 900)
    game.run(60, TitleScene())
