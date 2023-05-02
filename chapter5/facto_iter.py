# Factorial iterator
class FactoIterator:
    def __init__(self, n):
        self.n = n
        self.result = 1
        self.order =1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.order > self.n:
            raise StopIteration
        
        self.result *= self.order
        self.order += 1
        return self.result

facto_iter = iter(FactoIterator(10))

for factorial in facto_iter:
    print("{:,}".format(factorial))