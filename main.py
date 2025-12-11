import pygame
from game import GameScene
from menus.main_menu import MainMenu
from menus.settings_menu import SettingsMenu
from menus.game_over_menu import GameOverScene
from settings import Settings
from constants import *


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout!")
clock = pygame.time.Clock()
running = True


# functions to switch scenes
def go_to_game():
    global current_scene, game_scene
    game_scene = GameScene(screen, settings, go_to_main_menu, quit_game, go_to_game_over)
    current_scene = game_scene


def go_to_settings():
    global current_scene
    current_scene = settings_menu


def go_to_main_menu():
    global current_scene
    current_scene = main_menu


def quit_game():
    global running
    running = False


def go_to_game_over(score, background_surface):
    global current_scene, game_over_scene
    game_over_scene = GameOverScene(
        screen,
        score,
        background_surface,
        go_to_main_menu,
        go_to_game,
        quit_game
    )
    current_scene = game_over_scene



# initialize settings
settings = Settings()

# create scenes
main_menu = MainMenu(screen, settings, go_to_game, go_to_settings, quit_game)
settings_menu = SettingsMenu(screen, settings, go_to_main_menu, quit_game)
game_scene = GameScene(screen, settings, go_to_main_menu, quit_game, go_to_game_over)

# start with main menu
current_scene = main_menu


while running:
    dt = clock.tick(FPS) / 1000  # limits FPS to 60
    if current_scene == game_scene:
        current_scene.next_round()
    events = pygame.event.get()
    current_scene.handle_input(events)
    current_scene.update(dt)
    current_scene.draw()
    pygame.display.flip()


pygame.quit()