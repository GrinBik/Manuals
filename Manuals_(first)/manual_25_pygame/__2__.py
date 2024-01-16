import pygame


pygame.init()

WIDTH = 480
HEIGHT = 360

# https://colorpicker.me/#aaf0d1
RGB_color = (0, 0, 0)
HEX_color = "#aaf0d1"
name_color = "MediumOrchid"

FPS = 100
clock = pygame.time.Clock()

posX = 20
posY = 20
speed = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шаблон")

run = True

while run:
    clock.tick(FPS)
    screen.fill(RGB_color)

    pygame.draw.rect(screen, "White", (posX, posY, 30, 30))

    for event in pygame.event.get():
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
            elif event.key == pygame.K_r:
                RGB_color = (RGB_color[0] + 1, RGB_color[1], RGB_color[2])
            elif event.key == pygame.K_g:
                RGB_color = (RGB_color[0], RGB_color[1] + 1, RGB_color[2])
            elif event.key == pygame.K_b:
                RGB_color = (RGB_color[0], RGB_color[1], RGB_color[2] + 1)

    pygame.display.flip()

pygame.quit()

# ДЗ
# Необходимо модернизировать программу таким образом, чтобы с помощью клавиш r, g, b - плавно менять цвет фона окна.
