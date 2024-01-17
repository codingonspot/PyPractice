class Polygon:
    __width = None
    __height = None

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Rectangle(Polygon):
    def area(self):
        return self.get_width()  * self.get_height()


class Traingle(Polygon):
    def area(self):
        return self.get_width()* self.get_height() / 2


r = Rectangle()
t = Traingle()
r.set_values(5, 4)
t.set_values(4, 3)
print(r.area())
print(t.area())