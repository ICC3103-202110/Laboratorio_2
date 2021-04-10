class Player:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.score = 0
        self.selected_coords = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score >= 0:
            self.__score = score
        else:
            self.__score = 0

    @property
    def selected_coords(self):
        return self.__selected_coords

    @selected_coords.setter
    def selected_coords(self, selected_coords):
        self.__selected_coords = selected_coords
