import pygame
from .rectshape import RectShape

class Paddle(RectShape):
    def __init__(self, color, width, height, x, y, speed):
        super().__init__(color, width, height)

        self.color = color
        self.position = pygame.Vector2(x, y)
        self.speed = speed
        self.velocity = pygame.Vector2(0, 0)
        self.sync_rect()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Move left/right
        if keys[pygame.K_a]:
            self.position.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.position.x += self.speed * dt

        # Keep paddle within screen bounds
        screen_width = pygame.display.get_surface().get_width()
        half_w = self.rect.width / 2
        
        if self.position.x < half_w:
            self.position.x = half_w
        if self.position.x > screen_width - half_w:
            self.position.x = screen_width - half_w

        self.sync_rect()

    def reset(self, color):
        """Resets the paddle to the center bottom of the screen."""
        self.color = color
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()
        self.position = pygame.Vector2(screen_width / 2, screen_height - 50)
        self.sync_rect()
