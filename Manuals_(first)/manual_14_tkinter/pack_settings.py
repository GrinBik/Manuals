import tkinter


root = tkinter.Tk()
root.geometry()
for e, expand in enumerate([False, True]):
    for f, fill in enumerate([None, tkinter.X, tkinter.Y, tkinter.BOTH]):
        for s, side in enumerate([tkinter.TOP, tkinter.LEFT, tkinter.BOTTOM, tkinter.RIGHT]):
            position = '+{}+{}'.format(s * 205 + e * 820, f * 235)
            win = tkinter.Toplevel(root)
            win.geometry('200x200' + position)
            text = str("side='{}'\nfill='{}'\nexpand={}".format(side, fill, str(expand)))
            tkinter.Label(win, text=text, bg=['#FF5555', '#55FF55'][e]).pack(side=side, fill=fill, expand=expand)

root.mainloop()
