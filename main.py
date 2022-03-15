import pygame
import controls
from person import Person
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Dream Walker")
    background_image = pygame.image.load('image/roads2.png')
    person = Person(screen)
    pillows = Group()
    controls.create_army(screen, pillows)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, person)
        if stats.run_game:
            person.update_person()
            controls.update(background_image, screen, stats, sc, person, pillows)
            controls.update_pillows(stats, screen, person, pillows)

run()
