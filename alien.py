import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        # скажем так, делает экран игры также экраном и пришельца тоже

        self.image = pygame.image.load(('D:/python '
                                        'projects/alien_invasion/alien.bmp'))
        # загружаем изображение пришельца
        self.rect = self.image.get_rect()
        # задаем прямоугольник для пришельца

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # пришелец появляется в левом верхнем углу экрана

        self.x = float(self.rect.x)
        # сохранение точной горизонтальной позиции пришельца

