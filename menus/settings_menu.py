import pygame
from menus.menu import Menu


class SettingsMenu(Menu):
    def __init__(self, screen, back_callback, quit_callback):
        font = pygame.font.SysFont("Consolas", 40)
        # Example settings options
        options = [
            ("Option 1: ON", None),
            ("Option 2: OFF", None),
            ("Back", back_callback)
        ]

        super().__init__(screen, options, font, quit_callback)
        self.quit_callback = quit_callback