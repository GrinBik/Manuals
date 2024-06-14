import socket
import time

# создаем главный сокет socket.AF_INET - семейство адресов IPv4, socket.SOCK_STREAM - протокол TCP
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# отключаем пакетирование
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
# связываем сокет с конкретным портом (IP-адрес и порт)
main_socket.bind(("localhost", 10000))
# чтобы программа не останавливалась пока ждет нового подключения, работала дальше
main_socket.setblocking(False)
# кол-во одновременных запросов на подключение
main_socket.listen(5)
print("Главный сокет готов")

# список игроков
players = []

# сервер должен работать постоянно
while True:
    # принимаем входящие запросы
    try:
        # new_socket - выделенный сокет (порт) игроку (новый), addr - адрес игрока
        new_socket, addr = main_socket.accept()
        # чтобы программа не останавливалась пока ждет команды от игрока, работала дальше
        new_socket.setblocking(False)
        # добавляем сокет нового игрока в список игроков
        players.append(new_socket)
        # вывод информации о подключившемся игроке
        print('Подключился ', addr)
    except BlockingIOError:
        pass

    # читаем команды игроков
    for sock in players:
        try:
            # 1024 - это кол-во получаемых данных, которые декодируем из байтов в строку
            data = sock.recv(34)
            data = data.decode()
            print("Получено: ", data)
        except:
            pass

    # приостановим работу программы
    time.sleep(1)
