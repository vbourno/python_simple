num = 10
my_list = [1, 2]

# prints memory address
print(id(num))
print(id(10))

print("-----------")

print(id(my_list))
print(id([1, 2]))
print(my_list is [1, 2])