# Написать клиентскую программу, которая будет отправлять на сервер строчки из стихотворения Пушкина
import socket
import time


# настраиваем клиентский сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# отключаем пакетирование
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

# установка IP-адреса и порта (соединение)
sock.connect(("localhost", 10000))

# чтение стихотворения из файла
# переменная для хранения прочитанного
temp = []
# открываем файл
with open('text.txt', 'r', encoding='UTF-8') as file:
    # читаем все строки
    lines = file.readlines()
    # перебор строк
    for line in lines:
        # удаление последнего элемента переноса на новую строку
        line = line.replace('\n', '')
        # добавляем во временную переменную temp
        temp.append(line)
# храним прочитанное стихотворение в кортеже
poem = tuple(temp)
# удаление temp за ненадобностью
del temp

# кол-во строк
length = len(poem)
i = 0

# отправка сообщений пользователем постоянно
# encode - кодирует сообщения (преобразовывает) в байты
while True:
    # отправка сообщения
    sock.send(poem[i % length].encode())
    i += 1
    # заморозка выполнения на то же время, чот и на сервере!
    time.sleep(5)
