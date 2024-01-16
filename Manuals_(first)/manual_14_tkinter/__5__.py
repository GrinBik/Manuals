import tkinter


root = tkinter.Tk()

root.geometry("600x400")
root.title("Окошко")
root["bg"] = 'green'

text = tkinter.Label(root, text="Привет, Мир!", font=("Consolas", 32, "bold"), fg="white", bg="darkblue")
text.pack()

btn = tkinter.Button(root, text="Press me!", fg="tomato2", bg="navajowhite2",
                     activeforeground="tomato4", activebackground="navajowhite4", font=("Algerian", 35))
btn.pack()

root.mainloop()
