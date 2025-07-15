class KrispyKreme:
    def __init__(self, filling='Plain', glazing=''):
        self.filling = filling
        self.glazing = glazing

    def __str__(self):
        if self.filling == None:
            self.filling = 'Plain'
        
        if self.glazing:
            return f'{self.filling} with {self.glazing}'
        else:
            return f'{self.filling}'

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing