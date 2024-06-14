import socket


# создаем главный сокет socket.AF_INET - семейство адресов IPv4, socket.SOCK_STREAM - протокол TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# отключаем пакетирование
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
# связываем сокет с конкретным портом (IP-адрес и порт)
sock.connect(("localhost", 10000))

# чтение стихотворения из файла
text = ''

# открываем файл
with open('text.txt', 'r', encoding='UTF-8') as file:
    # читаем все строки
    lines = file.readlines()
    # перебор строк
    for line in lines:
        text += line

# храним прочитанное стихотворение в кортеже
poem = tuple(text.split('\n'))

# кол-во строк
poem_len = len(poem)
i = 0

# отправка строк стихотворения
while True:
    # отправка сообщения
    sock.send(poem[i % poem_len].encode())
    i += 1

    # прием сообщений и синхронизация с сервером
    data = sock.recv(1024).decode()
    print('Получено ', data)
