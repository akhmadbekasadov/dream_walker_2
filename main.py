import pygame
import controls
from person import Person
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():

    pygame.init()

    background_image = pygame.image.load('image/test/roads.png')
    screen = pygame.display.set_mode(background_image.get_size())
    pygame.display.set_caption("Dream Walker")

    person = Person(screen)
    pillows = Group()
    controls.create_army(screen, pillows, screen_size=background_image.get_size())
    stats = Stats()
    sc = Scores(screen, stats)

    tmp = 0  # position
    velocity = 2

    while True:
        controls.events(screen, person, screen_size=background_image.get_size())
        if stats.run_game:
            person.update_person()
            controls.update(background_image, screen, stats, sc, person, pillows)
            controls.update_pillows(stats, screen, sc, person, pillows, velocity)

            tmp += velocity
            if tmp % 500 == 0:
                controls.create_army(screen, pillows, screen_size=background_image.get_size())


run()
