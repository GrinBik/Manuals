from tkinter import *


root = Tk()
root.geometry('800x600')
root.title('Сетка')

empty_label = Label(root, text='тест', font=(None, 30))
empty_label.grid(row=0, column=0)

btn = Button(root, text='пупсик', font=(None, 15))
btn.grid(row=1, column=2)
root.mainloop()
