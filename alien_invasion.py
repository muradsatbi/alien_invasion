import sys

import pygame

from settings import Settings
# импортируем класс из модуля с настройками
from ship import Ship
# импортируем класс Ship из модуля ship
from bullet import Bullet
# импортируем класс Bullet из модуля bullet
from alien import Alien


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.settings = Settings()
        # загружаем все настройки из модуля settings в переменную self.settings
        # нужно удалить все присваивания настроек внутри этого кода, но мы их
        # просто закомментим

        # self.screen = pygame.display.set_mode((1200, 800))
        # Создает окно, в котором будет идти работа, аргумент - кортеж,
        # представляющий собой размеры игрового окна
        # Объект окна создается присваивается атрибуту self.screen,
        # что позволяет работать с ним во всех методах класса
        # Часть экрана в PyGame называется поверхностью

        # self.screen = pygame.display.set_mode((self.settings.screen_width,
        #                                      self.settings.screen_height))
        # задаем переменную self.screen уже через переменные объекта
        # self.settings screen_width и screen_height

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Метод pygame.FULLSCREEN получает и присваивает self.screen широту и
        # высоту экрана
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # Просто присваиваем атрибутам новые значения. На данном этапе это ни
        # на что не влияет

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

        self.bullets = pygame.sprite.Group()
        # Создается группа

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            # Отслеживание событий клавиатуры и мыши

            self.ship.update()
            # Вызов метода обновления корабля с учетом новых событий

            self._update_bullets()
            # Вызов метода обновления пуль

            self._update_screen()
            # Обновляет экран

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)

    def _check_events(self):
        # Событие - действие, выполняемое пользователем во время игры
        for event in pygame.event.get():
            # цикл для получения событий
            if event.type == pygame.QUIT:
                # Условие, если тип события - это pygame.QUIT, то есть,
                # нажатие крестика в правом углу, то система выходит из
                # игрового окна
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # проверка типа события на тип нажатие клавиши
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # проверка типа события на тип нажатие клавиши
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # проверка нажания клавиши вправо
            self.ship.moving_right = True
            # переключение флажка в True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            # переключение флажка в True
        elif event.key == pygame.K_q:
            sys.exit()
            # Если нажатие клавиши равно q: выход из системы
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # проверка нажатия клавиши вправо
            self.ship.moving_right = False
            # переключение флажка в True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            # переключение флажка в True

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            # Условие, если длина группы пуль меньше ограничителя из settings
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # Присваиваем переменной new_bullet объект класса Bullet() и затем
            # добавляем этот объект в группу bullets

    def _update_screen(self):
        # self.screen.fill(self.bg_color)
        # В этом методе экран при каждом цикле заполняется заданным цветом.

        self.screen.fill(self.settings.bg_color)
        # Заменяем параметры из внутреннего кода на параметры из модуля
        # settings

        self.ship.blitme()
        # вызов этого метода blitme после заполнения фона выводит это
        # изображение поверх фона

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Перебираем все пули из bullets методом sprites и применяем к
        # каждому из них метод draw для обрисовки

        self.aliens.draw(self.screen)
        # прорисовываем пришельцев на экране

        # Отображение последнего прорисованного экрана
        pygame.display.flip()
        # Этот "метод" постоянно обновляет экран, показывая новые
        # изображения и скрывая старые

    def _update_bullets(self):
        self.bullets.update()  # как метод update() из класса Bullet работает
        # здесь? Как?
        # Понял: bullet появляется в bullets в методе _fire_bullet, а метод
        # update работает по отношению к bullets потому что это спрайт из
        # bullet
        # Вызов update для группы приводит к автоматическому вызову
        # update для каждого спрайта в группе

        for bullet in self.bullets.copy():
            # перебирает пули в копии bullets
            if bullet.rect.bottom <= 0:
                # проверяет условие, если низ пули выше верха экрана (0)
                self.bullets.remove(bullet)
                # удаляет эту пулю из основной группы


# if __name__ == 'main':
# Создание экземпляра и запуск игры.
# Эти два аспекта заключены в блок if, чтобы запуск игры совершался
# только при прямом вызове функции, но пока для проверки работы блок if
# закомменчен
ai = AlienInvasion()
ai.run_game()
