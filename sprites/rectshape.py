import pygame

class RectShape(pygame.sprite.Sprite):
    # Constructor. Pass in color and its x,y position
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height

        if hasattr(self, "containers") and self.containers is not None:
            groups = self.__class__.containers
            if isinstance(groups, tuple):
                for g in groups:
                    g.add(self)
            else:
                groups.add(self)

        
        # Logical position (center)
        self.position = pygame.Vector2(0, 0)
        
        # Create an image of the rect and fill it with a color
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = (self.position.x, self.position.y) # keep in sync

        # Default velocity (optional)
        self.velocity = pygame.Vector2(0, 0)


    def sync_rect(self):
        """Keep the sprite's rect in sync with its logical position."""
        self.rect.center = (self.position.x, self.position.y)


    def update(self, dt):
        """Sub-classes should override this. If they move position, call sync_rect()."""
        pass

    def check_collision(self, other):
        return self.rect.colliderect(other.rect)
    
    def set_size(self, width, height):
        """Update the sprite size and refresh its surface."""
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.sync_rect()