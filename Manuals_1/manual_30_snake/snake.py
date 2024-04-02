import pygame
import menu
import random


def disable():
    global state
    main_menu.disable()
    state = "game"
    bg.play(loops=-1)


def eating_check(xcor, ycor, food_X, food_Y):
    if food_X - snake_block <= xcor <= food_X + snake_block:
        if food_Y - snake_block <= ycor <= food_Y + snake_block:
            eat.play()
            return True
    else:
        return False


def loose():
    label.set_title(f"Счёт: {length - 1}")
    play_btn.set_title('Играть')
    new_game()
    main_menu.enable()
    bg.stop()
    game_over.play()


def new_game():
    global x1_change, y1_change, length, x1, y1
    global food_x, food_y
    x1_change = 0
    y1_change = 0
    length = 1
    snake_list.clear()
    x1 = WIDTH // 2
    y1 = HEIGHT // 2
    food_x = random.randrange(0, WIDTH - snake_block)
    food_y = random.randrange(0, HEIGHT - snake_block)


def create_mes(msg, color, x, y, font, size):
    font_style = pygame.font.SysFont(font, size)
    mes = font_style.render(msg, True, color)
    screen.blit(mes, [x, y])


def change_difficulty(value):
    global FPS
    FPS = 5 * value


pygame.init()

WIDTH = 800
HEIGHT = 600

FPS = 5
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

state = "menu"

snake_list = []
x1 = WIDTH // 2
y1 = HEIGHT // 2
snake_block = 30
snake_step = 30
x1_change = 0
y1_change = 0
length = 1

food_x = random.randrange(0, WIDTH - snake_block)
food_y = random.randrange(0, HEIGHT - snake_block)

main_menu = menu.Menu(screen)
label = main_menu.add.label(f"Счёт: {length - 1}")
label_id = label.get_id()
play_btn = main_menu.add.button('Играть', disable)
slider = main_menu.add.range_slider("Сложность", 1, (1, 2, 3, 4, 5), onchange=change_difficulty)
main_menu.add.button('Выход', quit)

bg = pygame.mixer.Sound("music/background.mp3")
bg.set_volume(0.3)
eat = pygame.mixer.Sound("music/eat.mp3")
game_over = pygame.mixer.Sound("music/gameover.mp3")
wall = pygame.mixer.Sound("music/wall.wav")
wall.set_volume(0.3)

run = True

while run:
    clock.tick(FPS)
    screen.fill("white")
    create_mes(f"Счёт: {length - 1}", "black", 0, 0, "Comic Sans", 25)

    pygame.draw.rect(screen, "green", [food_x, food_y, snake_block, snake_block])

    snake_head = [x1, y1]
    
    if x1 <= -snake_block or x1 >= WIDTH + snake_block or y1 <= -snake_block or y1 >= HEIGHT + snake_block:
        wall.play()
        loose()

    snake_list.append(snake_head)
    for x in snake_list:
        pygame.draw.rect(screen, "black", [x[0], x[1], snake_block, snake_block])
    if len(snake_list) > length - 1:
        del snake_list[0]

    if eating_check(x1, y1, food_x, food_y):
        food_x = random.randrange(0, WIDTH - snake_block)
        food_y = random.randrange(0, HEIGHT - snake_block)
        length += 1

    for x in snake_list[:-1]:
        if x == snake_head:
            loose()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                state = "menu"
                main_menu.enable()
                bg.stop()
                x1_change = 0
                y1_change = 0
            elif event.key == pygame.K_LEFT:
                x1_change = -snake_step
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_step
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_step
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_step

    x1 += x1_change
    y1 += y1_change

    main_menu.flip(events)
    pygame.display.flip()

pygame.quit()

# ДЗ
# Реализовать звуковой эффект столкновения змейки со стеной.
# Чем больше FPS, тем быстрее идёт игра. Пусть ползунок сложности меняет FPS и, в соответствии, сложность игры.
