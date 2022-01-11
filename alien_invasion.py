import sys

import pygame

from settings import Settings
# импортируем класс из модуля с настройками
from ship import Ship


# импортируем класс ship из модуля Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.settings = Settings()
        # загружаем все настройки из модуля settings в переменную self.settings
        # нужно удалить все присваивания настроек внутри этого кода, но мы их
        # просто закомментим

        # self.screen = pygame.display.set_mode((1200, 800))
        # Создает окно, в котором будет идти работа, аргумент - кортеж,
        # представляющий собой размеры игрового окна.
        # Объект окна создается присваивается атрибуту self.screen,
        # что позволяет работать с ним во всех методах класса
        # Часть экрана в PyGame называется поверхностью

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # задаем переменную self.screen уже через переменные объекта
        # self.settings screen_width и screen_height

        pygame.display.set_caption("Инопланетное вторжение")
        # Задается заголовок игрового экрана

        # Назначим цвет фона, чтобы потом им заменить черный цвет по
        # умолчанию. Делается это в методе __init__
        # self.bg_color = (2, 86, 105)
        # Цвета в pygame задаются в схеме RGB

        self.ship = Ship(self)
        # Создаем объект класса Ship и передаем ему экземпляр AlienInvasion
        # при помощи передачи аргумента self классу Ship. Присваиваем все это
        # объекту self.ship

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()
            # Отслеживание событий клавиатуры и мыши.

    def _check_events(self):
        # Событие - действие, выполняемое пользователем во время игры
        for event in pygame.event.get():
            # цикл для получения событий
            if event.type == pygame.QUIT:
                # Условие, если тип события - это pygame.QUIT, то есть,
                # нажатие крестика в правом углу, то система выходит из
                # игрового окна
                sys.exit()

    def _update_screen(self):
        # self.screen.fill(self.bg_color)
        # В этом методе экран при каждом цикле заполняется заданным цветом.

        self.screen.fill(self.settings.bg_color)
        # Заменяем параметры из внутреннего кода на параметры из модуля
        # settings

        self.ship.blitme()
        # вызов этого метода blitme после заполнения фона выводит это
        # изображение поверх фона

        # Отображение последнего прорисованного экрана
        pygame.display.flip()
        # Этот "метод" постоянно обновляет экран, показывая новые
        # изображения и скрывая старые


# if __name__ == 'main':
# Создание экземпляра и запуск игры.
# Эти два аспекта заключены в блок if, чтобы запуск игры совершался
# только при прямом вызове функции, но пока для проверки работы блок if
# закомменчен
ai = AlienInvasion()
ai.run_game()
