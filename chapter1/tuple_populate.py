# Populating a tuple

ages = (30, 40, 25, 27)

# print(type(ages))

# Απλή for
for index, age in enumerate(ages):
    print(f"{index} : {age}")

# Enhanced for
for age in ages:
    print(age)