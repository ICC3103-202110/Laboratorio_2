from random import shuffle
from card import Card


class Board:

    MAX_NUMBER_OF_CARDS = 32
    MIN_NUMBER_OF_CARDS = 6

    def __init__(self, max_cards):
        self.cards = self.__create_cards(list(range(1, max_cards+1)))
        self.grid = self.__create_grid()

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        self.__cards = cards

    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, grid):
        self.__grid = grid

    # Public Methods

    def exists_non_discovered_cards(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if not self.grid[row][col].discovered:
                    return True
        return False

    def check_last_move(self, selected_coords):
        if (
            self.grid[selected_coords[0][0]][selected_coords[0][1]].value
            ==
            self.grid[selected_coords[1][0]][selected_coords[1][1]].value
        ):
            return True
        return False

    def remove_cards(self, selected_coords):
        self.grid[selected_coords[0][0]][selected_coords[0][1]].discovered = True
        self.grid[selected_coords[1][0]][selected_coords[1][1]].discovered = True

    def show_card(self, coords):
        self.grid[coords[0]][coords[1]].hidden = False

    def hide_card(self, coords):
        self.grid[coords[0]][coords[1]].hidden = True

    # Private Methods

    def __create_cards(self, cards_values):
        if len(cards_values) < self.MIN_NUMBER_OF_CARDS:
            cards_values = list(range(1, self.MIN_NUMBER_OF_CARDS+1))
        if len(cards_values) > self.MAX_NUMBER_OF_CARDS:
            cards_values = list(range(1, self.MAX_NUMBER_OF_CARDS+1))

        cards = []
        for card_value in cards_values:
            cards.append(Card(card_value))
            cards.append(Card(card_value))

        return cards

    def __create_grid(self):
        number_of_rows, number_of_cols = self.__get_rows_and_cols()
        cards = self.cards.copy()
        shuffle(cards)
        grid = []
        for row in range(number_of_rows):
            grid.append([])
            for col in range(number_of_cols):
                grid[row].append(cards.pop())
        return grid

    def __get_rows_and_cols(self):
        total_blocks = len(self.cards)
        rows_cols = [int(total_blocks/2), 2]
        cols = 3
        while rows_cols[0] > cols:
            if total_blocks % cols == 0:
                rows_cols = [int(total_blocks/cols), cols]
            cols += 1
        return rows_cols

    def __str__(self):
        str_grid = ''
        for row in range(len(self.grid)):
            row_elements = []
            for col in range(len(self.grid[0])):
                if (
                    self.grid[row][col].hidden and
                    not self.grid[row][col].discovered
                ):
                    row_elements.append(
                        str(self.grid[row][col]).format(row, col).center(7)
                    )
                else:
                    row_elements.append(str(self.grid[row][col]))
            str_grid += ' '.join(row_elements) + '\n'

        return str_grid
