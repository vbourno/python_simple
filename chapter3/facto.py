# Factorial
def facto(n):
    if n < 0 : return 0
    if n in (0, 1) : return 1
    return n * facto(n - 1)

def main():
    n = 10
    print(f"facto({n}) = {facto(n)}")

main()