import tkinter


root = tkinter.Tk()

root.geometry("600x400")
root.title("Окошко")
root["bg"] = 'green'

text = tkinter.Label(root, text="𓁈𓂀𓋹𓆣𓁀𓀾", font=("Arial", 100, "bold"), fg="dark green", bg="green")
text.pack()

root.mainloop()
