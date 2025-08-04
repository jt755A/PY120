class Card:
    CARD_VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    SUIT_VALUES = {'Spades': 4, 'Hearts': 3, 'Clubs': 2, 'Diamonds': 1}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def rank_value(self):
        return Card.CARD_VALUES.get(self.rank, self.rank)

    @property
    def suit_value(self):
        return Card.SUIT_VALUES[self.suit]


    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank == other.rank:
            # return Card.SUIT_VALUES[self.suit] < Card.SUIT_VALUES[other.suit]
            return self.suit_value < other.suit_value

        return self.rank_value < other.rank_value



# cards = [Card(2, 'Hearts'),
#          Card(10, 'Diamonds'),
#          Card('Ace', 'Clubs')]
# print(min(cards) == Card(2, 'Hearts'))             # True
# print(max(cards) == Card('Ace', 'Clubs'))          # True
# print(str(min(cards)) == "2 of Hearts")            # True
# print(str(max(cards)) == "Ace of Clubs")           # True

# cards = [Card(5, 'Hearts')]
# print(min(cards) == Card(5, 'Hearts'))             # True
# print(max(cards) == Card(5, 'Hearts'))             # True
# print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True
print(f'Test: {min(cards) == Card(4, 'Diamonds')}')

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True
print(f'Test: {max(cards) == Card('Jack', 'Spades')}')

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True
print(f'{min(cards)=}, {max(cards)=}')