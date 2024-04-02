import menu
import pygame


pygame.init()

WIDTH = 480
HEIGHT = 360

# https://colorpicker.me/#aaf0d1
RGB_color = (255, 0, 255)
HEX_color = "#aaf0d1"
name_color = "MediumOrchid"

FPS = 100
clock = pygame.time.Clock()

posX = 20
posY = 20
speed = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шаблон")

main_menu = menu.Menu(screen)
main_menu.add.text_input('Name: ', default='GrinBik')
main_menu.add.button('Play', main_menu.disable)
main_menu.add.button('Exit', quit)

run = True

while run:
    clock.tick(FPS)
    screen.fill(RGB_color)

    pygame.draw.rect(screen, "White", (posX, posY, 30, 30))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posX -= speed
            elif event.key == pygame.K_RIGHT:
                posX += speed
            elif event.key == pygame.K_UP:
                posY -= speed
            elif event.key == pygame.K_DOWN:
                posY += speed
            elif event.key == pygame.K_m:
                main_menu.enable()

    main_menu.flip(events)
    pygame.display.flip()

pygame.quit()

# ДЗ
# Настроить тему меню по вкусу.
# Документация: https://pygame-menu.readthedocs.io/en/3.5.2/_source/themes.html
