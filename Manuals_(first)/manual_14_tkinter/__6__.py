import tkinter


def test():
    text.destroy()


root = tkinter.Tk()

root.geometry("600x400")
root.title("Окошко")
root["bg"] = 'green'

text = tkinter.Label(root, text="Привет, Мир!", font=("Consolas", 32, "bold"), fg="white", bg="darkblue")
text.pack()

btn = tkinter.Button(root, text="Press me!", font=("Algerian", 35), command=test)
btn.pack()

root.mainloop()
