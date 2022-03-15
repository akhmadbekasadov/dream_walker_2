import pygame


class Pillow(pygame.sprite.Sprite):
    """class one pillow"""

    def __init__(self, screen):
        """inicialization and starting position"""

        super(Pillow, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/pillow2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self):
        """output pillow on the screen"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """movement pillows"""

        self.y += 0.1
        self.rect.y = self.y
