# Find common items in two lists and save in a new list without duplicates

fruits_first = ["Apple", " Banana", "Orange", "Mango", "Banana", "Strawberry", "Banana"]
fruits_second = ["Melon", "Orange", "Mango", "Banana", "Strawberry", "Pear"]

new_fruit_list = []

for fruit in fruits_first:
    if fruit in fruits_second and fruit not in new_fruit_list:
        new_fruit_list.append(fruit)

print("New fruit list:", new_fruit_list)