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

rect = Rectangle(1, 3)
print(f'{rect.width=}')
print(f'{rect.height=}')

rect.height = 7