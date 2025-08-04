class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        try:
            float(new_width)
        except (TypeError, ValueError) as e:
            print(e)
            # raise e

        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        try:
            float(new_height)
        except (TypeError, ValueError) as e:
            print(e)
            # raise e

        self._height = new_height


rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True

rect = Rectangle(4, [5])


print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True