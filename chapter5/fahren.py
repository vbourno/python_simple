# F -> C
fahrenheit_temps = [32, 67, 90, 102, 75, 68, 55]

# create list celsius using list compr
celsius_temps = ["{:.2f}".format((temp-32)*5/9) for temp in fahrenheit_temps]

print("Celsius temps:", celsius_temps)