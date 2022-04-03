import random
import pygame
import sys
from pillow import Pillow
import time


def events(screen, person, screen_size):
    """processing events"""

    step = screen_size[0] / 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #turn to the right and to the left
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and person.rect.centerx + step < screen_size[0]:
                person.rect.centerx = 2.5*step
            elif event.key == pygame.K_a and person.rect.centerx - step > 0:
                person.rect.centerx = 0.5*step
            elif event.key == pygame.K_s:
                person.rect.centerx = 1.5*step
        #key unpressed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                person.moveright = False
            elif event.key == pygame.K_a:
                person.moveleft = False
            elif event.key == pygame.K_s:
                person.moveright = False


def update(background_image, screen, stats, sc, person, pillows):
    """update screen"""

    screen.blit(background_image, (0, 0))
    sc.show_score()
    person.output()
    pillows.draw(screen)
    pygame.display.flip()


def create_army(screen, pillows, screen_size):
    """create army pillows"""

    position = screen_size[0] / 6
    step = screen_size[0] / 3
    number_pillow_x = 2

    for pillow_number in range(number_pillow_x):
        pillow = Pillow(screen)
        pillow.rect.centerx = position + step*random.randint(0, 2)
        pillows.add(pillow)


def update_pillows(stats, screen, sc, person, pillows, velocity):
    """update pillows position"""

    pillows.update(velocity)

    """check pillow touching to person"""
    if pygame.sprite.spritecollideany(person, pillows):
        person_kill(stats, screen, sc, person, pillows)


def person_kill(stats, screen, sc, person, pillows):
    """touching person and army"""

    if stats.persons_life > 0:
        stats.persons_life -= 1
        sc.image_lifes()
        pillows.empty()
        create_army(screen, pillows, screen.get_size())
        person.create_person()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def check_high_score(stats, sc):
    """check new records"""

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.img_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))
