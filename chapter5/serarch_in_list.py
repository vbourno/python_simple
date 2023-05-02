# Search with: in, index(), count()

nums = [1, 2, 3, 4, 5]

num_to_find = 20

# in operator
if num_to_find in nums:
    print("Found it")
else:
    print("Not found")

# method index()
try:
    index = nums.index(num_to_find)
    print("Found")
except ValueError as e:
    print("Value error:", e)

# method count()
count = nums.count(num_to_find)

if count > 0:
    print(f"{num_to_find} is present {count} times in the list")
else:
    print(f"{num_to_find} is not present in the list")