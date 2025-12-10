import pygame
import math
from .rectshape import RectShape
from constants import *

class Ball(RectShape):
    def __init__(self, color, size, x, y, x_vel, y_vel):
        super().__init__(color, size, size)
        self.size = size
        self.start_x = x
        self.start_y = y
        self.start_x_vel = x_vel
        self.start_y_vel = y_vel
        # Set initial position
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(x_vel, y_vel)


    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        self.sync_rect()


    def reset(self):
        """Resets the ball to its starting position and velocity."""
        self.position = pygame.Vector2(self.start_x, self.start_y)
        self.velocity = pygame.Vector2(self.start_x_vel, self.start_y_vel)
        self.sync_rect()

    
    def clamp_speed(self):
        """Clamp the ball's speed to the maximum allowed."""
        # Limit horizontal speed to prevent near-horizontal bounces
        self.velocity.x = max(-BALL_MAX_X_SPEED, min(BALL_MAX_X_SPEED, self.velocity.x))
        # Limit total speed
        if self.velocity.length() > BALL_MAX_SPEED:
            self.velocity.scale_to_length(BALL_MAX_SPEED)


    def bounce_off_paddle(self, paddle):
        """Bounce the ball off the paddle with spin based on paddle movement, and stronger horizontal effect near paddle edges."""
        # Reverse vertical velocity (always bounce up)
        self.velocity.y = -abs(self.velocity.y)
        # Calculate offset from paddle center (-1 to 1)
        offset = (self.position.x - paddle.position.x) / (paddle.rect.width / 2)
        offset = max(-1, min(1, offset)) # Clamp to [-1, 1]
        # Apply horizontal 'kick' from hit position
        self.velocity.x += offset * EDGE_BOUNCE_FACTOR
        # Add 'spin' based on paddle movement
        self.velocity.x += paddle.velocity.x * BALL_SPIN_FACTOR
        # Clamp speed
        self.clamp_speed()
            

    def bounce_off_brick(self, brick):
        """Bounce the ball off a brick, reversing the appropriate velocity component based on collision side. Supposed to deal with corner cases. Should help to make the game feel more like classic Breakout."""
        # Determine overlap on each axis
        dx = (self.rect.centerx - brick.rect.centerx)
        dy = (self.rect.centery - brick.rect.centery)
        # Check dominant axis of collision
        if abs(dx) > abs(dy):
            # Horizontal collision
            self.velocity.x *= -1
        else:
            # Vertical collision
            self.velocity.y *= -1