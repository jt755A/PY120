# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import random
import os

def clear_screen():
    os.system('clear')

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.score = 0

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)


class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)


class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"


    def __init__(self, marker= " "):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    CENTER_SQUARE = 5
    SQUARES_IN_BOARD = 9

    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = {key: Square()
                        for key in range(1, Board.SQUARES_IN_BOARD + 1)}


    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}  |")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}  |")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}  |")
        print("     |     |")
        print()


    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def is_full(self):
        unused_squares = self.unused_squares()
        return len(unused_squares) == 0

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
    )

    WINNING_SCORE = 3

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.first_player = self.human

    def play(self):
        self.display_welcome_message()

        while True:
            self.play_one_game()
            if self.is_match_over():
                break
            if not self.play_again():
                break

            print("Let's play again!")
            print()

            self.first_player = self.toggle_player(self.first_player)

        self.display_match_winner()
        self.display_goodbye_message()

    def play_one_game(self):
        current_player = self.first_player

        self.board.reset()
        self.board.display()
        self.display_current_score()

        while True:
            self.player_moves(current_player)
            # self.human_moves()
            if self.is_game_over():
                break


            # self.computer_moves()s
            # if self.is_game_over():
            #     break

            self.board.display_with_clear()
            current_player = self.toggle_player(current_player)


        self.board.display_with_clear()
        self.display_results()
        self.increment_score()
        self.display_current_score()


    def play_again(self):
        options = ('y', 'n')
        choice = input("Would you like to play another game? (y/n) ").casefold()
        while choice not in options:
            choice = input("Sorry, that's not a valid choice. "
            "Please choose (y/n) to play again").casefold()

        clear_screen()
        return choice.startswith('y')

    def display_current_score(self):
        print(f'Current score = Human: {self.human.score} | '
              f'Computer: {self.computer.score}')

    def increment_score(self):
        if self.is_winner(self.human):
            self.human.score += 1
        elif self.is_winner(self.computer):
            self.computer.score += 1
        else:
            pass

    def display_welcome_message(self):
        clear_screen()
        print('Welcome to Tic Tac Toe!')
        print()

    def display_goodbye_message(self):
        print('Thanks for playing Tic Tac Toe! Goodbye!')

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("Computer wins...")
        else:
            print("It's a tie!")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def display_match_winner(self):
        human_score = self.human.score
        computer_score = self.computer.score
        print()

        if human_score > computer_score:
            print('You are the winner')
        elif computer_score > human_score:
            print('Computer wins! Better luck next time.')
        else:
            print("The match is tied!")

    def toggle_player(self, player):
        return self.computer if player == self.human else self.human

    def player_moves(self, current_player):
        if current_player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def human_moves(self):
        valid_choices = self.board.unused_squares()
        while True:
            printable_choices = TTTGame._join_or(valid_choices)
            prompt = f"Choose a square ({printable_choices}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = self.computer_offense_defense_move(self.computer)
        if not choice:
            choice = self.computer_offense_defense_move(self.human)

        if not choice:
            # pick square 5 if it's available
            if self.board.squares[Board.CENTER_SQUARE].is_unused():
                choice = Board.CENTER_SQUARE

        if not choice:
            valid_choices = self.board.unused_squares()
            choice = random.choice(valid_choices)

        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def is_match_over(self):
        return (self.human.score == TTTGame.WINNING_SCORE or
                self.computer.score == TTTGame.WINNING_SCORE)

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def two_in_a_row(self, player, row):
        # this could be used to alert the player if the computer has 2
        # in a row?
        return self.board.count_markers_for(player, row) == 2

    def empty_square(self, row):
        for key in row:
            if key in self.board.unused_squares():
                return key

        return None

    def computer_offense_defense_move(self, winning_player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.two_in_a_row(winning_player, row) and self.empty_square(row):
                return self.empty_square(row)

        return None

    def someone_won(self):
        return (self.is_winner(self.human) or
               self.is_winner(self.computer))

    @staticmethod
    def _join_or(choices, separator=", ", conjunction="or"):
        if len(choices) == 1:
            return str(choices[0])
        if len(choices) == 2:
            return f"{choices[0]} {conjunction} {choices[1]}"

        last = choices[-1]
        initial = choices[:-1]
        initial = [str(choice) for choice in initial]
        prompt = separator.join(initial)
        return f"{prompt}{separator}{conjunction} {last}"

game = TTTGame()
game.play()
