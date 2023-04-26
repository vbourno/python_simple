import math

class Circle:
    __count = 0
    def __init__(self, radius = 100):
        self.__radius = radius
        Circle.__count += 1

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            self.__radius = 0
        else:
            self.__radius = value

    @property
    def perimeter(self):
        return 2 * math.pi * self.__radius

    @classmethod
    def count(cls):
        return cls.__count
        
def main():    
    c1 = Circle()
    c = Circle(10)
    c.radius = 30
    print("Radius:", c.radius)
    print("Perimeter:", c.perimeter)
    print("Number of circles:", Circle.count())

if __name__ == '__main__':
    main()