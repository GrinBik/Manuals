import socket


# создаем главный сокет socket.AF_INET - семейство адресов IPv4, socket.SOCK_STREAM - протокол TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# отключаем пакетирование
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
# связываем сокет с конкретным портом (IP-адрес и порт)
sock.connect(("localhost", 10000))

# отправка команд от игрока
# encode - кодирует сообщения (преобразовывает) в байты
while True:
    # отправка команды
    sock.send("Хочу пойти направо".encode())
