import pygame
import controls
from person import Person
from pygame.sprite import Group
from stats import Stats
from scores import Scores
import windows
import datetime


def run():
    pygame.init()

    background_image = pygame.image.load('image/roads3.png')
    screen = pygame.display.set_mode(background_image.get_size())
    pygame.display.set_caption("Dream Walker")

    person = Person(screen)
    pillows = Group()
    # get the very first set of cushions
    sub_pills = controls.create_army(screen, pillows, screen_size=background_image.get_size())
    stats = Stats()
    sc = Scores(screen, stats)

    velocity = 0.1
    windows.start(sc)

    try:
        while True:
            controls.events(screen, person, screen_size=background_image.get_size())
            if stats.run_game:
                person.update_person()
                controls.update(background_image, screen, stats, sc, person, pillows)
                controls.update_pillows(stats, screen, sc, person, pillows, velocity)

                if 300 <= stats.score < 600:
                    velocity = 0.2
                elif 600 <= stats.score < 900:
                    velocity = 0.3
                elif 900 <= stats.score < 1200:
                    velocity = 0.4
                elif 1200 <= stats.score < 1500:
                    velocity = 0.5
                elif 1500 <= stats.score < 2000:
                    velocity = 0.6
                elif stats.score >= 2000:
                    velocity = 0.7

                # print([x.y for x in sub_pills.sprites()])  # leave the prints for now so that there is an understanding
                # here should be configured exactly when to enter the cushion set update
                if sub_pills.sprites()[0].y > 690:  # if any of the cushion set comes down low enough
                    # print(datetime.datetime.now().strftime("%H:%M:%S:%f"))
                    # it's time to update the cushion set
                    sub_pills = controls.create_army(screen, pillows, screen_size=background_image.get_size())
    except AssertionError:
        gameover(stats.score, stats.high_score)


def gameover(resultat, high_resultat):
    while (1):
        windows.screen.blit(windows.background_image, (0, 0))

        label = pygame.font.SysFont("", 66).render("Sweet dreams!", 1, (153, 255, 255))
        windows.screen.blit(label, (200, 100))
        label2 = pygame.font.SysFont("", 66).render(f"Your score: {resultat}", 1, (51, 255, 51))
        windows.screen.blit(label2, (180, 370))
        label3 = pygame.font.SysFont("", 66).render(f"High score: {high_resultat}", 1, (255, 0, 0))
        windows.screen.blit(label3, (180, 420))

        windows.buttons(150, 500, (255, 255, 255), "RESTART", 160, 50)
        windows.buttons(420, 500, (255, 255, 255), "QUIT", 110, 50)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 150 < mouse[0] < 310 and 500 < mouse[1] < 550:
            windows.buttons(150, 500, (153, 255, 255), "RESTART", 160, 50)
            if click[0] == 1:
                run()
        if 420 < mouse[0] < 530 and 500 < mouse[1] < 550:
            windows.buttons(420, 500, (153, 255, 255), "QUIT", 110, 50)
            if click[0] == 1:
                pygame.quit()
                quit()
        pygame.display.update()
        command = pygame.event.poll()
        if command.type == pygame.QUIT:
            pygame.quit()
            quit()


run()


"start counting after press letsgo"