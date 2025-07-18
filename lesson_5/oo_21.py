import random

class Card:
    SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace')
    ROYALS = ('Jack', 'Queen', 'King')

    def __init__(self, suit, rank):
        # STUB
        # What attributes does a card need? Rank? Suit?
        #   Points?
        self._suit = suit
        self._rank = rank
        # self._value = self.value()

        pass

    def value(self):
        # the value of a card is the numeric component, or 10 if a royal.
        # Ace depends on your hand.....
        # should this be a method in hand class
        pass

    def __str__(self):
        return f'{self._rank} of {self._suit}'


class Deck:
    def __init__(self):
        # STUB
        # What attributes does a deck need? A collection of
        #   52 cards?
        # Some data structure, like a list or dictionary,
        #   might be required.
        # a list of Card objects?

        # reset deck method? When deck is empty

        self.current_state = self.reset()

        pass

    def reset(self):
        # STUB
        # Resets the deck by creating a shuffled list. This list is initialized
        # in __init__method. Can call again if necessary.
        # Shuffle 52 cards.
        deck = [Card(suit, rank) for suit in Card.SUITS
         for rank in Card.RANKS]
        random.shuffle(deck)
        return deck
    
    def deal(self):
    # STUB
    # Does the dealer or the deck deal?
    # If deck is empty... Call the reset function

    # Pop a card from current deck
    # (This can be can be called by either player in the Game class?)
        drawn_card = self.current_state.pop()
        # print(f'Card drawn. Deck now has length: {len(self.current_state)}')
        return drawn_card

class Hand:
    def __init__(self):
        # STUB
        # Don't think this is needed at all
        # Just a list o 
        pass

class Participant:
    def __init__(self):
        # STUB
        # What attributes does a participant require? Score?
        #   Hand? Betting balance?
        # What else goes here? all the redundant behaviors
        #   from Player and Dealer?
        self._hand = []
        pass

    @property
    def hand(self):
        return self._hand

    def hit(self, card):
        self._hand.append(card)
        # STUB
        # draws one card from deck

        pass

    def stay(self):
        return f'chose to stay with {self.score()}'
        pass

    def is_busted(self):
        # STUB
        # Checks if player's score is above the Game limit
        return self.score() > TwentyOneGame.LIMIT
        pass

    def score(self):
        # STUB
        # iterate through cards in hand, sum the amounts.
        # needs a helper function for ace?
        total = 0
        aces_count = 0

        for card in self.hand:
            if card._rank == 'Ace':
                total += 11
                aces_count += 1
            elif isinstance(card._rank, int):
                total += card._rank
            elif card._rank in Card.ROYALS:
                # Magic number....
                total += 10
        
        while aces_count and total > TwentyOneGame.LIMIT:
            total -= 10
            aces_count -= 1        

        return total



class Player(Participant):
    def __init__(self):
        # STUB
        # What additional attributes might a player need?
        # Score? Hand? Amount of money available?
        super().__init__()
        self.pot
        pass

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        # STUB
        # Very similar to a Player; do we need this?
        self._reveal = False

        pass

    def hide(self):
        # STUB
        pass

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
        # STUB
        # What attributes does the game need? A deck? Two
        #   participants?

        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        pass

    def start(self):
        # SPIKE
        self.display_welcome_message()

        # Not needed for actual game play

        self.deal_cards()
        # self.show_current_deck()
        # self.show_cards()
        # self.display_hidden_hands()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.display_goodbye_message()

    def show_current_deck(self):
        for card in self.deck.current_state:
            print(card)
        print(f'Total cards = {len(self.deck.current_state)}')
    
    def deal_cards(self):
        # STUB
        # Takes card from end of deck, deals alternately to player and dealer
        # Need to check if deck is empty first?
        
        player_hand = self.player.hand
        dealer_hand = self.dealer.hand

        for _ in range(TwentyOneGame.NUM_CARDS_INITIAL_DEAL):
            player_hand.append(self.deck.deal()) # deal to
            dealer_hand.append(self.deck.deal()) # deal to

        pass



    # def show_cards(self):
    #     # # STUB
    #     # # print player, computer
    #     # print(f"Player has: {str(self.player.hand)} |"
    #     #       f"Dealer has: {str(self.dealer.hand)}")

    #     if not self.dealer.reveal:
    #         print(f'Dealer has: {self.join_and(self.dealer.hand, 
    #         ', ', 'and', True)} and unknown card')
    #     else:
    #         print(f'Dealer has: {self.join_and(self.dealer.hand)}')

    #     print(f'You have: {self.join_and(self.player.hand)}')
    #     print(f"Player's score is: {self.player.score()}")
    #     pass

    def show_player_cards(self):
        print(f'You have: {self.join_and(self.player.hand)}')
        print(f"Player's score is: {self.player.score()}")
    
    def show_dealer_cards(self):
        if not self.dealer.reveal:
            print(f'Dealer has: {self.join_and(self.dealer.hand, 
                                ', ', 'and', True)} and unknown card')
        else:
            print(f'Dealer has: {self.join_and(self.dealer.hand)}')
            print(f"Dealer's score is: {self.dealer.score()}")



    def player_turn(self):
        # STUB
        while True:
            # self.display_hidden_hands()
            # self.show_cards()
            self.show_dealer_cards()
            self.show_player_cards()
            # self.show_
            choice = self.hit_or_stay()
            if choice:
                print(f"You chose to hit with: {self.player.score()}")
                drawn_card = self.deck.deal()
                self.player.hit(drawn_card)

                if self.player.is_busted():
                    # print(f"Your score is: {self.player.score()}. You lost!")
                    break
            
            else:
                # print(f"You chose to stay with: {self.player.score()}")
                print(f'You {self.player.stay()}')
                break

    def hit_or_stay(self):
        # STUB
        # code to ask player whether they want to take another card.
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
        else:
            print('player stays')
            return False

        
            
        pass

    def dealer_turn(self):
        # STUB
        # Reveal the dealer's hand
        self.dealer.reveal = True
        while self.dealer.score() < TwentyOneGame.DEALER_LIMIT:
            self.show_dealer_cards()
            drawn_card = self.deck.deal()
            self.dealer.hit(drawn_card)

            if self.dealer.is_busted():
                break
        
        if not self.dealer.is_busted():
            print(f'Dealer {self.dealer.stay()}')

    def display_welcome_message(self):
        # STUB
        self.display_rules()

    def display_rules(self):
        print("""Welcome to twenty-one! You will be playing against the 
              dealer. The value of cards in your hands will be summed. 
              Whoever's total is closest to 21 wins. If you go over 21, you 
              'bust' - losing the round. Regular rank cards have a value that 
              matches their rank. Royals have a value of 10. Aces have EITHER 
              11 or 1, depending on your hand. Your betting balance is $5.
              If you lose a round, you lose $1. If you win, you gain $1.
              The game is over when you run out of money, or reach $10.
              Good luck!""")
        
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
        
    def display_hidden_hands(self):
        print(f'Dealer has: {self.join_and(self.dealer.hand, 
            ', ', 'and', True)} and unknown card')
        
        print(f'You have: {self.join_and(self.player.hand)}')
        print(f"Player's score is: {self.player.score()}")

    def display_goodbye_message(self):
        # STUB
        print("Thanks for playing twenty-one. Goodbye!")

    def display_result(self):
        # STUB
        # determine winner.
        # print winner
           
        if self.player.is_busted():
            return self.dealer
        elif self.dealer.is_busted():
            return self.player
        
        if self.player.score() > self.dealer.score():
            return self.player
        elif self.dealer.score() > self.player.score():
            return self.dealer
        else:
            return "It's a tie!"

game = TwentyOneGame()
game.start()