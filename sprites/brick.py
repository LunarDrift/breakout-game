import pygame
from .rectshape import RectShape
from constants import BRICK_HEALTH_COLORS


class Brick(RectShape):
    def __init__(self, width, height, x, y, health=None):
        # Determine starting health
        self.max_health = health if health is not None else 1
        self.health = self.max_health

        # Set initial color based on health
        self.color = BRICK_HEALTH_COLORS[self.health]

        # Initialize the RectShape with current color
        super().__init__(self.color, width, height)

        # Set position of brick (center)
        self.position = pygame.Vector2(x, y)        
        self.sync_rect()


    def hit(self):
        """Call when the ball hits the brick."""
        # Reduce health
        self.health -= 1

        if self.health > 0:
            # Update color based on new health
            self.color = BRICK_HEALTH_COLORS[self.health]
            # Update the image to reflect new color
            self.image.fill(self.color)
        else:
            # Destroy brick if health is 0
            self.destroy()


    def destroy(self):
        """Handle the destruction of the brick."""
        self.kill()  # Remove the brick from all sprite groups