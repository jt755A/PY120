import random

class Player:
    def __init__(self):
        self.guesses = 7

    def make_a_guess(self):
        prompt = (f"Enter a number between {min(GuessingGame.NUMBER_OPTIONS)}"
                       f" and {max(GuessingGame.NUMBER_OPTIONS)}: ")
        while True:
            guess = input(f'{prompt}')
            if guess.isdigit():
                guess = int(guess)

            if guess in GuessingGame.NUMBER_OPTIONS:
                return guess

            print(f'Invalid guess.', end=" ")



class GuessingGame:
    NUMBER_OPTIONS = list(range(1, 101))
    GUESSES = 7
    GUESS_MESSAGES = {'high': 'Your guess is too high.',
                      'low': 'Your guess is too low',
                      'correct': "That's the number!"}

    # no play again functionality
    # default guess Limit is 7 --> Constant
    # number range is defeault: 1 - 100
        # Min and max limits as constant
    # random number defined in init method?
    def __init__(self):
        self.correct_number = None
        self.guesses = GuessingGame.GUESSES
        self.player = Player()

    def play(self):
        self.set_random_num()
        while not self.is_game_over():
            self.display_guesses()
            guess = self.player_turn()
            result = self.check_guess(guess)
            self.display_round_result(result)
            if result == 'correct':
                break
            self.update_guesses()

        self.display_game_result(result)

    def display_guesses(self):
        guesses_remaining = self.player.guesses
        if guesses_remaining == 1:
            print(f'You have {self.player.guesses} guess remaining.')
        else:
            print(f'You have {self.player.guesses} guesses remaining.')

    def player_turn(self):
        return self.player.make_a_guess()

    def check_guess(self, guess):
        if guess > self.correct_number:
            return 'high'
        elif guess < self.correct_number:
            return 'low'
        return 'correct'

    def update_guesses(self):
        self.player.guesses -= 1

    def display_round_result(self, result):
        print(self.GUESS_MESSAGES[result])

    def set_random_num(self):
        self.correct_number = random.choice(GuessingGame.NUMBER_OPTIONS)

    def is_game_over(self):
        return self.player.guesses <= 0


    # def user_turn(self):
    #     while True:
    #         choice = self.make_a_choice()
    #         if choice == self.correct_number:
    #             print("That's the number!")
    #             break
    #         elif choice < self.correct_number:
    #             print('Your guess is too low')
    #         else:
    #             print('Your guess is too high')


    def display_game_result(self, result):
        if result == 'correct':
            print('You won!')

        else:
            print('You have no more guesses. You lost!')


game = GuessingGame()
game.play()