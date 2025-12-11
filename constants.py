# game constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60
BG_COLOR = (0, 0, 0)
MAX_LIVES = 3

# paddle constants
PADDLE_COLOR = (128, 255, 0)
PADDLE_SPEED = 420  # blaze it
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 20
PADDLE_START_X = SCREEN_WIDTH // 2
PADDLE_START_Y = SCREEN_HEIGHT - 40
MAX_PADDLE_SHRINK = 0.5  # Paddle can shrink to 50% of original size
MIN_PADDLE_WIDTH = PADDLE_WIDTH * MAX_PADDLE_SHRINK
PADDLE_COLORS = {
        "GREEN": (128, 255, 0),
        "CYAN": (0, 255, 255),
        "MAGENTA": (255, 0, 255),
        "YELLOW": (255, 255, 0),
        "WHITE": (255, 255, 255),
        "BLACK": (0, 0, 0),
        "ORANGE": (255, 165, 0)
    }

# score constants
SCORE_COLOR = (255, 255, 255)

# ball constants
BALL_COLOR = (224, 224, 224)
BALL_SIZE = 12
BALL_INITIAL_SPEED = 290
BALL_SPIN_FACTOR = 0.25  # tweak for feel; higher = more influence from paddle movement
BALL_MIN_SPEED = 180
BALL_MAX_SPEED = 600  # total vector length in pixels/second
BALL_MAX_X_SPEED = BALL_MAX_SPEED * 0.8 # prevents near-horizontal bounces
EDGE_BOUNCE_FACTOR = 120 # adjust slightly to taste; higher = stronger bounce off edges
BALL_START_X = SCREEN_WIDTH // 2
BALL_START_Y = SCREEN_HEIGHT // 2
BALL_COLORS = {
        "GRAY": (224, 224, 224),
        "WHITE": (255, 255, 255),
        "BLACK": (0, 0, 0),
        "LIGHT RED": (255, 100, 100),
        "LIGHT GREEN": (100, 255, 100),
        "LIGHT BLUE": (100, 100, 255)
    }

# brick constants
BRICK_WIDTH = 64
BRICK_HEIGHT = 24
BRICK_COUNT = 13
BRICK_ROWS = 5
BRICK_GAP = 10
BRICK_TOP_Y = 60
BRICK_POINTS = {
    1: 10,  # weakest (red)
    2: 20,
    3: 30,
    4: 40,
    5: 50   # strongest (blue)
}
BRICK_HEALTH_COLORS = {
    1: (255, 0, 0),
    2: (255, 165, 0),
    3: (255, 255, 0),
    4: (0, 128, 0),
    5: (0, 0, 255)
}
BRICK_SPEED_POINT_FACTOR = 1.5  # ball speed increase per brick hit based on toughness