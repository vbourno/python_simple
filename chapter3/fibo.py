# Fibonacci
def fibo(n):
    if n in (0, 1):
        return n
    
    return fibo(n - 1) + fibo(n - 2)

def main():
    n = 8
    print(f"fibo({n}) = {fibo(n)}")

main()