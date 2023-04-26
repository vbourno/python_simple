# while ... else

counter = 0

while counter < 5:
    print("The current value of counter is:", counter)
    counter += 1
    if counter == 3:
        break
else:
    print("The counter is not less than 5 anymore")