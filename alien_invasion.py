import sys

import pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        # Создает окно, котором будет идти работа, аргумент - кортеж,
        # представляющий собой размеры игрового окна.
        # Объект окна создается присваивается атрибуту self.screen,
        # что позволяет работать с ним во всех методах класса
        # Часть экрана в PyGame называется поверхностью
        pygame.display.set_caption("Инопланетное вторжение")
        # Задается заголовок игрового экрана

        # Назначим цвет фона, чтобы потом им заменить черный цвет по
        # умолчанию. Делается это в методе __init__
        self.bg_color = (2, 86, 105)
        # Цвета в pygame задаются в схеме RGB

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            # Событие - действие, выполняемое пользователем во время игры
            for event in pygame.event.get():
                # цикл событий для получения событий
                if event.type == pygame.QUIT:
                    # Условие, если тип события - это pygame.QUIT, то есть,
                    # нажатие крестика в правом углу, то система выходит из
                    # игрового окна
                    sys.exit()

            # При каждом переходе цикла прорисовывается экран заданного цвета.
            self.screen.fill(self.bg_color)
            # В этом методе экран при каждом цикле заполняется заданным цветом.

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
