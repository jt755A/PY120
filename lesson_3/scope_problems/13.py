class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

'''
Pine will have a `type` attribute with the value "Pine Tree" when an instance
is created. Line 8 overrides the `type` attribute from line 7 that is called
from the superclass. THe original value "Generic Tree" is reassigned.
'''