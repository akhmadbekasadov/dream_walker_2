import pygame.font
from person import Person
from pygame.sprite import Group


class Scores():
    """output game info"""

    def __init__(self, screen, stats):
        """inicialization counting scores"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_persons()

    def image_score(self):
        """text score to graphic image"""

        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 255, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.score_rect.right
        self.score_rect.top = 20

    def image_high_score(self):
        """text record score to graphic image"""

        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 255, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_persons(self):
        """number of lifes"""

        self.persons = Group()
        for person_number in range(self.stats.persons_life):
            person = Person(self.screen)
            person.rect.x = 15 + person_number * person.rect.width
            person.rect.y = 20
            self.persons.add(person)

    def show_score(self):
        """output score on the screen"""

        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.persons.draw(self.screen)