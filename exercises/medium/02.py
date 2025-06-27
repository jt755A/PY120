'''
TOTAL_GUESSES = 7
START_NUM = 1
END_NUM = 100
TARGET_NUM = random generated number

round = 0
guesses_remaining = TOTAL_GUESSES - round

Start a loop (until 
    - You have .... gueses remaining
    - Enter number
        - Validate input (make sure it's an integer, and in range)
    - compare user input to TARGET_NUM
        - break if it's equal
        - winning message

    - if not equal
        - say if guess is too high or low
    
    - decrement count
    -   

- if guesses_remaining = 0
- losing_message
- end game
'''

import random

class GuessingGame:
    GUESS_LIMIT = 7
    START_NUM = 1
    END_NUM = 100
    TARGET_NUM = random.randrange(START_NUM, END_NUM + 1)

    winner = False

    round_counter = 0
    guesses_remaining = GUESS_LIMIT - round_counter

    @classmethod
    def guesses_left(cls):
        print(f'You have {GuessingGame.guesses_remaining} guesses remaining.')

    @classmethod
    def enter_message(cls):
        return (f'Enter a number between {GuessingGame.START_NUM} and '
              f'{GuessingGame.END_NUM}: ')
    


    def valid_num(self, number):
        try:
            int(number)
        
        except TypeError:
            return False
        
        except ValueError:
            return False
        
        if (int(number) < GuessingGame.START_NUM 
            or int(number) > GuessingGame.END_NUM):
            return False
        
        return True
    
    
    
    def guess(self):
        pass

    
    

    def got_the_num(self, guess):
        self.guess = guess
        if self.guess == GuessingGame.TARGET_NUM:
            GuessingGame.winner = True
            print(f"That's the number!\nYou won!")
        
        elif self.guess < GuessingGame.TARGET_NUM:
            print("Your guess is too low.")
        
        else:
            print("Your guess is too high.")
        
    def play(self):
        while GuessingGame.guesses_remaining > 0 and not GuessingGame.winner:
            GuessingGame.guesses_left()
            choice = input(GuessingGame.enter_message())
            while not GuessingGame.valid_num(int(choice)):
                choice = input(f'Invalid choice. {GuessingGame.enter_message()}')
            
        


game = GuessingGame()
game.play()
