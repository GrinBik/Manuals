import menu
import pygame
import random


def set_side(_, side):
    global player_side, comp_side
    if side:
        player_side = "x"
        comp_side = "o"
    else:
        comp_side = "x"
        player_side = "o"
    reset()


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


def comp_step():
    while True:
        row, column = random.randint(0, 2), random.randint(0, 2)
        if field[row][column] != "":
            continue
        else:
            field[row][column] = comp_side
            break


def win_check():
    global game_over
    win = ()
    for side in "xo":
        for row in field:
            if row.count(side) == 3:
                row = field.index(row)
                win = ((0, row), (1, row), (2, row))
        for column in range(3):
            if field[0][column] == field[1][column] == field[2][column] == side:
                win = ((column, 0), (column, 1), (column, 2))
        if field[0][0] == field[1][1] == field[2][2] == side:
            win = ((0, 0), (1, 1), (2, 2))
        if field[0][2] == field[1][1] == field[2][0] == side:
            win = ((0, 2), (1, 1), (2, 0))
        if win != ():
            if side == player_side:
                pygame.display.set_caption("Победил игрок")
            else:
                pygame.display.set_caption("Победил компьютер")
            game_over = True
    return win


def draw_win(line):
    for x, y in line:
        pygame.draw.rect(screen, "green", (x * STEP_X, y * STEP_Y, STEP_X, STEP_Y))


def reset():
    global game_over, field, winner_line, empty_cells
    game_over = False
    field = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]
    winner_line = ()
    empty_cells = 9
    disable()


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

empty_cells = 9

state = "menu"
game_over = False

winner_line = ()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики - Нолики")

main_menu = menu.Menu(screen)
main_menu.add.selector('Сторона :', [('Крестики', True), ('Нолики', False)], onchange=set_side)
main_menu.add.button('Играть', disable)
main_menu.add.button('Переиграть', reset)
main_menu.add.button('Выход', quit)

run = True

while run:
    clock.tick(FPS)
    screen.fill('white')

    winner_line = win_check()
    draw_win(winner_line)

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
        elif event.type == pygame.MOUSEBUTTONDOWN and state == "game" and not game_over:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // 200][pos[0] // 200] == "":
                field[pos[1] // 200][pos[0] // 200] = player_side
                empty_cells -= 1
                if empty_cells > 1:
                    empty_cells -= 1
                    comp_step()

    main_menu.flip(events)
    pygame.display.flip()

pygame.quit()

# ДЗ
# Настроить программу так, чтобы при выигрыше пропадала возможность нажимать на экран и играть дальше.
