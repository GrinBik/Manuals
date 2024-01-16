# ДЗ
# Разместить 4 кнопки в середине экрана.
# При их создании - случайная из них выбирается правильной. При нажатии на правильную появляется текст «Ты угадал!».
# При нажатии на неправильную — удаляются все неправильные кнопки и появляется текст «Ты не угадал >:( »
import tkinter
from random import shuffle


def winner():
    message['text'] = 'Ты угадал!'


def lose():
    message['text'] = 'Ты не угадал >:('
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()


root = tkinter.Tk()
root.geometry('800x600')
root['bg'] = 'aqua'
root.title('Выбор')

button_names = ['Кнопка 1', 'Кнопка 2', 'Кнопка 3', 'Кнопка 4']
shuffle(button_names)

btn1 = tkinter.Button(root, text=button_names[0], font=('Arial', 15), command=winner)
btn2 = tkinter.Button(root, text=button_names[1], font=('Arial', 15), command=lose)
btn3 = tkinter.Button(root, text=button_names[2], font=('Arial', 15), command=lose)
btn4 = tkinter.Button(root, text=button_names[3], font=('Arial', 15), command=lose)

message = tkinter.Label(root, text='test', font=('Arial', 30), bg='aqua', fg='black')

buttons = [btn1, btn2, btn3, btn4]
shuffle(buttons)

message.pack(side=tkinter.TOP, fill=tkinter.X)
buttons[0].pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
buttons[1].pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
buttons[2].pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)
buttons[3].pack(side=tkinter.LEFT, fill=tkinter.X, expand=True)

root.mainloop()
