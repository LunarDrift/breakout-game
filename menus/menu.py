import pygame
import sys


class Menu:
    """Base class for all menus."""
    def __init__(self, screen, options, font, quit_callback, font_color=(255, 255, 255), highlight_color=(255, 255, 0), spacing=50):
        self.screen = screen
        self.options = options  # list of (label, callback) tuples
        self.font = font
        self.font_color = font_color
        self.highlight_color = highlight_color
        self.quit_callback = quit_callback
        self.selected_index = 0
        self.spacing = spacing
        self.option_rects = []


    def handle_input(self, events):
        mouse_pos = pygame.mouse.get_pos()

        
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_callback()
                sys.exit()

            # Navigate up/down with keys
            # Activate option on Enter/Click
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    # Activate the selected option
                    label, callback = self.options[self.selected_index]
                    callback()

            # Mouse input
            elif event.type == pygame.MOUSEMOTION:
                # Highlight the option the mouse is hovering over
                for i, rect in enumerate(self.option_rects):
                    if rect.collidepoint(mouse_pos):
                        self.selected_index = i
                        break

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Activate the clicked option
                for i, rect in enumerate(self.option_rects):
                    if rect.collidepoint(mouse_pos):
                        label, callback = self.options[i]
                        callback()
                        break

    def update(self, dt):
        # Optional animations, transitions, etc.
        pass


    def draw(self):
        # Draw all options
        # Highlight self.options[self.selected_index]
        self.screen.fill((0, 0, 0))  # Clear screen with black
        center_x = self.screen.get_width() // 2
        start_y = self.screen.get_height() // 2 - (len(self.options) * self.spacing) // 2
        
        # Store option rects for mouse interaction
        self.option_rects = []
        
        for i, (label, _) in enumerate(self.options):
            color = self.highlight_color if i == self.selected_index else self.font_color
            text_surf = self.font.render(label, True, color)
            text_rect = text_surf.get_rect(center=(center_x, start_y + i * self.spacing))
            self.screen.blit(text_surf, text_rect)
            self.option_rects.append(text_rect)