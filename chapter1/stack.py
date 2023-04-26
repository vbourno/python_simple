# Import regular expression module
import re

# Declaration of an empty stack
stack = []
num = 0

def push(list, item):
    list.append(item)

def pop(list):
    if list:
        return list.pop()
    else:
        print("Stack is empty")

def print_menu():
    print("1. Insert on the top")
    print("2. Get from the top")
    print("q/Q for Quit")

def get_choice():
    return input("Please provide a choice\n")

def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue

        if choice == 'q' or choice == 'Q':
            break

        pattern = r'^\d+$'
        match = re.match(pattern, choice)

        if not match:
            print("Error in choice")
            continue

        choice = int(choice)

        match choice:
            case 1:
                num = input("Please insert a num\n")
                match = re.match(pattern, num)

                if not match:
                    print("Error in num")
                    continue

                num = int(num)
                push(stack, num)
                print(num, "pushed in the stack")

            case 2:
                out_num = pop(stack)
                print("You got:", out_num)

            case _:
                print("Not valid choice")

    print("Goodbye")

if __name__ == '__main__':
    main()