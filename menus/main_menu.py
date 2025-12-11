import pygame
from menus.menu import Menu

class MainMenu(Menu):
    def __init__(self, screen, settings, start_game_callback, open_settings_callback, quit_callback):
        self.settings = settings
        self.start_game_callback = start_game_callback
        self.open_settings_callback = open_settings_callback
        
        
        font = pygame.font.SysFont("Pixeled", 32)
        options = [
            ("START GAME", self.start_game),
            ("SETTINGS", self.open_settings),
            ("QUIT", self.quit_game)
        ]

        super().__init__(screen, options, font, quit_callback)

    
    def start_game(self):
        # Switch state to the gameplay
        self.start_game_callback()


    def open_settings(self):
        # Switch state to the settings menu
        self.open_settings_callback()


    def quit_game(self):
        self.quit_callback()