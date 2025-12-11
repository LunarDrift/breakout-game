from constants import PADDLE_COLORS, BALL_COLORS

class Settings:
    def __init__(self):
        self.paddle_color_name = "GREEN"
        self.ball_color_name = "GRAY"
        self.max_lives = 3


    @property
    def paddle_color(self):
        # Return RGB value of current name
        return PADDLE_COLORS[self.paddle_color_name]
    
    @property
    def ball_color(self):
        # Return RGB value of current name
        return BALL_COLORS[self.ball_color_name]

    
    def toggle_paddle_color(self):
        names = list(PADDLE_COLORS.keys())
        current_index = names.index(self.paddle_color_name)
        self.paddle_color_name = names[(current_index + 1) % len(names)]


    def toggle_ball_color(self):
        names = list(BALL_COLORS.keys())
        current_index = names.index(self.ball_color_name)
        self.ball_color_name = names[(current_index + 1) % len(names)]

    
    def increase_lives(self):
        if self.max_lives < 10:
            self.max_lives += 1

    def decrease_lives(self):
        if self.max_lives > 1:
            self.max_lives -= 1