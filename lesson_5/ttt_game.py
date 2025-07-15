import random

class Square:
    def __init__(self):
        # STUB
        # We need some way to keep track of this square's
        #   marker.
        pass

class Board:
    def __init__(self):
        # STUB
        # We need a way to model the 3x3 grid. Perhaps
        #   "squares"?
        # What data structure should we use? A list? A
        #   dictionary? Something else?
        # What should the data structure store? Strings?
        #   Numbers? Square objects?
        pass

class Row:
    def __init__(self):
        # STUB
        # We need some way to identify a row of 3 squares
        pass

class Player:
    def __init__(self, marker):
        # STUB
        # A player is either a human or a computer that is
        #   playing the game.
        # Perhaps we need a "marker" to keep track of this
        #   player's symbol? (i.e., 'X' or 'O')
        self.marker = marker

    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def play(self):
        # STUB
        # We need a way for each player to play the game.
        # Do we need access to the board?
        pass

class Human(Player):
    def __init__(self):
        # STUB
        # What does a human player need to do? How does it
        #   differ from the basic Player or a Computer?
        super().__init__(Square.HUMAN_MARKER)

        
class Computer(Player):
    def __init__(self):
        # STUB
        # What does a computer player need to do? How does
        #   it differ from the basic Player or a Human?
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

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

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

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker


class TTTGame:
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        # SPIKE
        self.display_welcome_message()

        while True:
            self.board.display()

            self.human_moves()
            self.board.display() # to see human's move
            if self.is_game_over():
                break

            self.computer_moves()
            self.board.display() # to see computer's move
            if self.is_game_over():
                break

            break # only executes loop once for now

        self.board.display()
        self.display_results()
        self.display_goodbye_message()

    def display_welcome_message(self):
        print('Welcome to Tic Tac Toe!')

    def display_goodbye_message(self):
        print('Thanks for playing Tic Tac Toe! Goodbye!')

    def display_results(self):
        # STUB
        # Show the results of this game (win, lose, tie).
        pass
    

    def human_moves(self):
        choice = None
        while True:
            choice = input("Choose a square between 1 and 9: ")
            try:
                choice = int(choice)
                if 1 <= choice <= 9:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)
        # Mark the chosen square with the human's marker.

    def computer_moves(self):
        choice = random.randint(1, 9)
        self.board.mark_square_at(choice, self.computer.marker)
              
    def is_game_over(self):
        # STUB
        # We'll start by assuming the game never ends.
        return False

game = TTTGame()
game.play()