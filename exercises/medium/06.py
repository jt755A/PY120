import random

class Card:
    CARD_RANKS = {
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14,
    }

    def __init__(self, rank, suit):
        self._rank = rank
        self.suit = suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        
        return (self.__class__.CARD_RANKS[self.rank] < 
                other.__class__.CARD_RANKS[other.rank])
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        
        return (self.__class__.CARD_RANKS[self.rank] ==
                other.__class__.CARD_RANKS[other.rank])
    

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.deck = self.build_deck()

    def build_deck(self):
        # new_deck = []
        # for suit in self.__class__.SUITS:
        #     for rank in self.__class__.RANKS:
        #         new_deck.append(Card(rank, suit))

        new_deck = [Card(rank, suit)
                    for rank in Deck.RANKS
                    for suit in Deck.SUITS]

        random.shuffle(new_deck)     
        return new_deck
        
    def draw(self):
        if len(self.deck) == 0:
            self.deck = self.build_deck()
        
        drawn_card = self.deck.pop()
        return drawn_card
    
# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck):
        pass

    def print(self):
       pass

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        pass

    def _is_straight_flush(self):
        pass

    def _is_four_of_a_kind(self):
        pass

    def _is_full_house(self):
        pass

    def _is_flush(self):
        pass

    def _is_straight(self):
        pass

    def _is_three_of_a_kind(self):
        pass

    def _is_two_pair(self):
        pass

    def _is_pair(self):
        pass