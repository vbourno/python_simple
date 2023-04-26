# Αριθμό ημερών -> .. έτη, .. μήνες, .. μέρες

# Giving total days
total_days = 999

# Calculate the number of years
years = total_days // 365

# Calculate the remaining number of days (- years)
days_remaining = total_days - (years * 365)

# Calculate the number of months
months = days_remaining // 30

# Calculate the remaining days (- months)
days = days_remaining - (months * 30)

# Printing the results
print(f"{years} έτη, {months} μήνες, {days} ημέρες")