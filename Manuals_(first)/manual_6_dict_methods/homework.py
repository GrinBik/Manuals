# ДЗ
# Телефонная книга обновилась и теперь позволяет абонентам иметь в базе сразу несколько номеров,
# но код остался прежним. Необходимо улучшить код таким образом, чтобы у каждой фамилии мог быть не один номер.
# После чего вывести на консоль всех абонентов телефонной книги.

new_phone_book = {'Белозеров': ['+7 120 959 45 19'],
                  'Владимиров': ['+7 (342) 787-1717'],
                  'Симонов': ['+7 550 642 49 52'],
                  'Герасимова': ['+7 056 273 2478']}

new_phone_book["Владимиров"].append('+79175694884')
new_phone_book.pop("Герасимова")
last_name = input("Введите фамилию -> ")
print(f"Найден номер телефона: {new_phone_book[last_name]}")

print(list(new_phone_book.keys()))
