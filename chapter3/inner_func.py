# Inner func

def outer_func():
    print("Outer func started")

    # inner function
    def inner_func():
        print("Inner func ran")

    inner_func()

    print("Outer func ended")

def main():
    # outer_func()

    new_func_name = outer_func
    new_func_name()

main()