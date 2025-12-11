import pygame
from sprites import Ball, Paddle, Brick
from constants import *


class GameScene:
    def __init__(self, screen, settings, return_to_menu_callback, quit_callback):
        self.screen = screen
        self.settings = settings
        self.return_to_menu = return_to_menu_callback
        self.quit_callback = quit_callback
        
        self.all_sprites = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.score = 0
        self.lives = self.settings.max_lives
        self.score_font = pygame.font.SysFont("Consolas", SCREEN_WIDTH // 50)

        # Game objects
        self.ball = Ball(self.settings.ball_color, BALL_SIZE, BALL_START_X, BALL_START_Y, BALL_INITIAL_SPEED, -BALL_INITIAL_SPEED)
        self.player = Paddle(self.settings.paddle_color, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_START_X, PADDLE_START_Y, PADDLE_SPEED)

        # Add objects to sprite groups
        self.all_sprites.add(self.ball, self.player)

        # Spawn initial bricks
        self.spawn_brick_grid(BRICK_ROWS, BRICK_COUNT, BRICK_GAP, BRICK_TOP_Y, BRICK_HEIGHT)

        # Make classes aware of containers
        Ball.containers = self.all_sprites
        Paddle.containers = self.all_sprites
        Brick.containers = (self.all_sprites, self.bricks)


    # ---------------- Brick Spawning ----------------
    def spawn_centered_bricks(self, y, health):
        total_width = ((BRICK_COUNT * BRICK_WIDTH) + ((BRICK_COUNT + 1) * BRICK_GAP))
        start_x = (SCREEN_WIDTH - total_width) // 2 + BRICK_GAP

        for i in range(BRICK_COUNT):
            x = start_x + BRICK_WIDTH/2 + i * (BRICK_WIDTH + BRICK_GAP)
            brick = Brick(BRICK_WIDTH, BRICK_HEIGHT, x, y, health=health)
            self.bricks.add(brick)
            self.all_sprites.add(brick)


    def spawn_brick_grid(self, rows, cols, gap, top_y, row_height):
        """Spawns a grid of bricks."""
        for r in range(rows):
            health = rows - r  # Higher rows have higher health
            y = top_y + r * (row_height + gap)
            self.spawn_centered_bricks(y, health)

    
    def reset_game(self):
        self.lives = self.settings.max_lives
        self.score = 0
        # remove all existing bricks
        for brick in list(self.bricks):
            brick.kill()
        # respawn bricks
        self.spawn_brick_grid(BRICK_ROWS, BRICK_COUNT, BRICK_GAP, BRICK_TOP_Y, BRICK_HEIGHT)
        self.ball.reset(self.settings.ball_color)
        self.player.reset(self.settings.paddle_color)


    # ---------------- Input handling ----------------
    def handle_input(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.return_to_menu()
            return
        
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_callback()
                return

    
    # ---------------- Update ----------------
    def update(self, dt):
        self.all_sprites.update(dt)
        self.handle_collisions()


    # ---------------- Draw ----------------
    def draw(self):
        self.screen.fill(BG_COLOR)
        self.all_sprites.draw(self.screen)
        # Draw score and lives
        score_text = self.score_font.render(f"Score: {self.score}", True, SCORE_COLOR)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 10))
        lives_text = self.score_font.render(f"Lives: {self.lives}", True, SCORE_COLOR)
        self.screen.blit(lives_text, (10, 10))


    # ---------------- Collision Handling ----------------
    def handle_collisions(self):
        # Ball bounce on walls
        if self.ball.rect.left <= 0 or self.ball.rect.right >= SCREEN_WIDTH:
            self.ball.velocity.x *= -1
        if self.ball.rect.top <= 0:
            self.ball.velocity.y *= -1
        if self.ball.rect.bottom >= SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives <= 0:
                self.reset_game()
            self.ball.reset(self.settings.ball_color)
            self.player.reset(self.settings.paddle_color)

        # Paddle bounce
        if pygame.sprite.collide_rect(self.ball, self.player):
            self.ball.bounce_off_paddle(self.player)

        # Ball hits bricks
        hit_list = pygame.sprite.spritecollide(self.ball, self.bricks, False)
        for brick in hit_list:
            brick_was_alive = brick.health > 0
            brick.hit()
            if brick_was_alive and brick.health == 0:
                self.score += BRICK_POINTS[brick.max_health]
            self.ball.bounce_off_brick(brick)
            break

        # Enforce minimum speed
        if self.ball.velocity.length() < BALL_MIN_SPEED:
            self.ball.velocity.scale_to_length(BALL_MIN_SPEED)