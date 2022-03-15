import pygame
import sys
from pillow import Pillow
import time


def events(screen, person):
    """processing events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #turn to the right and to the left
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                person.rect.centerx += 250
            elif event.key == pygame.K_LEFT:
                person.rect.centerx -= 250
        #key unpressed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                person.moveright = False
            elif event.key == pygame.K_LEFT:
                person.moveleft = False


def update(background_image, screen, stats, sc, person, pillows):
    """update screen"""

    screen.blit(background_image, (0, 0))
    sc.show_score()
    person.output()
    pillows.draw(screen)
    pygame.display.flip()


def create_army(screen, pillows):
    """create army pillows"""

    pillow = Pillow(screen)
    pillow_width = pillow.rect.width
    number_pillow_x = 2
    for pillow_number in range(number_pillow_x):
        pillow = Pillow(screen)
        pillow.x = pillow_width + 3*pillow_width * pillow_number
        pillow.rect.x = pillow.x
        pillows.add(pillow)


def update_pillows(stats, screen, person, pillows):
    """update pillows position"""

    pillows.update()

    """check pillow touching to person"""
    if pygame.sprite.spritecollideany(person, pillows):
        person_kill(stats, screen, person, pillows)


def person_kill(stats, screen, person, pillows):
    """touching person and army"""

    if stats.persons_life > 0:
        stats.persons_life -= 1
        pillows.empty()
        create_army(screen, pillows)
        person.create_person()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def check_high_score(stats, sc):
    """check new records"""

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))




