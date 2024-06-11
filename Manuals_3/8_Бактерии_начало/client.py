import socket


# настраиваем клиентский сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# отключаем пакетирование
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

# установка IP-адреса и порта (соединение)
sock.connect(("localhost", 10000))

# отправка сообщений пользователем постоянно
# encode - кодирует сообщения (преобразовывает) в байты
while True:
    # отправка сообщения
    sock.send("Привет, как дела?\nУ меня все хорошо!".encode())
    # заморозка выполнения на то же время, чот и на сервере!
