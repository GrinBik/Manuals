# ДЗ
# Написать функцию, которая получает строку, разбивает её на слова и возвращает список из этих слов,
# записанных задом наперёд.

def rlist(line):
    # что точно известно и как можно было сделать ДЗ
    words = []
    current_word = ""
    for char in line:
        if char == ' ':
            words.append(current_word)
            current_word = ''
        elif char == ',':
            continue
        else:
            current_word += char
    words.append(current_word)
    # ИЛИ что оно же
    # можно сначала избавиться от возможных запятых
    line = line.replace(',', '')
    # разбиваем на список
    words = line.split(' ')
    # список для перевернутых слов
    reversed_words = []
    # переворачиваем слова
    for word in words:
        reversed_words.append(word[::-1])
    return reversed_words


arr = rlist('Привет, как дела?')
print(arr)
