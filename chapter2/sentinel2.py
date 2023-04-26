def main():
    ch = input("Give a char:  ")

    while(True):
        print(ch, ord(ch))
        ch = input("Give a char:  ")
        if ch == "#":
            break
    
    print("Goodbye!")

main()