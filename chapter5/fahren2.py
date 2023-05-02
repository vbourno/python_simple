# F -> C
fahrenheit_temps = [32, 67, 90, 102, 75, 68, 55]

# create generator
celsius_temps = ("{:.2f}".format((temp-32)*5/9) for temp in fahrenheit_temps)

for celsius_temp in celsius_temps:
    print(celsius_temp, end=" ")