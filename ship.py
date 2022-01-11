import pygame


class Ship():
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        # Метод __init__ получает два параметра: ссылку self и ссылку на
        # текущий экземпляр класса, в котором он вызывается. Таким образом,
        # класс Ship получает доступ ко всем игровым ресурсам, определенным в
        # Alien Invasion

        self.screen = ai_game.screen
        # Экран присваивается атрибуту Ship self.screen, чтобы обращаться к
        # нему во всех модулях класса

        self.screen_rect = ai_game.screen.get_rect()
        # Программа обращается к атрибуту rect объекта экрана при помощи
        # get_rect() и присваивает его self.screen_rect. Проще говоря,
        # мы определяем функцию прямоугольника экрана, в которой заложены
        # многие полезные методы такие как center, centerx, centery, top,
        # bottom, left, right

        self.image = pygame.image.load('D:/python projects/alien_invasion/ship.bmp')
        # Загружаем изображение корабля при помощи метода pygame.image.load()

        self.rect = self.image.get_rect()
        # Получаем, скажем так, прямоугольник изображения self.image,
        # применив к нему метод get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # Атрибуты прямоугольника корабля и прямоугольника экрана
        # выравниваются по заданным атрибутам

        # В pygame начало координат (0, 0) находится в левом верхнем углу

        self.moving_right = False
        self.moving_left = False
        # два вспомогательных флажка для функций движения корабля

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
        # Метод, который выводит изображение на экран

    def update(self):
        """Обновляет позицию корабля с учетом флагов передвижения"""
        if self.moving_right:
            self.rect.x += 1
            # действие - перенос прямоугольника корабля на 10 по икс вправо
        elif self.moving_left:
            self.rect.x -= 1
            # действие - перенос прямоугольника корабля на 10 по икс влево
