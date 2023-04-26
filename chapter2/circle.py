import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, value):
        if value < 0:
            self.__radius = 0
        else:
            self.__radius = value

    def get_perimeter(self):
        return 2 * math.pi * self.__radius
    
    radius = property(get_radius, set_radius)
    perimeter = property(get_perimeter)
    
def main():    
    c = Circle(10)
    c.radius = 30
    print("Radius:", c.radius)
    print("Perimeter:", c.perimeter)

if __name__ == '__main__':
    main()