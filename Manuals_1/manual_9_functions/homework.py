# ДЗ
# Написать функцию, которая будет складывать все значения из списка в одну строку.
# На вход функция должна принимать список, а возвращать строку.

def change(arr):
    line = ''
    for elem in arr:
        line = line + str(elem)
    return line


numbers = [2, 4, 6, 2, 42, 4, 765, 34, 47, 547, 425, 547, 547]
ans = change(numbers)
print(ans)
print(change(['1231', '2133', '14 13', 'fsd sd', 'first']))
