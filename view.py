import tkinter as tk
from functools import partial

class View:

    def __init__(self):
        self.window = tk.Tk()

    def init_components(self):
        self.init_output_label()
        self.init_number_buttons()
        self.init_clear_button()
        self.init_equal_button()
        self.init_operation_buttons()

    def number_event(self, value):
        print('view:number_event: ' + str(value))

    def clear_event(self):
        print('view:clear_event')

    def equal_event(self):
        print('view:equal_event')

    def operation_event(self, value):
        print('view:operation_event: ' + str(value))

    def set_output(self, value):
        print('view:set_output: ' +str(value))
        self.output.set(str(value))

    def init_number_buttons(self):
        row = 0
        column = 0

        for num in range(10):
            button = tk.Button(self.window, text=str(num), command=partial(self.number_event, num))

            if num % 3 == 0:
                row += 1
                column = 0
            else:
                column += 1

            button.grid(row=row, column=column)

    def init_clear_button(self):
        button = tk.Button(self.window, text="C", command=self.clear_event)
        button.grid(row=4, column=1)

    def init_equal_button(self):
        button = tk.Button(self.window, text="=", command=self.equal_event)
        button.grid(row=4, column=2)

    def init_output_label(self):
        self.output = tk.StringVar()
        self.output_label = tk.Label(self.window, textvariable=self.output, relief=tk.RAISED)
        self.output.set(str(0))
        self.output_label.grid(row=0, column=0, columnspan=10)

    def init_operation_buttons(self):
        add_button = tk.Button(self.window, text="+", command=partial(self.operation_event, 1))
        add_button.grid(row=1, column=3)

        subtract_button = tk.Button(self.window, text="-", command=partial(self.operation_event, 2))
        subtract_button.grid(row=2, column=3)

        multiply_button = tk.Button(self.window, text="*", command=partial(self.operation_event, 3))
        multiply_button.grid(row=3, column=3)

        divide_button = tk.Button(self.window, text="/", command=partial(self.operation_event, 4))
        divide_button.grid(row=4, column=3)
