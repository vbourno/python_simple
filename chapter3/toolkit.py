import functools

def calculate(args):
    def plus():
        return functools.reduce(lambda x, y: x + y, args)
    
    def minus():
        return functools.reduce(lambda x, y: x - y, args)
        # return args[0] - plus()

    def mul():
        return functools.reduce(lambda x, y: x * y, args)
    
    def div():
        if plus() == 0:
            return 0
        return "{:.2f}".format(args[0] / plus())
    
    return plus, minus, mul, div

def main():
    ints = [26, 5, 4, 3, 2, 1]

    add_func, minus_func, mul_func, div_func = calculate(ints)

    # print results
    print("add_func:", add_func())
    print("minus_func:", minus_func())
    print("mul_func:", mul_func())
    print("div_func:", div_func())

main()