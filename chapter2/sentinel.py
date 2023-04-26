def main():
    ch = input("Give a char:  ")

    while ch != "#":
        print(ch, ord(ch))
        ch = input("Give a char:  ")
    
    print("Goodbye!")

main()