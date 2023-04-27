def get_formatted_date(day=1, month=1, year=2000):
    return f"{day:02d}/{month:02d}/{year:4d}"

def main():
    # positional arguments
    print(get_formatted_date())
    print(get_formatted_date(10))
    print(get_formatted_date(12, 4))
    print(get_formatted_date(27, 10, 2023))
    # keyword arguments
    print(get_formatted_date(year=2023))
    print(get_formatted_date(year=2023, day= 27, month=4))

if __name__ == '__main__':
    main()