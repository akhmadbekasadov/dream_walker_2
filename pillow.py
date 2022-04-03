import pygame
import controls
from pygame.sprite import Group


class Pillow(pygame.sprite.Sprite):
    """class one pillow"""

    def __init__(self, screen):
        """inicialization and starting position"""

        super(Pillow, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/test/pillow.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = -self.rect.height
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self):
        """output pillow on the screen"""

        self.screen.blit(self.image, self.rect)

    def update(self, velocity):
        """movement pillows"""

        self.y += velocity
        self.rect.y = self.y

