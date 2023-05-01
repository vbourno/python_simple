# Iterates a list of fruits and returns the fruits with odd number of letters

# Declaration of the list
fruits = ["apple", "banana", "cherry", "fig", "melon"]

# Selects the fruits with names containing odd number of letters
odd_fruits = list(filter(lambda fruit: len(fruit) % 2 == 1, fruits))

# Creation of a list with the odd numbers of the names of the fruit
fruit_lengths = []
for fruit in odd_fruits:
   fruit_lengths.append(len(fruit))

#Output
print("Original list of fruits:", fruits)
print("Fruits with odd number of letters:", odd_fruits)
print("Odd numbers of letters:", set(fruit_lengths))
