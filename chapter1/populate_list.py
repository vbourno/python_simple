# List populate
ages = [37, 42, 22, 27] #[], list()

# Iterate the list
for index, age in enumerate(ages):
    print(f"ages[{index}] is {age}")

print("-----")

# Enhanced for
for age in ages:
    print(age)

# range - question
for index, i in enumerate(range(5), start=1): # 0, 1, 2, 3, 4
    print(index, i)