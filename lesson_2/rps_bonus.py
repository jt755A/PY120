import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None
        self.score = 0

class Human(Player):
    def __init__(self):
        super().__init__()
        
    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).casefold()
            if choice in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')
        
        self.move = choice

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class MoveHistory:
    def __init__(self):
        self._history = []

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._current_match = 1
        self._current_round = 1

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper'))
    
    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
            (computer_move == 'paper' and human_move == 'rock') or
            (computer_move == 'scissors' and human_move == 'paper'))
    
    def _display_winner(self):

        print(f'You chose: {self._human.move}')
        print(f'Computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
            self._human.score += 1
        elif self._computer_wins():
            print('Computer wins!')
            self._computer.score += 1

        else:
            print("It's a tie!")
        
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
        

    def _reset(self):
        self._human.score = 0
        self._computer.score = 0
        self._current_round = 1
        self._current_match += 1

    def play(self):
        self._display_welcome_message()
        while True:
            self._reset()

            while True:
                self._display_current_round()
                self._human.choose()
                self._computer.choose()
                self._display_winner()
                self._display_current_score()
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

'''