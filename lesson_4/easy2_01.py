class Game:
    _count = 0

    @classmethod
    def count(cls):
        return cls._count
    
    def __init__(self):
        self.__class__._count += 1
    
    def play(self):
        return f'Start the {self.__class__.__name__} game!'

class Bingo(Game):
    def __init__(self, game_name, player_name):
        self.game_name = game_name
        self._player_name = player_name



bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'