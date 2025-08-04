class Game:
    count = 0

    def __init__(self, game_name):
        Game.count += 1
        self.game_name = game_name

    def play(self):
        return f'Start the {self.game_name} game!'

class Bingo(Game):
    def __init__(self, game, player):
        super().__init__(game)
        self.game_name = game
        self.player_name = player

class Scrabble(Game):
    def __init__(self, game, player1, player2):
        super().__init__(game)
        self.game_name = game
        self.player_name1 = player1
        self.player_name2 = player2


bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'