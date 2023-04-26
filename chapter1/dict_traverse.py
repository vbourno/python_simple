# Dict traverse

# Populate a dictionary
products = {1:"apples", 2:"bananas", 3:"pears"}

# Traverse the keys of dict with keys()
for key in products.keys():
    print(key)

# Traverse the keys - value pairs of dict with keys()
for key in products.keys():
    print(key,":", products[key])

# Traverse the values of dict with values()
for value in products.values():
    print(value)

# Traverse the keys - value pairs of dict with items()
for key, value in products.items():
    print(key,":", value)