from m_04 import Card

import random

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._init_deck()

    def _init_deck(self):
        deck = [Card(rank, suit) for suit in Deck.SUITS
                for rank in Deck.RANKS]
        random.shuffle(deck)
        self._deck = deck

    def draw(self):
        if not self._deck:
            # print('Empty Deck!')
            self._init_deck()
            # print('New deck drawn!')

        drawn_card = self._deck.pop()
        return drawn_card


deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).


'''
A deck will be a list of all cards

if deck is empty: initialize deck -- pop
Pop one card from self._deck
'''

