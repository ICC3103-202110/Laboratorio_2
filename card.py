class Card:

    def __init__(self, value):
        self.__value = value
        self.discovered = False
        self.hidden = True

    @property
    def value(self):
        return self.__value

    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden):
        self.__hidden = hidden

    @property
    def discovered(self):
        return self.__discovered

    @discovered.setter
    def discovered(self, discovered):
        self.__discovered = discovered

    def __str__(self):
        if self.discovered:
            string = ' '
            return string.center(7)
        elif self.hidden:
            return '({},{})'
        else:
            return str(self.value).center(7)
