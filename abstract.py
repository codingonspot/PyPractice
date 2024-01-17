from abc import ABC, abstractmethod


class Shapes(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Square(Shapes):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


sq = Square(5)
print(sq.area())
print(sq.perimeter())
