def my_add(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result

    Args:
    a (int) -- The first number to add.
    b (int) -- The second number to add.

    Returns:
    The sum of a and b.
    """
    return a + b

print("10 + 20:", my_add(10, 20))
print("Annotations:", my_add.__annotations__)
print("Docs:", my_add.__doc__)

help(my_add)