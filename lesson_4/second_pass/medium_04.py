class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

    def __str__(self):
        filling = self.filling
        glazing = self.glazing

        if filling is None:
            filling = 'Plain'
        if glazing is None:
            glazing = ''

        if glazing:
            return f'{filling} with {glazing}'

        return f'{filling}'

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

# None filling = 'Plain'
# glazing: None = empty

# pass in to arguemnts

# needs to print: __str__ method