class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    

rect1 = Rectangle(1, 4)

print(rect1.width)
print(rect1.height)

rect1.width = 15
rect1.height = 15

print(rect1.width)
print(rect1.height)



