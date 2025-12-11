import pygame
from menus.menu import Menu


class SettingsMenu(Menu):
    def __init__(self, screen, settings, back_callback, quit_callback):
        self.settings = settings
        font = pygame.font.SysFont("Consolas", 40)
        # Example settings options
        options = [
                    (f"Paddle Color: {self.settings.paddle_color}", self.change_paddle_color),
                    (f"Ball Color: {self.settings.ball_color}", self.change_ball_color),
                    (f"Max Lives: {self.settings.max_lives}", self.change_max_lives),
                    ("Back", back_callback)
                ]

        super().__init__(screen, options, font, quit_callback)
        self.quit_callback = quit_callback

    def change_paddle_color(self):
        self.settings.toggle_paddle_color()
        self.update_labels()

    def change_ball_color(self):
        self.settings.toggle_ball_color()
        self.update_labels()

    def change_max_lives(self):
        # Example: cycle max lives between 1 and 5
        self.settings.max_lives = (self.settings.max_lives % 5) + 1
        self.update_labels()


    def update_labels(self):
        self.options[0] = (f"Paddle Color: {self.settings.paddle_color}", self.change_paddle_color)
        self.options[1] = (f"Ball Color: {self.settings.ball_color}", self.change_ball_color)
        self.options[2] = (f"Max Lives: {self.settings.max_lives}", self.change_max_lives)
        self.options[3] = ("Back", self.options[3][1])  # keep back callback