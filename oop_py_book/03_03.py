'''
3. Challenge: Create the classes needed to make the following code 
work as shown:
'''
class Candidate:
    
    def __init__(self, name):
        self.name = name
        self.votes = 0
    
    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        self.votes += other
        return self


class Election:

    def __init__(self, candidates):
        self.candidates = candidates    
    
    def results(self):
        highest_votes = 0
        total_votes = 0
        winner = None

        for candidate in candidates:
            total_votes += candidate.votes
            if candidate.votes > highest_votes:
                highest_votes = candidate.votes
                winner = candidate.name
        
        winner_percent = f'{highest_votes / total_votes:.1%}'
        
        for candidate in self.candidates:
            print(f'{candidate.name}: {candidate.votes} votes')
        
        print()
        print(f'{winner} won {winner_percent} of votes')
        


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
    candidate += 1

# print(votes)

election = Election(candidates)
election.results()

'''
Mike Jones: 3 votes
Susan Dore: 4 votes
Kim Waters: 1 votes

Susan Dore won: 50.0% of votes
'''