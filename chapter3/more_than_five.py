# Declaration of the list
cf = ["Coding", "Factory", "3", "October", "2023"]

"""
Returns the strings of the list that contain more than five chars.
"""
def more_than_five():
    return list(filter(lambda str: len(str) > 5, cf))

# Output
print("Original list:", cf)
print("Strings with more than five chars:", more_than_five())