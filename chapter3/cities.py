# map() function

def main():
    cities = ["london", "paris", "barcelona", "athens"]

    cap_cities = list(map(lambda city: city.title(), cities))

    cap_lengthy_cities = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))

    print("Cap cities:", cap_cities)

    print("Cap lengthy cities", cap_lengthy_cities)

main()