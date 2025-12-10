import pygame
from game import GameScene
from menus.main_menu import MainMenu
from menus.settings_menu import SettingsMenu
from sprites import Ball, Paddle, Brick
from constants import *


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout!")
clock = pygame.time.Clock()
running = True

# create game scene
game_scene = GameScene(screen)

# Example: current_scene = game_scene for testing gameplay
current_scene = game_scene


while running:
    dt = clock.tick(FPS) / 1000  # limits FPS to 60
    events = pygame.event.get()
    current_scene.handle_input(events)
    current_scene.update(dt)
    current_scene.draw()
    pygame.display.flip()


       

pygame.quit()