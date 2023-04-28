fruits_first = ["Apple", " Banana", "Orange", "Mango", "Banana", "Strawberry", "Banana"]
fruits_second = ["Melon", "Orange", "Mango", "Banana", "Strawberry", "Pear"]

set_fruit1 = set(fruits_first)
set_fruit2 = set(fruits_second)

common_element = set_fruit1.intersection(set_fruit2)

print(common_element)