import sys

import pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        # Создает окно, котором будет идти работа, аргумент -
        # кортеж, представляющий собой размеры игрового окна
        # Объект окна создается присваивается атрибуту self.screen,
        # что позволяет работать с ним во всех методах класса
        # Часть экрана в PyGame называется поверхностью
        pygame.display.set_caption("Инопланетное вторжение")
        # задается заголовок игрового экрана

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == 'main':
    # создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
