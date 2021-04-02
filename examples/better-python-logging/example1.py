import random
import time

def count_cars(lotname): 

    print("Starting to count cars")

    print(lotname)

    four_door_cars=random.randint(0,9)

    print("four_door_cars: " + str(four_door_cars))

    time.sleep(0.4)

    three_door_cars=random.randint(0,9)

    print("three_door_cars: " + str(three_door_cars))

    time.sleep(0.4)

    total_cars = four_door_cars + three_door_cars

    print("Total cars at " + lotname + ": " + str(total_cars))

    time.sleep(0.4)

    print("done counting cars")

    return total_cars


if __name__ == "__main__":
    lotnames=["henry_ford", "buck_chevy", "jimmy_jeep"]
    all_cars=0

    print("App started")

    print("Counting cars in: ")
    print(*lotnames, sep = "\n")

    for lotname in lotnames: 
        lot_total=count_cars(lotname)
        all_cars=all_cars + lot_total

    print("Grand Total of all cars at all lots:")
    print(all_cars)