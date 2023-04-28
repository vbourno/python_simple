# Separator
def join_args(separator, *args):
    """
    This function returns a string using separator
    """
    return separator.join(args)

def main():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    sep = "-"

    new_string = join_args(sep, *days)

    print(new_string)

main()