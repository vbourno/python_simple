from collections import deque # as d

garage = deque() # create a deque

# simulation of cars arriving at the garage
garage.append("Car1")
garage.append("Car2")
garage.append("Car3")
garage.append("Car4")

# print current state of the garage (time1)
print("(time1) Current state og thw garage:", list(garage))

# simulate a car leaving the garage
car_left = garage.popleft()

# simulation of cars arriving at the garage
garage.append("Car5")
garage.append("Car6")

# print current state of the garage (time2)
print("(time2) Current state og thw garage:", list(garage))
print("Last car left the garage:", car_left)