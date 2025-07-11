import random

class Move:
    # methods for defeating another move?
    def __init__(self):
        self._defeats = ()    
        self.name = self.__class__.__name__
    
    def __str__(self):
        return self.__class__.__name__
    # pros and cons:
    pass

class Rock(Move):
    def __init__(self):
        super().__init__()
        self._defeats = ('lizard', 'scissors')
    
class Paper(Move):
    def __init__(self):
        super().__init__()
        self._defeats = ('rock', 'spock')

class Scissors(Move):
    def __init__(self):
        super().__init__()
        self._defeats = ('paper', 'lizard')

class Lizard(Move):
    def __init__(self):
        super().__init__()
        self._defeats = ('spock', 'paper')

class Spock(Move):
    def __init__(self):
        super().__init__()
        self._defeats = ('scissors', 'rock')

class Player:
    CHOICES = {'rock': Rock(), 'paper': Paper(), 'scissors': Scissors(), 'lizard': Lizard(), 'spock': Spock()}
    ABBRIEV_CHOICES = {'r': 'rock', 'p': 'paper', 'sc': 'scissors', 'l': 'lizard', 'sp': 'spock'}

    def __init__(self):
        self.move = None
        self.score = 0
        self.history = []

class Human(Player):
    def __init__(self):
        super().__init__()
        
    def choose(self):
        # Assigns an instance of a Move subclass to a `move` instance variable.
        prompt = 'Please choose rock, paper, scissors, lizard, or spock: '

        while True:
            choice = input(prompt).casefold()
            if choice in Player.CHOICES:
                break
            elif choice in self.ABBRIEV_CHOICES:
                choice = self.ABBRIEV_CHOICES[choice]
                break

            print(f'Sorry, {choice} is not valid')
        
        self.move = self.CHOICES[choice]

class Computer(Player):
    OPPONENT_LIST = ('R2D2', 'HAL', 'Daneel')

    def __init__(self):
        super().__init__()
        self._name = random.choice(self.OPPONENT_LIST)

    def choose(self):
        if self._name == 'R2D2':
            choice = 'rock'
        
        elif self._name == 'HAL':
            weights = [4 if option == 'scissors' else 1 for option in
                       Player.CHOICES.keys()]
            print(weights)
            
            choice = random.choice(list(Player.CHOICES.keys()),
                                   weights=weights, k=1)
        
        else:
            # Daneel
            choice = random.choice(list(Player.CHOICES.keys()))
        
        self.move = Player.CHOICES[choice]

# class MoveHistory:
#     def __init__(self):
#         self._human = []
#         self._computer = []

#     def __str__(self):
        # return f'Human: {self._human} | Computer: {self._computer}'

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._current_match = 1
        self._current_round = 1
        self._game_name = 'Rock Paper Scissors Lizard Spock'
    
    def _display_welcome_message(self):
        print(f'Welcome to {self._game_name}!')
        print(f'You are playing against: {self._computer._name}')

    def _display_goodbye_message(self):
        print(f'Thanks for playing {self._game_name}. Goodbye!')

    # def _choose_computer(self):
    #     while True:
    #         opponent = (input(f'Choose an opponent from: '
    #                         f'{', '.join(self.COMPUTER_LIST)}'))
    #         if opponent in self.COMPUTER_LIST:
    #             break
    #     self._opponent = opponent
        

            
            

    def _display_winner(self):        
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {self._human.move}')
        print(f'Computer chose: {self._computer.move}')
        
        if human_move == computer_move:
            print("It's a tie!")

        elif computer_move.name.lower() in human_move._defeats:
            print('Human wins!')
            self._human.score += 1
        
        else:
            print('Computer wins!')
            self._computer.score += 1

    def _update_and_display_move_history(self):
        self._human.history.append(f'{self._current_round}: '
                                   f'{self._human.move.name}')
        self._computer.history.append(f'{self._current_round}: '
                                      f'{self._computer.move.name}')
        print(f'Human choices: {self._human.history} | '
              f'Computer choices: {self._computer.history}')
        
        
        # MoveHistory._human.append(self.human_move.name)
        # MoveHistory._computer.append(self.computer_move.name)
        # print(Move


    def _display_current_score(self):
        print(f'The score is now:\n'
              f'Human: {self._human.score} Computer: {self._computer.score}')
        
    def _display_grand_winner(self):
        grand_winner = None
        if self._human.score == 5:
            grand_winner = 'Human'
        else:
            grand_winner = 'Computer'
        print(f'\nThe winner is {grand_winner}!')
              
        
    def _display_current_round(self):
        print(f'\nRound {self._current_round})')

    def _increment_round(self):
        self._current_round += 1
    
    def _update_move_history(self):
        pass

    def _reset(self):
        self._human.score = 0
        self._computer.score = 0
        self._current_round = 1
        self._current_match += 1
        self._reset_opponent()

    def _reset_opponent(self):
        self._computer.name = random.choice(Computer.OPPONENT_LIST)

    def play(self):
        self._display_welcome_message()
        while True:
            # clears player/computer scores, starts new best of 5 match
            self._reset()
            # self._choose_computer()

            while True:
                # current match loop
                self._display_current_round()
                self._human.choose()
                self._computer.choose()
                self._display_winner()
                self._display_current_score()
                self._update_and_display_move_history()
                if self._human.score == 5 or self._computer.score == 5:
                    break
                self._increment_round()
                

            self._display_grand_winner()
            if not self._play_again():
                    break
        self._display_goodbye_message()

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')    

RPSGame().play()

'''
History of moves
List with nested Dictionaries
[
    {'Human': [move1, move2, move3 ....]}
    {'Computer': [{move1: round1}, {move2: round2}
    ]

[
    {Match 1:
        {round1:
            {human: human choice},
            {computer: computer_choice}
            },
    {Match 2:
        ..........

        
Classes for MOves
method for x defeats: x, y

'''