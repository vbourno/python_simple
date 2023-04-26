
a = int(input("Please give the length of a side:  "))
b = int(input("Please give the length of b side:  "))

if a > 0 and b > 0:
    if a == b:
        print("Square")
    else:
        print("Rectangle")
    
    print("Square") if a == b else print("Rectangle")