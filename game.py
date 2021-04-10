from console import Console
from player import Player
from board import Board


class Game:

    MAX_NUMBER_OF_PLAYERS = 2
    __players = []
    __board = None
    __current_player = None

    @classmethod
    def play(cls):
        cls.__set_players()
        cls.__set_board()

        while cls.__board.exists_non_discovered_cards():
            for _ in range(3):
                cls.__player_play()
            if cls.__board.check_last_move(
                cls.__current_player.selected_coords
            ):
                cls.__board.remove_cards(
                    cls.__current_player.selected_coords
                )
                cls.__current_player.score += 1
            else:
                for coord in cls.__current_player.selected_coords:
                    cls.__board.hide_card(coord)
                cls.__current_player = (
                    cls.__players[0] if
                    cls.__current_player.number == 2 else
                    cls.__players[1]
                )
            cls.__current_player.selected_coords = []

        winner = cls.__get_winner()
        if winner:
            Console.print_str_with_args('The winner is {}!', [winner.name])
        else:
            Console.print_str('Draw!!!!')

    @classmethod
    def __set_players(cls):
        for i in range(1, cls.MAX_NUMBER_OF_PLAYERS + 1):
            name = Console.get_str_input_with_args(
                'Please enter player\'s {} name: ', [i]
            )
            cls.__players.append(Player(name, i))
        cls.__current_player = cls.__players[0]

    @classmethod
    def __set_board(cls):
        total_cards = Console.get_int_input(
            'Please enter the number of cards to play: '
        )
        cls.__board = Board(total_cards)

    @classmethod
    def __player_play(cls):
        Console.clear()
        Console.print_str_with_args(
            'Turn of player {}\n\n',
            [cls.__current_player.name]
        )
        Console.print_str(str(cls.__board))
        Console.print_str('\n\nPoints:')
        Console.print_str_with_args(
            '{}: {} | {}: {}\n',
            [
                cls.__players[0].name, cls.__players[0].score,
                cls.__players[1].name, cls.__players[1].score
            ]
        )
        if len(cls.__current_player.selected_coords) < 2:
            cls.__current_player.selected_coords.append(
                [
                    int(number) for number in Console.get_str_input(
                        'Select a card entering the '
                        'coords separeted by comma: '
                    ).split(',')
                ]
            )
            cls.__board.show_card(cls.__current_player.selected_coords[-1])
        else:
            Console.get_str_input('Press any key to continue...')

    @classmethod
    def __get_winner(cls):
        if cls.__players[0].score > cls.__players[1].score:
            return cls.__players[0]
        elif cls.__players[0].score < cls.__players[1].score:
            return cls.__players[1]
        else:
            return None


if __name__ == "__main__":
    Game.play()
