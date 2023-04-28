# filter function with lambda

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)

    list_even_nums = list(even_numbers_iterator)

    for num in list_even_nums:
        print(num, end=" ")
    print()

    for num in list_even_nums:
        print(num, end=" ")
    print()

# Iterator can be iterated just once
    # for even_num in even_numbers_iterator:
    #   print(even_num, end=" ")
    # print()

main()