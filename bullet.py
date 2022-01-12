import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # скажем так, делает экран игры также экраном и пули тоже
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # присваивает пуле цвет из настроек

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        # создает прямоугольник пули и присваивает ему значения ширины и
        # высоты из настроек
        self.rect.midtop = ai_game.ship.midtop
        # выравнивает середину верха пули и середину верха корабля

        self.y = float(self.rect.y)
        # сохраняет как координату y пули координату центра прямоугольника пули

    def update(self):
        # Перемещает пулю вверх по экрану
        self.y  -= self.settings.bullet_speed
        # Обновление позиции снаряда в вещественном формате
        self.rect.y  = self.y
        # Обновление позиции прямоугольника

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        # Рисует прямоугольник - указывая на чем, какого цвета и что рисовать