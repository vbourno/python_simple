# Set operators
bag1 = {"A1", "A2", "A3", "A4", "BA1"}
bag2 = {"A1", "A2", "B3", "B4", "BB2"}

common_elements = bag1 & bag2
all_elements = bag1 | bag2
diff1 = bag1 - bag2
diff2 = bag1 ^ bag2

print("bag1:", bag1)
print("bag2:", bag2)
print("common elements:", common_elements)
print("all elements:", all_elements)
print("diff1:", diff1)
print("diff2:", diff2)