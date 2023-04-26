# Set example 02
# add(), remove()

# Δήλωση ενός συνόλου

s = {5, 10, 10, 10, 5, "Coding", 3.14, True, "Factory"}

print("Set after poppulation: ", (s))
print(len(s))

# add some items
s.add(True)
print("1. Set after add: ", s)

s.add(100)
print("2. Set after add: ", s)

#remove
s.remove(True)
print("Set after remove 'True': ", s)

# check with membership operator: in
print("Check if 10 exists: ", 10 in s)
