import math

name = "Alice"
age = 30

print('CF')             # CF
print("PI = ", math.pi) # PI = 3.14
print("My name is", name, "and I am", age, "years old.")
print("My name is " + name + " and I am " + str(age) + " years old.")

# Python 2 Style
print("PI = %6.2f" %math.pi)
print("%s is %d years old." %(name, age))

# Python 3 Style
print("Age is {0:2d}".format(age)) # Age is 30
print("PI is {0:.3f}".format(math.pi))
print("{0} is {1} years old.".format(name, age)) # Alice is 30 years old.
print("{0:*^10} {1:>20}".format(name, age)) # Alice

# f-strings and variables interpolation
print(f"My name is {name} and I am {age} years old.")
print(f"{name:>20}, {age:<5}")