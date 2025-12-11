class Settings:
    def __init__(self):
        self.paddle_color = (128, 255, 0)
        self.ball_color = (224, 224, 224)
        self.max_lives = 3

    
    def toggle_paddle_color(self):
        # cycle through some preset colors
        colors = [
            (128, 255, 0),  # default green
            (0, 255, 255),  # cyan
            (255, 0, 255),  # magenta
            (255, 255, 0),  # yellow
        ]
        current_index = colors.index(self.paddle_color)
        self.paddle_color = colors[(current_index + 1) % len(colors)]


    def toggle_ball_color(self):
        # cycle through some preset colors
        colors = [
            (224, 224, 224),  # default gray
            (255, 100, 100),  # light red
            (100, 255, 100),  # light green
            (100, 100, 255),  # light blue
        ]
        current_index = colors.index(self.ball_color)
        self.ball_color = colors[(current_index + 1) % len(colors)]

    
    def increase_lives(self):
        if self.max_lives < 10:
            self.max_lives += 1

    def decrease_lives(self):
        if self.max_lives > 1:
            self.max_lives -= 1