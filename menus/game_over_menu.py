import pygame
from constants import SCREEN_WIDTH

class GameOverScene:
    def __init__(self, screen, score, background_surface, go_to_main_menu, restart_game, quit_game):
        self.screen = screen
        self.score = score
        self.background = background_surface
        self.go_to_main_menu = go_to_main_menu
        self.restart_game = restart_game
        self.quit_callback = quit_game


        self.font = pygame.font.SysFont("Pixeled", SCREEN_WIDTH // 30)
        self.small_font = pygame.font.SysFont("Pixeled", SCREEN_WIDTH // 50)

        # Semi-transparent overlay
        self.overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 180))  # 180 alpha ≈ 70% opacity


    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart_game()
                if event.key == pygame.K_ESCAPE:
                    self.go_to_main_menu()
                if event.key == pygame.K_q:
                    self.quit_callback()


    def update(self, dt):
        pass


    def draw(self):
        # Draw frozen game scene as background
        self.screen.blit(self.background, (0, 0))
        # Draw semi-transparent overlay
        self.screen.blit(self.overlay, (0, 0))

        # Draw text
        center_x = self.screen.get_width() // 2
        self.screen.blit(self.font.render("GAME OVER", True, (255, 0, 0)),
                         self.font.render("GAME OVER", True, (255, 0, 0)).get_rect(center=(center_x, 150)))
        self.screen.blit(self.small_font.render(f"FINAL SCORE: {self.score}", True, (255, 255, 255)),
                         self.small_font.render(f"FINAL SCORE: {self.score}", True, (255, 255, 255)).get_rect(center=(center_x, 250)))
        self.screen.blit(self.small_font.render("PRESS R TO RESTART, Q TO QUIT, OR ESC TO MENU", True, (255, 255, 255)),
                         self.small_font.render("PRESS R TO RESTART, Q TO QUIT, OR ESC TO MENU", True, (255, 255, 255)).get_rect(center=(center_x, 350)))