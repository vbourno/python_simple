# Reverse a string

def get_reversed(arr):
    """
    Prints the reverse string.
    """
    if (arr == None):
        return []
    return arr[::-1]

def main():
    name = "Coding Factory"

    print(f"Reverse name: {get_reversed(name)}")

main()