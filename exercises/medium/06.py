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
        self._deck = self.build_deck()


    def build_deck(self):
        new_deck = [Card(rank, suit)
                    for rank in Deck.RANKS
                    for suit in Deck.SUITS]

        random.shuffle(new_deck)     
        return new_deck
        
    def draw(self):
        if len(self._deck) == 0:
            self._deck = self.build_deck()
        
        drawn_card = self._deck.pop()
        return drawn_card
    
# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]
        # self._hand_suits = [card.suit for card in self._hand]
        self._hand_rank = [card.rank for card in self._hand]
        self._hand_count = {card.rank: self._hand_rank.count(card.rank)
                            for card in self._hand}

        # print(f'hand count: {self._hand_count}')

    def print(self):
        for card in self._hand:
            print(card)
 
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

    def _is_n_of_kind(self, n):
        return n in self._hand_count.values()
    
    def _is_royal_flush(self):
        return self._is_straight_flush() and min(self._hand).rank == 10

    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self):
        return self._is_n_of_kind(4)
        

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        for suit in Deck.SUITS:
            if all([card.suit == suit for card in self._hand]):
                return True
        
        return False           
        

    def _is_straight(self):
        self.card_values_asc = sorted([Card.CARD_RANKS[card.rank]
                            for card in self._hand])
        
        smallest_card = min(self._hand).rank
        straight_range = range(smallest_card, smallest_card + 5)
        return self.card_values_asc == list(straight_range)


    def _is_three_of_a_kind(self):
        return self._is_n_of_kind(3)
        

    def _is_two_pair(self):
        pair_count = [value for value in self._hand_count.values()
                      if value == 2]
        return len(pair_count) == 2

    def _is_pair(self):
        return self._is_n_of_kind(2)


# hand = PokerHand(Deck())
# hand.print()

# print(hand)
# print(hand._is_flush())


'''
hand.print - prints each card in hand, on separate line


Straight
create a 5 element range upward, starting from smallest card in my hand
    - "smallest" uses the CARD_RANKS dictionary value
- compare is a list of this range is equal to a sorted list of my hand

evaluate() suggests a dicitonary of cards in hand: {(rank, suit): num_value, ...}
or just a count_dict: {1: 1, 2: 2, 5: 1, King: 1
    - return key where value = the amount you want...

is_flush:
    cr
    
    
    - Iterate through suits in SUITS
        - iterate through self._hand
            - if suit of element != `suit`
                - break
                - otherwise continue



    - create a hand_suit list
            - iterate thorugh cards in hand, select suit
            - iterate through suits:
                - if all hand_suit members belong to 'suit'
                    - return True
        - 


n of a kind: pairs, three of a kind, 4 of a kind, full house
takes hand, n as arguments

creates a dictionary of counts: card: number of occurences
    - return boolean of whether n is in dictionary_values



'''
# print(hand.evaluate())
# print()

# # Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# # All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")