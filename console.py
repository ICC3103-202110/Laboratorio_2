import os


class Console:

    @staticmethod
    def get_int_input(message):
        return int(input(message))

    @staticmethod
    def get_str_input(message):
        return input(message)

    @staticmethod
    def get_str_input_with_args(message, args):
        return input(message.format(*args))

    @staticmethod
    def print_str(message):
        print(message)

    @staticmethod
    def print_str_with_args(message, args):
        print(message.format(*args))

    @staticmethod
    def clear():
        os.system('cls||clear')
