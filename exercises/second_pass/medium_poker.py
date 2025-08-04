from random import shuffle

class Card:
    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

# insert Card class from previous exercise here

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._reset()

    def draw(self):
        if not self._deck:
            self._reset()

        return self._deck.pop()

    def _reset(self):
        self._deck = [Card(rank, suit)
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]

        shuffle(self._deck)

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    CARDS_IN_HAND = 5

    def __init__(self, deck):
        self.deck = deck
        self.hand = self.initial_deal()
        self._card_ranks = [card.rank for card in self.hand]
        self._rank_occurences = {card.rank: self._card_ranks.count(card.rank)
                                 for card in self.hand}

    def print(self):
       for card in self.hand:
           print(card)

    def initial_deal(self):
        return [self.deck.draw() for _ in range(PokerHand.CARDS_IN_HAND)]

    def get_hand_matches(self):
        matches = {}
        for card in self.hand:
            matches.setdefault(card.rank, 1)


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
        return (self._is_straight_flush()
                and min(self.hand).value == 10)


    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self):
        return 4 in self._rank_occurences.values()

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        for suit in Deck.SUITS:
            if all([suit == card.suit for card in self.hand]):
                return True

        return False

    def _is_straight(self):
        sorted_hand = sorted([card.value for card in self.hand])
        # print(sorted_hand)
        smallest_card_value = min(self.hand).value
        # print(smallest_card_value)
        poss_straight = range(smallest_card_value, smallest_card_value + 5)
        # print(poss_straight)
        return sorted_hand == list(poss_straight)



    def _is_three_of_a_kind(self):
        return 3 in self._rank_occurences.values()

    def _is_two_pair(self):
        card_occurences = list(self._rank_occurences.values())
        return card_occurences.count(2) == 2

    def _is_pair(self):
        return 2 in self._rank_occurences.values()


'''
Dict of rank: occurences in hand
    - iterate through hand
        - add rank, occurence

    - how to find occurence
        - given hand
        - count how many times rank is in card_ranks
'''


hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

# class TestDeck(Deck):
#     def __init__(self, cards):
#         self._deck = cards

# # All of these tests should return True

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Ace", "Hearts"),
#             Card("Queen", "Hearts"),
#             Card("King", "Hearts"),
#             Card("Jack", "Hearts"),
#             Card(10, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Royal flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Clubs"),
#             Card("Queen", "Clubs"),
#             Card(10, "Clubs"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Four of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Full house")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(10, "Hearts"),
#             Card("Ace", "Hearts"),
#             Card(2, "Hearts"),
#             Card("King", "Hearts"),
#             Card(3, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Flush")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(8, "Clubs"),
#             Card(9, "Diamonds"),
#             Card(10, "Clubs"),
#             Card(7, "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card("Queen", "Clubs"),
#             Card("King", "Diamonds"),
#             Card(10, "Clubs"),
#             Card("Ace", "Hearts"),
#             Card("Jack", "Clubs"),
#         ]
#     )
# )
# print(hand.evaluate() == "Straight")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(3, "Hearts"),
#             Card(3, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(3, "Spades"),
#             Card(6, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Three of a kind")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(9, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(8, "Spades"),
#             Card(5, "Hearts"),
#         ]
#     )
# )
# print(hand.evaluate() == "Two pair")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card(9, "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "Pair")

# hand = PokerHand(
#     TestDeck(
#         [
#             Card(2, "Hearts"),
#             Card("King", "Clubs"),
#             Card(5, "Diamonds"),
#             Card(9, "Spades"),
#             Card(3, "Diamonds"),
#         ]
#     )
# )
# print(hand.evaluate() == "High card")

# '''
# - Straight requires you to sort the values in hand sequentially
# - Then comparing these values to a range generated from smallest card in hand.

# '''

# test_hand = PokerHand(
#     TestDeck(
#         [
#             Card(10, "Hearts"),
#             Card("Ace", "Hearts"),
#             Card(2, "Hearts"),
#             Card("King", "Hearts"),
#             Card(3, "Hearts"),
#         ]
#     )
# )

# test_hand._is_straight()