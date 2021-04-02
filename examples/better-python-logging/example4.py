import random
import time

from loguru import logger
import watchtower

logger.add("demo.log", rotation="1 week", retention="5 weeks", compression="zip")  
logger.add(watchtower.CloudWatchLogHandler(log_group="/kh.com/better_py_logging", stream_name="demotime"))

def count_cars(lotname): 


    logger.debug("Starting to count cars")

    logger.debug(lotname)

    four_door_cars=random.randint(0,9)

    logger.debug("four_door_cars: " + str(four_door_cars))

    time.sleep(0.4)

    three_door_cars=random.randint(0,9)

    logger.debug("three_door_cars: " + str(three_door_cars))

    time.sleep(0.4)

    total_cars = four_door_cars + three_door_cars

    logger.debug("Total cars at " + lotname + ": " + str(total_cars))

    time.sleep(0.4)

    logger.debug("done counting cars")

    return total_cars


if __name__ == "__main__":


    lotnames=["henry_ford", "buck_chevy", "jimmy_jeep"]
    all_cars=0

    logger.debug("App started")

    logger.info("Counting cars in: " + ",".join(lotnames))


    for lotname in lotnames: 
        lot_total=count_cars(lotname)
        all_cars=all_cars + lot_total

    logger.info("Grand Total of all cars at all lots:")
    logger.info(all_cars)
