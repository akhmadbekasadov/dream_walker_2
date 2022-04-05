import pygame
import controls
from person import Person
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()

    background_image = pygame.image.load('image/test/roads3.png')
    screen = pygame.display.set_mode(background_image.get_size())
    pygame.display.set_caption("Dream Walker")

    person = Person(screen)
    pillows = Group()
    # получаем самый первый сет подушек
    sub_pills = controls.create_army(screen, pillows, screen_size=background_image.get_size())
    stats = Stats()
    sc = Scores(screen, stats)

    velocity = 0.25

    while True:
        controls.events(screen, person, screen_size=background_image.get_size())
        if stats.run_game:
            person.update_person()
            controls.update(background_image, screen, stats, sc, person, pillows)
            controls.update_pillows(stats, screen, sc, person, pillows, velocity)

            if 200 <= stats.score < 400:
                velocity = 0.5
            elif stats.score >= 400:
                velocity = 0.75

            print([x.y for x in sub_pills.sprites()])  # принты пока оставь, чтобы было понимание
            # здесь следует настроить, когда именно вводить обновление сета подушек
            if sub_pills.sprites()[0].y > 600:  # если любая из сета подушек спустилась достаточно низко
                # то пора обновить сет подушек
                sub_pills = controls.create_army(screen, pillows, screen_size=background_image.get_size())


run()
