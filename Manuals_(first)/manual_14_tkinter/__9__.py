import tkinter


def test():
    label_a = tkinter.Label(root, text="Label A", bg="yellow")
    label_b = tkinter.Label(root, text="Label B", bg="orange")
    label_c = tkinter.Label(root, text="Label C", bg="red")
    label_d = tkinter.Label(root, text="Label D", bg="light green")
    label_e = tkinter.Label(root, text="Label E", bg="blue")

    #  и разместим их по такой вот сетке
    label_a.grid(row=0, column=0)
    label_b.grid(row=1, column=0)
    label_c.grid(row=0, column=1)
    label_d.grid(row=0, column=2)
    label_e.grid(row=2, column=0)


root = tkinter.Tk()

root.geometry("600x400")
root.title("Окошко")
root["bg"] = 'green'

btn = tkinter.Button(root, text="Press me!", font=("Algerian", 35), command=test)
btn.grid(row=3, column=3)

new_btn = tkinter.Button(root, text="new", font=("Algerian", 35), command=test)
new_btn.grid(row=1, column=3, rowspan=2, columnspan=3)

root.mainloop()
