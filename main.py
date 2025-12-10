import pygame
from sprites import Ball, Paddle, Brick
from constants import *


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout!")
clock = pygame.time.Clock()
running = True
dt = 0

# keep track of score
score = 0
score_font = pygame.font.SysFont("Consolas", int(SCREEN_WIDTH / 50))
lives = MAX_LIVES

# set up sprite groups
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

# make sure classes know which group to add to
Ball.containers = all_sprites
Paddle.containers = all_sprites
Brick.containers = (all_sprites, bricks)



def spawn_centered_bricks(
        screen_width,
        brick_width,
        brick_height,
        brick_count,
        y,
        gap,
        health,
        group
):
    """Spawns a centered row of evenly spaced bricks. Gap is applied between bricks AND between walls."""
    total_width = ((brick_count * brick_width) + ((brick_count + 1) * gap))
    start_x = (screen_width - total_width) / 2 + gap

    for i in range(brick_count):
        x = start_x + brick_width/2 + i *(brick_width + gap)
        Brick(brick_width, brick_height, x, y, health=health)
        group.add(bricks)

def spawn_brick_grid(rows, cols, gap, top_y, row_height, group):
    """Spawns a grid of bricks."""
    for r in range(rows):
        # Strongest bricks on top row
        health = rows - r
        y = top_y + r * (row_height + gap)
        spawn_centered_bricks(
            SCREEN_WIDTH,
            BRICK_WIDTH,
            BRICK_HEIGHT,
            cols,
            y,
            gap,
            health,
            bricks
        )


def reset_game():
    global lives, score
    lives = MAX_LIVES
    score = 0
    # remove all existing bricks
    for brick in bricks:
        brick.kill()
    # respawn bricks
    spawn_brick_grid(BRICK_ROWS, BRICK_COUNT, BRICK_GAP, BRICK_TOP_Y, BRICK_HEIGHT, bricks)

# create game objects
# ball
ball = Ball(BALL_COLOR, BALL_SIZE, BALL_START_X, BALL_START_Y, BALL_INITIAL_SPEED, -BALL_INITIAL_SPEED)
# player
player = Paddle(PADDLE_COLOR, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_START_X, PADDLE_START_Y, PADDLE_SPEED)
# bricks
spawn_brick_grid(BRICK_ROWS, BRICK_COUNT, BRICK_GAP, BRICK_TOP_Y, BRICK_HEIGHT, bricks)


while running:
    dt = clock.tick(FPS) / 1000  # limits FPS to 60
    keys = pygame.key.get_pressed()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if keys[pygame.K_ESCAPE]:
        running = False
   
    # update objects
    all_sprites.update(dt)

    # bounce ball off left/right edges
    if ball.rect.left <=0 or ball.rect.right >= SCREEN_WIDTH:
        ball.velocity.x *= -1

    # bounce ball off top edge
    if ball.rect.top <=0:
        ball.velocity.y *= -1

    # ball hits bottom edge - reset ball and player position
    if ball.rect.bottom >= SCREEN_HEIGHT:
        lives -= 1
        if lives <= 0:
            reset_game()
        ball.reset()
        player.reset()
    

    # collisions
    # paddle bounce
    if pygame.sprite.collide_rect(ball, player):
        ball.bounce_off_paddle(player)

    # ball hits brick; kill brick based on color, bounce ball
    hit_list = pygame.sprite.spritecollide(ball, bricks, False)
    for brick in hit_list:
        brick_was_alive = brick.health > 0
        brick.hit()

        # Only update score if brick was destroyed
        if brick_was_alive and brick.health == 0:
            score += BRICK_POINTS[brick.max_health]  # use max_health to award points based on original strength

        # Bounce ball on first brick hit only
        ball.bounce_off_brick(brick)
        break  # stop after first hit to avoid multiple bounces in one frame

        # ensure minimum speed
    if ball.velocity.length() < BALL_MIN_SPEED:
        ball.velocity.scale_to_length(BALL_MIN_SPEED)
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BG_COLOR)

    # RENDER YOUR GAME HERE
    # draw all sprites
    all_sprites.draw(screen)
    # draw scoreboard
    score_text = score_font.render(f"{score}", True, SCORE_COLOR)
    screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()


       

pygame.quit()