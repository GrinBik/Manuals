import tkinter


def test():
    text.destroy()


root = tkinter.Tk()

root.geometry("600x400")
root.title("Окошко")
root["bg"] = 'green'

text = tkinter.Label(root, text="Привет, Мир!", font=("Consolas", 32, "bold"), fg="white", bg="dark blue")
text.pack()

text.destroy()
text = tkinter.Label(root, text="𓁈𓂀𓋹𓆣𓁀𓀾", font=("Arial", 100, "bold"), fg="dark green", bg="green")
text.pack()

btn = tkinter.Button(root, text="Press me!", fg="tomato2", bg="navajowhite2",
                     activeforeground="tomato4", activebackground="navajowhite4", font=("Algerian", 35), command=test)
btn.pack()

# btn.place(x=95, y=0)

root.mainloop()
