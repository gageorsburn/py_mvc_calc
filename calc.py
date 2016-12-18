class Calculate:

    """A simple calculator class"""

    def __init__(self):
        self.__result = 0
        self.__number = 0
        self.__operation = Operation.none

    def add(self):
        self.__result += self.__number

    def subtract(self):
        self.__result -= self.__number

    def multiply(self):
        self.__result *= self.__number

    def divide(self):
        self.__result /= self.__number

    def append(self, value):
        if self.__operation == Operation.none:
            self.__result = int(str(self.__result) + str(value))
            self.set_output(self.__result)
        else:
            self.__number = int(str(self.__number) + str(value))
            self.set_output(self.__number)

    def set_operation(self, value):
        self.__operation = Operation(value)

    def do_operation(self):
        if self.__operation == Operation.add:
            self.add()
        elif self.__operation == Operation.subtract:
            self.subtract()
        elif self.__operation == Operation.multiply:
            self.multiply()
        elif self.__operation == Operation.divide:
            self.divide()

        self.__number = 0

        self.set_output(self.__result)

    def get_result(self):
        return self.__result

    def clear(self):
        self.__result = 0
        self.__number = 0
        self.__operation == Operation.none
        self.set_output(0)

    def set_output(self, value):
        print('calc:set_output: ' + str(value))

from enum import Enum

class Operation(Enum):
    none = 0
    add = 1
    subtract = 2
    multiply = 3
    divide = 4
