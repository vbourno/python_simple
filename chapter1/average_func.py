# Gets 3 args and returns the average value

def get_average(num1, num2, num3):
    # block κώδικα
    total = num1 + num2 + num3
    average = total / 3
    return average

# Αρχικοποιώ τις μεταβλητές
a = 10
b = 15
c = 16

# Καλώ τη συνάρτηση και εκχωρώ το αποτέλεσμα σε μια μεταβλητή
result = get_average(a, b, c)

print("Average of", a, b, c, "is equal to:", "{:.2f}".format(result))