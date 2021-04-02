import random
import time

import os  #---> Need this to access envroment variables

def logging_example(message): #---> Create a wrapper around our print statement to determin if we should print or not based on envroment variable

    if os.getenv('print_setting')=="enable": 
        print(message) #---> this will only happen if we run export print_setting="enable" before the app runs. 

def count_cars(lotname): 


    logging_example("Starting to count cars")

    logging_example(lotname)

    four_door_cars=random.randint(0,9)

    logging_example("four_door_cars: " + str(four_door_cars))

    time.sleep(0.4)

    three_door_cars=random.randint(0,9)

    logging_example("three_door_cars: " + str(three_door_cars))

    time.sleep(0.4)

    total_cars = four_door_cars + three_door_cars

    logging_example("Total cars at " + lotname + ": " + str(total_cars))

    time.sleep(0.4)

    logging_example("done counting cars")

    return total_cars


if __name__ == "__main__":


    lotnames=["henry_ford", "buck_chevy", "jimmy_jeep"]
    all_cars=0

    logging_example("App started")

    logging_example("Counting cars in: ")
    logging_example("\n".join(lotnames))

    for lotname in lotnames: 
        lot_total=count_cars(lotname)
        all_cars=all_cars + lot_total

    print("Grand Total of all cars at all lots:")
    print(all_cars)