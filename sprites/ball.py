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


    def reset(self, color):
        """Resets the ball to its starting position and velocity."""
        self.color = color
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
            

    def bounce_off_brick(self, brick, brick_destroyed):
        """Bounce the ball off the brick based on overlap depth to determine true collision side."""

        # Calculate overlap amounts on each side
        overlap_left   = self.rect.right  - brick.rect.left
        overlap_right  = brick.rect.right - self.rect.left
        overlap_top    = self.rect.bottom - brick.rect.top
        overlap_bottom = brick.rect.bottom - self.rect.top

        # Only keep positive overlaps (actual penetration)
        overlaps = {
            "left":   overlap_left,
            "right":  overlap_right,
            "top":    overlap_top,
            "bottom": overlap_bottom
        }

        # Filter out negative overlaps (no collision on that side)
        overlaps = {side: val for side, val in overlaps.items() if val >= 0}

        if not overlaps:
            return  # No valid overlap — shouldn't happen, but safe guard.

        # Determine the side with the smallest penetration depth
        collision_side = min(overlaps, key=overlaps.get)

        # Respond based on which side has the smallest overlap
        if collision_side == "left":
            self.rect.right = brick.rect.left
            self.velocity.x *= -1

        elif collision_side == "right":
            self.rect.left = brick.rect.right
            self.velocity.x *= -1

        elif collision_side == "top":
            self.rect.bottom = brick.rect.top
            self.velocity.y *= -1

        elif collision_side == "bottom":
            self.rect.top = brick.rect.bottom
            self.velocity.y *= -1

        # Sync logical position back to the rect
        self.position.x = self.rect.centerx
        self.position.y = self.rect.centery

        # Scale speed based on brick toughness
        if brick_destroyed or BRICK_POINTS[brick.max_health] == min(BRICK_POINTS.values()):
            current_speed = self.velocity.length()
            boost = BRICK_POINTS[brick.max_health] * BRICK_SPEED_POINT_FACTOR
            new_speed = min(current_speed + boost, BALL_MAX_SPEED)

            # Scale velocity vector to match new speed
            self.velocity.scale_to_length(new_speed)