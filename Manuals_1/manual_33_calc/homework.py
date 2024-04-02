# ДЗ
# Необходимо исключить тот случай, когда возникает деление на ноль, и вывести в калькулятор надпись «Error».
# Сделать кнопки возведения в степень и вычисления квадратного корня рабочими.
# Внедрить набор нового числа, если в текущем значении калькулятора отображается результат последнего вычисления.
import tkinter
import math


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
        self.create_clear_button()
        self.create_equals_button()
        self.create_sqrt_button()
        self.create_square_button()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.evaluate = False

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
                                    font=("Arial", 24, "bold"), borderwidth=0,
                                    command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0],
                        column=grid_value[1], sticky=tkinter.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tkinter.Button(self.buttons_frame,
                                    text=symbol, bg="white", fg="black",
                                    font=("Arial", 24, "bold"), borderwidth=0,
                                    command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tkinter.NSEW)
            i += 1

    def create_clear_button(self):
        button = tkinter.Button(self.buttons_frame, text="C", bg="white", fg="black",
                                font=("Arial", 20),
                                borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tkinter.NSEW)

    def create_equals_button(self):
        button = tkinter.Button(self.buttons_frame, text="=", bg="white",
                                fg="black", font=("Arial", 20), borderwidth=0,
                                command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tkinter.NSEW)

    def create_sqrt_button(self):
        button = tkinter.Button(self.buttons_frame, text="√x", bg="white",
                                fg="black", font=("Arial", 20),
                                borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tkinter.NSEW)

    def create_square_button(self):
        button = tkinter.Button(self.buttons_frame, text="x²", bg="white",
                                fg="black", font=("Arial", 20),
                                borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tkinter.NSEW)

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:9])

    def add_to_expression(self, value):
        if len(self.current_expression) == 9:
            return
        if (self.current_expression == '0' and value != '.') or self.evaluate:
            self.current_expression = str(value)
            self.evaluate = False
        else:
            self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        if self.current_expression == '0':
            return
        self.current_expression += operator

        if '√' in self.total_expression:
            self.total_expression = str(math.sqrt(int(self.total_expression[1:]))) + operator
            self.update_total_label()
            return
        elif '²' in self.total_expression:
            self.total_expression = str(int(self.total_expression[:-1])**2) + operator
            self.update_total_label()
            return
        if self.total_expression == '0':
            self.total_expression = self.current_expression
        else:
            self.total_expression += self.current_expression
        self.current_expression = "0"
        self.update_total_label()
        self.update_label()

    def evaluate(self):
        if self.total_expression == self.current_expression == '0':
            return
        if self.total_expression == '0':
            self.total_expression = self.current_expression
        else:
            if self.total_expression[-1] == '/' and self.current_expression == '0':
                self.total_expression = 'Error'
                self.current_expression = 'Error'
                self.update_total_label()
                self.update_label()
                return
            else:
                self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(self.total_expression))
        self.total_expression = "0"
        self.evaluate = True
        self.update_label()

    def clear(self):
        self.current_expression = "0"
        self.total_expression = "0"
        self.update_label()
        self.update_total_label()

    def sqrt(self):
        self.total_expression = '√' + self.current_expression
        self.update_total_label()
        self.current_expression = str(math.sqrt(float(self.current_expression)))
        self.update_label()
        self.evaluate = True

    def square(self):
        self.total_expression = self.current_expression + '²'
        self.update_total_label()
        self.current_expression = str(float(self.current_expression)**2)
        self.update_label()
        self.evaluate = True


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
