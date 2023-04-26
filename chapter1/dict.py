# CRUD functions  on dicts

# NOT to do
# d = {1:True, "one":"ONE", "PI":3.14}

# Populate a dictionary
products = {1:"apples", 2:"bananas", 3:"pears"}
print("Dict: ", products)

# Insert
products[4] = "oranges"
print("Dict after insert 'oranges: ", products)

# Update
products[1] = "melon"
print("Dict after update 'key[1]' -> 'melon': ", products)

# Delete
del products[2]
print("Dict after deleting key-value pair with key = 2: ", products)

# Access a specific key:value pair
print("Access a specific key:value pair key = 4: ", products[4])
