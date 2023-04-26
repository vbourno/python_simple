# CRUD in lists

grades = [1, 4, 10, 7, 5]
print("Grades: ", grades)

# Append
grades.append(8)
print("Grades after append: ", grades)

# Update
grades[1] = 5
print("Grades after update: ", grades)

# Delete (remove)
grades.remove(1)
print("Grades after remove: ", grades)

# Search with value
if 10 in grades:
    print("Wow!")

# index()
if 10 in grades:
    position_to_update = grades.index(10)
    grades[position_to_update] = 9.5
print("Final grades list: ", grades)