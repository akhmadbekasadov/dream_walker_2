import pygame.font
import time


class Scores:
    """
    Output game info
    """
    def __init__(self, screen, stats):
        """
        Initialization counting scores
        """
        self.lifes_rect = None
        self.lifes_img = None
        self.high_score_rect = None
        self.high_score_img = None
        self.score_rect = None
        self.score_img = None

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont("", 36)

        self.passed_time = 0
        self.starting_time = time.time()

        self.image_score()
        self.image_high_score()
        self.image_lifes()

    def image_score(self):
        """
        Text score to graphic image
        """
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 255, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx

    def image_high_score(self):
        """text record score to graphic image"""

        self.high_score_img = self.font.render(str(self.stats.high_score), True, self.text_color, (100, 100, 100))
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.left = self.screen_rect.left
        self.high_score_rect.top = 20

    def image_lifes(self):
        """number of lifes"""

        self.lifes_img = self.font.render(str(self.stats.persons_life), True, self.text_color, (0, 0, 255))
        self.lifes_rect = self.lifes_img.get_rect()
        self.lifes_rect.right = self.screen_rect.right
        self.lifes_rect.top = 20

    def show_score(self):
        """output score on the screen"""

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.lifes_img, self.lifes_rect)

        self.passed_time = time.time() - self.starting_time
        self.stats.update_tick(int(10 * self.passed_time))
        self.image_score()
