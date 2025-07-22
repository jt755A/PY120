import random
import os
import time

def clear_screen():
    os.system('clear')

class Card:
    SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace')
    ROYALS = ('Jack', 'Queen', 'King')

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return f'{self._rank} of {self._suit}'


class Deck:
    def __init__(self):
        self.current_state = self.reset()

    def reset(self):
        deck = [Card(suit, rank) for suit in Card.SUITS
         for rank in Card.RANKS]
        random.shuffle(deck)
        return deck

    def deal(self):
        drawn_card = self.current_state.pop()
        return drawn_card

class Participant:

    def __init__(self):
        self._hand = []

    @property
    def hand(self):
        return self._hand

    def reset(self):
        self._hand = []

    def hit(self, card):
        self._hand.append(card)

    def stay(self):
        return f'chose to stay with {self.score()}'

    def is_busted(self):
        return self.score() > TwentyOneGame.LIMIT

    def score(self):
        total = 0
        aces_count = 0

        for card in self.hand:
            if card._rank == 'Ace':
                total += 11
                aces_count += 1
            elif isinstance(card._rank, int):
                total += card._rank
            elif card._rank in Card.ROYALS:
                total += 10

        while aces_count and total > TwentyOneGame.LIMIT:
            total -= 10
            aces_count -= 1

        return total

class Player(Participant):
    INITIAL_PURSE = 5
    WINNING_PURSE = 10

    def __init__(self):

        super().__init__()
        self.money = Player.INITIAL_PURSE

    def win_bet(self):
        self.money += 1

    def lose_bet(self):
        self.money -= 1

    def has_no_money(self):
        return self.money <= 0

    def has_winning_money(self):
        return self.money >= Player.WINNING_PURSE

    def show_purse(self):
        print(f'You have ${self.money}')
        print()

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self._reveal = False

    @property
    def reveal(self):
        return self._reveal

    @reveal.setter
    def reveal(self, value):
        self._reveal = value


class TwentyOneGame:
    LIMIT = 21
    DEALER_LIMIT = 17
    NUM_CARDS_INITIAL_DEAL = 2

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.display_welcome_message()
        while not self.game_is_over():
            self.play_one_round()
            if not self.play_again():
                break
        self.display_is_game_over_message()
        self.display_goodbye_message()


    def play_one_round(self):
        self.deal_cards()
        self.player.show_purse()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.update_purse()
        self.player.show_purse()

    def deal_cards(self):
        clear_screen()
        self.player.reset()
        self.dealer.reset()
        self.dealer.reveal = False
        player_hand = self.player.hand
        dealer_hand = self.dealer.hand

        for _ in range(TwentyOneGame.NUM_CARDS_INITIAL_DEAL):
            player_hand.append(self.deck.deal()) # deal to
            dealer_hand.append(self.deck.deal()) # deal to


    def show_player_cards(self):
        print(f'You have: {self.join_and(self.player.hand)}')
        print()
        print(f"Player's score is: {self.player.score()}")
        print()

    def show_dealer_cards(self):
        if not self.dealer.reveal:
            print(f'Dealer has: {self.join_and(self.dealer.hand,
                                ', ', 'and', True)} and unknown card')
        else:
            print(f'Dealer has: {self.join_and(self.dealer.hand)}')
            print(f"Dealer's score is: {self.dealer.score()}")
            print()


    def player_turn(self):
        while True:
            self.show_dealer_cards()
            self.show_player_cards()
            choice = self.hit_or_stay()
            if choice:
                clear_screen()
                print(f"You chose to hit with: {self.player.score()}")
                drawn_card = self.deck.deal()
                self.player.hit(drawn_card)

                if self.player.is_busted():
                    self.show_player_cards()
                    break

            else:
                clear_screen()
                print(f'You {self.player.stay()}')
                break

    def dealer_turn(self):
        if self.player.is_busted():
            return

        self.dealer.reveal = True
        self.show_dealer_cards()
        self.show_player_cards()
        while self.dealer.score() < TwentyOneGame.DEALER_LIMIT:
            time.sleep(2)
            drawn_card = self.deck.deal()

            self.dealer.hit(drawn_card)
            self.show_dealer_cards()

            if self.dealer.is_busted():
                break

        if not self.dealer.is_busted():
            print(f'Dealer {self.dealer.stay()}')

    def hit_or_stay(self):
        while True:
            choice = input("Would you like to hit or stay? "
                        "(h for hit; s for stay) ").casefold()
            if choice not in ['h', 's', 'hit', 'stay']:
                print("That's not a valid choice. Please enter 'h' or 's'")
            else:
                break

        if choice.startswith('h'):
            print('hit')
            return True

        return False

    def join_and(self, hand, delimiter=', ', join_word='and', hidden=False):
        joined_nums = ''

        if not hidden:
            str_lst = [str(card) for card in hand]
            joined_nums += delimiter.join(str_lst[:-1])
            return f'{joined_nums} {join_word} {str_lst[-1]}'

        if hidden:
            str_lst = [str(card) for card in hand[1:]]

            if len(str_lst) == 1:
                return str_lst[0]

            joined_nums += delimiter.join(str_lst[:])
            return f'{joined_nums} and unknown card'

    def determine_winner(self):
        if self.player.is_busted():
            return self.dealer
        if self.dealer.is_busted():
            return self.player

        if self.player.score() > self.dealer.score():
            return self.player
        if self.dealer.score() > self.player.score():
            return self.dealer
        else:
            return None

    def display_result(self):
        if self.player.is_busted():
            print('You busted. Dealer wins.')
        elif self.dealer.is_busted():
            print('Dealer busted. You win!')
        else:
            winner = self.determine_winner()
            if winner == self.player:
                print('You win!')
            elif winner == self.dealer:
                print('Dealer wins.')
            else:
                print("It's a tie!")

    def update_purse(self):
        winner = self.determine_winner()
        if winner == self.player:
            self.player.win_bet()
        elif winner == self.dealer:
            self.player.lose_bet()

    def display_welcome_message(self):
        print('Welcome to twenty one!')
        print()

    def display_goodbye_message(self):
        print("Thanks for playing twenty-one. Goodbye!")

    def play_again(self):
        while True:
            answer = input("Would you like to play again? (y/n) ").casefold()
            if answer in ['y', 'n', 'yes', 'no']:
                break
            print("That's not a valid answer.")

        return answer.startswith('y')

    def game_is_over(self):
        return self.player.has_no_money() or self.player.has_winning_money()

    def display_is_game_over_message(self):
        print('TEST: GAME IS OVER')
        if self.player.has_no_money():
            print("You ran out of money!")
        elif self.player.has_winning_money():
            print("You have plenty of money!")


game = TwentyOneGame()
game.start()
