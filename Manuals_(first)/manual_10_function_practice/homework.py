# ДЗ
# Написать функцию, которая получает строку, разбивает её на слова и возвращает список из этих слов,
# записанных задом наперёд.

def rlist(line):
    words = []
    current_word = ""

    for char in line:
        if char == ' ':
            reversed_word = ''
            for i in current_word:
                reversed_word = i + reversed_word
            words.append(reversed_word)
            current_word = ""
        else:
            current_word += char

    if len(current_word) > 0:
        reversed_word = ''
        for i in current_word:
            reversed_word = i + reversed_word
        words.append(reversed_word)

    return words


print(rlist('Довод как довод'))
