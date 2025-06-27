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
    
'''
Rules
    - when Deck initialized, it is shuffled
    - draw method (no arguments)
        - Remove one card from top/bottom (pop?)
            - its return value is a Card object: 2, "hearts"
        - if Deck is empty, generate + shuffle 52 more cards
            - deal one card, as above
    - implies a generate deck + shuffle method?

    - how to represent a deck of cards
        - inputs: lists of RANKS, SUITS
        - a new list, made by iterating through both constants?
        - shuffle the new sequence in place?
        - a list of tuples
'''

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

    
    # def show_cards(self):
    #     for card in self.deck:
    #         print(card)

    # def play(self):
    #     self.show_cards()

    # def __str__(self):
    #     return f'{}'



deck = Deck()
# deck.play()



drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

# print(deck)

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).