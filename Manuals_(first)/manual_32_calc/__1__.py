import tkinter


class Calculator:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("375x667")
        self.window.resizable(None, None)
        self.window.title("Калькулятор")
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = "0"
        self.current_expression = "0"
        self.total_label, self.label = self.create_display_labels()

        self.digits = {7: (1, 1), 8: (1, 2), 9: (1, 3),
                       4: (2, 1), 5: (2, 2), 6: (2, 3),
                       1: (3, 1), 2: (3, 2), 3: (3, 3),
                       0: (4, 2), '.': (4, 1)}

        self.operations = {"/": "/", "*": "*", "-": "-", "+": "+"}

        self.create_digit_buttons()
        self.create_operator_buttons()

    def run(self):
        self.window.mainloop()

    def create_display_frame(self):
        frame = tkinter.Frame(self.window, height=221, bg="lightgrey")
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tkinter.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tkinter.Label(self.display_frame,
                                    text=self.total_expression, anchor=tkinter.E,
                                    bg="lightgrey", fg="black",
                                    padx=24, font=("Arial", 16))
        total_label.pack(expand=True, fill="both")

        label = tkinter.Label(self.display_frame,
                              text=self.current_expression, anchor=tkinter.E,
                              bg="lightgrey", fg="black",
                              padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tkinter.Button(self.buttons_frame,
                                    text=str(digit), bg="white", fg="black",
                                    font=("Arial", 24, "bold"), borderwidth=0)
            button.grid(row=grid_value[0],
                        column=grid_value[1], sticky=tkinter.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tkinter.Button(self.buttons_frame,
                                    text=symbol, bg="white", fg="black",
                                    font=("Arial", 24, "bold"), borderwidth=0)
            button.grid(row=i, column=4, sticky=tkinter.NSEW)
            i += 1


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
