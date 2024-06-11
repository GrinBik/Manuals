import socket
import time

# настраиваем главный сокет
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# отключаем пакетирование
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

# установка IP-адреса и порта (соединение)
main_socket.bind(("localhost", 10000))

# не закрывать данный сокет после соединения
main_socket.setblocking(False)

# кол-во одновременно слушаемых игроков
main_socket.listen(5)

print("Сокет готов")

# список игроков
players = []

# сервер должен работать постоянно
while True:
    try:
        # принимаем входящие запросы: new_socket - подключение (сокет клиента), addr - клиент (его id)
        new_socket, addr = main_socket.accept()
        print('Подключился', addr)
        # не закрывать данный сокет после соединения
        new_socket.setblocking(False)
        # добавляем сокет нового игрока в список
        players.append(new_socket)
    except BlockingIOError:
        pass

    # читаем команды игроков
    for sock in players:
        try:
            # 1024 - это кол-во получаемых данных, которые декодируем из байтов в строку
            data = sock.recv(1024).decode()
            print("Получено сообщение: ", data)
        except:
            pass

    # приостановим работу программы
    time.sleep(1)
