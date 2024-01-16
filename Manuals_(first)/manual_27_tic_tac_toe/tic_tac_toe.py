import menu
import pygame


def set_side(_, side):
    global player_side, comp_side
    if side:
        player_side = "x"
        comp_side = "o"
    else:
        comp_side = "x"
        player_side = "o"


def draw_grid():
    for n in range(0, 4):
        pygame.draw.line(screen, "black", (n * STEP_X, 0), (n * STEP_X, HEIGHT), 3)
    for n in range(0, 4):
        pygame.draw.line(screen, "black", (0, n * STEP_Y), (WIDTH, n * STEP_Y), 3)


def disable():
    global state
    main_menu.disable()
    state = "game"


def draw_tic_tac_toe():
    for i in range(3):
        for j in range(3):
            if field[i][j] == "x":
                pygame.draw.line(screen, "black", (j * STEP_X, i * STEP_Y),
                                 (j * STEP_X + STEP_X, i * STEP_Y + STEP_Y), 3)
                pygame.draw.line(screen, "black", (j * STEP_X + STEP_X, i * STEP_Y),
                                 (j * STEP_X, i * STEP_Y + STEP_Y), 3)
            elif field[i][j] == "o":
                pygame.draw.circle(screen, 'black', (j * STEP_X + 0.5 * STEP_X, i * STEP_Y + 0.5 * STEP_Y),
                                   min(0.5 * STEP_X, 0.5 * STEP_Y), 3)


pygame.init()

WIDTH = 600
HEIGHT = 600

STEP_X = WIDTH // 3
STEP_Y = HEIGHT // 3

FPS = 90
clock = pygame.time.Clock()

field = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player_side = "x"
comp_side = "o"

state = "menu"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики - Нолики")

main_menu = menu.Menu(screen)
main_menu.add.selector('Сторона :', [('Крестики', True), ('Нолики', False)], onchange=set_side)
main_menu.add.button('Играть', disable)
main_menu.add.button('Выход', quit)

run = True

while run:
    clock.tick(FPS)
    screen.fill('white')
    draw_grid()
    draw_tic_tac_toe()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                state = "menu"
                main_menu.enable()
        elif event.type == pygame.MOUSEBUTTONDOWN and state == "game":
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 200][pos[0] // 200] == "":
                field[pos[1] // 200][pos[0] // 200] = player_side

    main_menu.flip(events)
    pygame.display.flip()

pygame.quit()

# ДЗ
# Добавить отрисовку нолика в поле. Проверить код, выбрав в меню сторону «Нолики».
