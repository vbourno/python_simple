class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: \
                            'Point' and {type(other).__name__}")
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
# create some instances
p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1 + p2)
print(p1 + 10)
print(20 + p1)
print(sum([p1, p2]))
print(p1 == Point(1, 2))
print(p1 == "Some message")

def do_add(a, b):
    return a + b

print(do_add(p1, 100))
print(do_add(p1, p2))
print(do_add(1, 2))
print(do_add(1.5, 2.6))