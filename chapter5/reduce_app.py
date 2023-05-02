# Reduce app
import functools
# from functools import reduce

# list of sales
sales = [8000.00, 9500.50, 12200.00, 4000.00]

total_of_sales = functools.reduce(lambda x, y: x + y, sales)

print("Total of sales: {:.2f} \u20AC".format(total_of_sales))