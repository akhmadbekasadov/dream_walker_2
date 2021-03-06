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
        # turn to the right and to the left
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and person.rect.centerx + step < screen_size[0]:
                person.rect.centerx = 2.5*step
            elif event.key == pygame.K_a and person.rect.centerx - step > 0:
                person.rect.centerx = 0.5*step
            elif event.key == pygame.K_s:
                person.rect.centerx = 1.5*step
        # key unpressed
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
    check_high_score(sc)
    sc.show_score()
    person.output()
    pillows.draw(screen)
    pygame.display.flip()


def create_army(screen, pillows, screen_size):
    """create army pillows"""

    pillows.empty()  # clean the old cushion set
    position = screen_size[0] / 6
    step = screen_size[0] / 3
    number_pillow_x = 2

    for pillow_number in range(1, number_pillow_x + 1):
        pillow = Pillow(screen)
        pillow.rect.centerx = position + step*random.randint(0, 2)
        pillows.add(pillow)

    return pillows  # bringing back an updated cushion set


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
        for i, y, z in zip(range(3, 0, -1), [200, 300, 400], [50, 75, 100]):
            label = pygame.font.SysFont("", z).render(f"{i}...", 1, (255, 255, 255))
            screen.blit(label, (300, y))
            pygame.display.update()
            time.sleep(1)
        # 3 2 1 paint
    else:
        stats.run_game = False
        raise AssertionError


def check_high_score(score):
    """check new records"""

    if score.stats.score > score.stats.high_score:
        score.stats.high_score = score.stats.score
        score.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(score.stats.high_score))
