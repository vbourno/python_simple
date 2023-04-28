list1 = [10, 20, 30, 40, 50]

list2 = list1

print("Id of list1:", id(list1))
print("Id of list2:", id(list2))

list1[0] = 777

print("List1:", list1)
print("List2:", list2)