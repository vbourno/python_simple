# String traverse example
s = input("Give me your name: ")

# Απλή for
for i in range(len(s)):
    print(s[i], end=" ")
print()

# Enhanced for
for char in s:
    print(char, end="")