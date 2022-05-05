import pygame
import time


background_image = pygame.image.load('image/roads4.png')
screen = pygame.display.set_mode(background_image.get_size())


def buttons(xpos, ypos, colour, text, width, height):
    pygame.draw.rect(screen, colour, (xpos, ypos, width, height))
    msg = pygame.font.SysFont("", 36).render(text, True, (0, 0, 0))
    screen.blit(msg, (xpos + 25, ypos + 12))


def start(score):
    while (1):
        screen.blit(background_image, (0, 0))
        label = pygame.font.SysFont("", 66).render("click below to start", 1, (255, 255, 255))
        screen.blit(label, (150, 450))
        buttons(270, 530, (255, 255, 255), "LETS GO!!", 170, 50)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        key = pygame.key.get_pressed()
        if 270 < mouse[0] < 420 and 530 < mouse[1] < 580:
            buttons(270, 530, (153, 255, 255), "LETS GO!!", 170, 50)
            if (click[0] == 1) or (click[0] == 1 and key[pygame.K_s]):
                score.starting_time = time.time()
                # for i in range(5, 0, -1):
                #     label = pygame.font.SysFont("", 100).render(f"{i}", 1, (255, 255, 255))
                #     screen.blit(label, (300, 300))
                #     pygame.display.update()
                #     time.sleep(1)
                return 1
        pygame.display.update()
        command = pygame.event.poll()
        if (command.type == pygame.KEYDOWN):
            if (command.key == pygame.K_RETURN):
                return 1
        if command.type == pygame.QUIT:
            pygame.quit()
            quit()
