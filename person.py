import pygame
from pygame.sprite import Sprite


class Person(Sprite):

    def __init__(self, screen):
        """initialization person"""
        super(Person, self).__init__()
        self.center = None
        self.screen = screen
        self.image = pygame.image.load('image/person2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moveright = False
        self.moveleft = False

    def output(self):
        """draw person"""

        self.screen.blit(self.image, self.rect)

    def update_person(self):
        """update position person, ! add argument action (!)"""

        if self.moveright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 5
        if self.moveleft and self.rect.left > 0:
            self.rect.centerx -= 5

    def create_person(self):
        """create person in center in bottom"""
        self.center = self.screen_rect.centerx
