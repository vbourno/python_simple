# String indexing and slicing
message = input("Please give me a message: ") # Coding Factory

print(message[0]) # C
print(message[len(message) - 1], " - ", message[-1]) # y - y

# Τα πέντε πρώτα γράμματα
print(message[0:5]) # Codin

# Από τα γράμματα -> Coding
print(message[:6]) # ίδιο με [0:6]

# Ολόκληρη τη συμβολοσειρά
print(message[:])  # message[0:len(message) - 1]

# Τα γράμματα που βρίσκονται σε ζυγό index
print(message[::2])