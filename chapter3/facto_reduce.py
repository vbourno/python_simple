from functools import reduce

def main():
    n = int(input("Please give me an integer: "))

    # Calculate the facto
    result = reduce(lambda x, y: x * y, range(1, n + 1))

    print(f"{n}! = {result}")

main()