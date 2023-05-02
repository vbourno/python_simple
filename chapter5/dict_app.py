from functools import reduce

quarters = ['A', 'B', 'C', 'D']
prices = [1000, 2000, 1800, 1500]

sales = dict(zip(quarters, prices))

print(sales)
for key, value in sales.items():
    print(key, ":", value)

filtered_sales = dict(filter(lambda quarter_tuple: quarter_tuple[1] >= 1500, sales.items()))

print("filtered sales:", filtered_sales)

quarters_tax = {key: value * 0.2 for key, value in sales.items()}

print("quarters tax:", quarters_tax)

total_year_sales = reduce(lambda x, y: x + y, sales.values())

print("total year sales:", total_year_sales)