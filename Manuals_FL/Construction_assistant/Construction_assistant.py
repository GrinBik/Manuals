# Модуль time для замедления вывода результатов на консоль
from time import sleep


# Функция для запроса и проверки данных
def get_param(main_question, additional_parameters=False, additional_question=None):
    # Если возник дополнительный параметр (например, окно или дверь)
    while additional_parameters:
        answer = input(additional_question + ' (введите да или нет): ').lower()
        # Если дополнительный параметр подтвердился, то переходим к запросу его параметра
        if answer == "да":
            additional_parameters = False
        # Если дополнительный параметр не подтвердился, то прекращаем работу функции
        elif answer == 'нет':
            return
        # Обработка ответа на корректность
        else:
            print('Ошибка! Повторите ответ.')
    # Запрос значения параметра и проверка его значения на корректность
    param = 0.0
    # Цикл в качестве проверки на корректность
    while True:
        # Запрос значения параметра
        try:
            param = float(input(main_question + ' (в метрах): '))
            # Параметр с нулевым значением не существует
            if param == 0.0:
                print('Размер не может быть нулевым!')
                # Запрос значения параметра заново
                continue
            # Если все хорошо, то останавливаем цикл while
            break
        # Если пользователь ввел некорректные данные, то информируем его об этом и начинаем заново
        except ValueError:
            print('Некорректные данные, начните заново!')
            continue
    # Возвращаем параметр
    return param


# Приветствие программы
print('Вас приветствует программа "Помощник строителя".')
sleep(1)

# Запрос размеров ремонтируемого помещения
print('Введите размеры ремонтируемого помещения:')
sleep(0.5)
length = get_param('длина (в метрах)')
width = get_param('ширина (в метрах)')
height = get_param('высота (в метрах)')

# Общая площадь комнаты
room_area = (length + width) * 2 * height

sleep(2)

# Запрос ширины окна при ее наличии
window_width = get_param('Введите ширину окна',
                         True,
                         'Имеется ли в помещении окно?')
# Если окно существует, то необходима еще и высота окна
if window_width is not None:
    window_height = get_param('Введите высоту окна')
# Иначе параметры окна равны 0, чтобы никак не влияло на результат
else:
    window_width = 0.0
    window_height = 0.0

# Площадь окна
window_area = window_width * window_height

sleep(1)

# Запрос ширины двери при ее наличии
door_width = get_param('Введите ширину двери',
                       True,
                       'Имеется ли в помещении дверь?')
# Если дверь существует, то необходима еще и ее высота
if door_width is not None:
    door_height = get_param('Высота двери')
# Иначе параметры двери равны 0, чтобы никак не влияло на результат
else:
    door_width = 0.0
    door_height = 0.0

# Площадь двери
door_area = door_width * door_height

sleep(1)

# Выбор режима программы: "Поклейка обоев" или "Укладка плитки"
while True:
    print('''Выберите что требуется сделать (введите 1 или 2):
             1. Поклеить обои
             2. Положить плитку''')
    mode = input('Режим: ')
    # Если пользователь ввел не номер режима
    if mode not in ('1', '2'):
        print('Ошибка! Сделайте выбор еще раз!')
        sleep(1)
    else:
        break

# Режим "Поклейка обоев"
if mode == '1':
    wallpaper_width = get_param('Введите ширину обоев')
    wallpaper_length = get_param('Введите длину обоев')
    sleep(1)
    # Вычисление
    wallpaper_area = wallpaper_width * wallpaper_length
    result = (room_area - window_area - door_area) / wallpaper_area
    print(f'Вам потребуется {round(result)} кол-во рулонов.')
# Режим "Укладка плитки"
else:
    tile_width = get_param('Введите размер стороны квадратной плитки (в метрах)')
    tile_area = tile_width ** 2
    result = (room_area - window_area - door_area) / tile_area
    print(f'Вам потребуется {round(result)} шт плитки.')
    sleep(2)
