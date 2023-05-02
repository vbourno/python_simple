# declare a list of grades
grades = [7, 5, 9, 10, 3]

# Map ()
upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]

print("Upscaled grades:", upscaled_grades)

upscaled_grades2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))

print("Upscaled grades 2:", upscaled_grades2)

# Without "else"?
# upscaled_grades3 = list(map(lambda grade: grade + 1 if grade <= 9, grades)) # expected 'else' (Pylance)

# Filter ()
passed_grades = [grade for grade in upscaled_grades if grade >= 5]

print("Passed grades:", passed_grades)

passed_grades2 = list(filter(lambda grade: grade >= 5, upscaled_grades))

print("Passed grades 2:", passed_grades2)