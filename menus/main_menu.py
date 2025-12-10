import pygame
from menus.menu import Menu

class MainMenu(Menu):
    def __init__(self, screen, start_game_callback, open_settings_callback):
        font = pygame.font.SysFont("Consolas", 50)
        options = [
            ("Start Game", self.start_game),
            ("Settings", self.open_settings),
            ("Quit", self.quit_game)
        ]

        super().__init__(screen, options, font)

    
    def start_game(self):
        # Switch state to the gameplay
        pass


    def open_settings(self):
        # Switch state to the settings menu
        pass


    def quit_game(self):
        pygame.quit()
        exit()