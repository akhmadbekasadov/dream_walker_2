import pygame

background_image = pygame.image.load('image/roads4.png')
screen = pygame.display.set_mode(background_image.get_size())


def buttons(xpos, ypos, colour, text, width, height):
    pygame.draw.rect(screen, colour, (xpos, ypos, width, height))
    msg = pygame.font.SysFont("", 36).render(text, True, (0, 0, 0))
    screen.blit(msg, (xpos + 25, ypos + 12))


def start():
    while (1):
        screen.blit(background_image, (0, 0))
        label = pygame.font.SysFont("", 66).render("click below to start", 1, (255, 255, 255))
        screen.blit(label, (150, 450))
        buttons(270, 530, (255, 255, 255), "LETS GO!!", 170, 50)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 270 < mouse[0] < 420 and 530 < mouse[1] < 580:
            buttons(270, 530, (153, 255, 255), "LETS GO!!", 170, 50)
            if click[0] == 1:
                return 1
        pygame.display.update()
        command = pygame.event.poll()
        if (command.type == pygame.KEYDOWN):
            if (command.key == pygame.K_RETURN):
                return 1
        if command.type == pygame.QUIT:
            pygame.quit()
            quit()


def gameover(resultat, high_resultat):
    while (1):
        screen.blit(background_image, (0, 0))

        label = pygame.font.SysFont("", 66).render("Sweet dreams!", 1, (153, 255, 255))
        screen.blit(label, (200, 100))
        label2 = pygame.font.SysFont("", 66).render(f"Your score: {resultat}", 1, (51, 255, 51))
        screen.blit(label2, (180, 370))
        label3 = pygame.font.SysFont("", 66).render(f"High score: {high_resultat}", 1, (255, 0, 0))
        screen.blit(label3, (180, 420))

        buttons(150, 500, (255, 255, 255), "RESTART", 160, 50)
        buttons(420, 500, (255, 255, 255), "QUIT", 110, 50)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (150 < mouse[0] < 310 and 500 < mouse[1] < 550):
            buttons(150, 500, (153, 255, 255), "RESTART", 160, 50)
            if click[0] == 1:
                return 1
        if (420 < mouse[0] < 530 and 500 < mouse[1] < 550):
            buttons(420, 500, (153, 255, 255), "QUIT", 110, 50)
            if click[0] == 1:
                pygame.quit()
                quit()

        pygame.display.update()
        command = pygame.event.poll()
        if command.type == pygame.QUIT:
            pygame.quit()
            quit()
