import pygame


class Menu:
    """Base class for all menus."""
    def __init__(self, screen, options, font, font_color=(255, 255, 255), highlight_color=(255, 255, 0), spacing=50):
        self.screen = screen
        self.options = options  # list of (label, callback) tuples
        self.font = font
        self.font_color = font_color
        self.highlight_color = highlight_color
        self.selected_index = 0
        self.spacing = spacing


    def handle_input(self, events):
        # Navigate up/down with keys
        # Activate option on Enter/Click
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    # Activate the selected option
                    label, callback = self.options[self.selected_index]
                    if callback():
                        callback()


    def update(self, dt):
        # Optional animations, transitions, etc.
        pass


    def draw(self):
        # Draw all options
        # Highlight self.options[self.selected_index]
        self.screen.fill((0, 0, 0))  # Clear screen with black
        center_x = self.screen.get_width() // 2
        start_y = self.screen.get_height() // 2 - (len(self.options) * self.spacing) // 2
        
        for i, (label, _) in enumerate(self.options):
            color = self.highlight_color if i == self.selected_index else self.font_color
            text_surf = self.font.render(label, True, color)
            text_rect = text_surf.get_rect(center=(center_x, start_y + i * self.spacing))
            self.screen.blit(text_surf, text_rect)