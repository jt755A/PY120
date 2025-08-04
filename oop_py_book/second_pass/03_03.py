class Candidate:
    total_votes = 0
    def __init__(self, name):
        self.name = name
        self.votes = 0


    def __iadd__(self, number):
        if not isinstance(number, int):
            return NotImplemented
        self.votes += number
        Candidate.total_votes += number
        return self

    def __str__(self):
        return f'{self.name}'

    def __lt__(self, other):
        return self.votes < other.votes

class Election:
    def __init__(self, candidates_set):
        self.candidates = candidates_set

    def _who_won(self):
        return max(candidates)

    def _display_votes(self):
        for candidate in self.candidates:
            print(f'{candidate}: {candidate.votes} votes')

    def _display_votes_breakdown(self, winner):
        winning_percentage = winner.votes / Candidate.total_votes
        print(f'{winner} won: {winning_percentage:.2%} of votes')



    def results(self):
        # for candidate in candidates:
        #     print(f'{candidate}: {candidate.votes} votes')
        self._display_votes()
        winner = self._who_won()
        self._display_votes_breakdown(winner)
        # print(f'{winner.name} won: {''} of votes')

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1 # implies an __iadd__ method that will increment an instance variable

election = Election(candidates)
election.results() # displays f'name: {votes} votes'
                    # picks winner. Displays name, they won...