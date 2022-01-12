class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    # Вместо того, чтобы добавлять настройки в коде самой игры, лучше создать
    # отдельный модуль, что мы и сделали, в нем прописать отдельный класс,
    # который хранит все настройки игры

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 4
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
