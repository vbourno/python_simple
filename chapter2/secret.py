# Guess the secret number
import random
import math

def main():
    secret = random.randint(1, 10)
    tries = 0
    MAX_TRIES = 5

    while True:
        tries += 1
        if tries > MAX_TRIES: break

        num = int(input("Please insert an int:  "))

        if num == secret:
            print("Bingo! Secret number was:", secret)
            break
        elif math.fabs(num - secret) <= 5:
            print("Hot")
        else:
            print("Cold")
        
        if tries == MAX_TRIES:
            print("You reached the max number of tries:", MAX_TRIES)

main()