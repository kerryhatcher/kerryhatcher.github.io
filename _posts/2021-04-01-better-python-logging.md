---
title: "Better Python Logging"
date: 2021-04-01 01:00:00
description: Debugging can be hard and print everywhere isn't the best. See how to make logging better. 
featured_image: '/images/better-python-logging/chris-ried-ieic5Tq8YMk-unsplash'
author: kerry
---

Is that variable getting set correctly? Why is your loop sometimes failing? Debugging in general can be a pain and most folks start off by sprinkling `print()` statements all over there code. Hello I'm Kerry and sometimes I abuse `print()` myself. So lets talk about how to improve the situation starting with the following example:

```python
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
```

See all those `print()` statements? They are handy since you can see how the program is handling all of the steps as it goes along. This way if something is adding up right you can see where it went wrong. This is the most basic form of logging, just printing to the standard output of the application. Saving and processing that log can then be handled by simply piping that to a text file and then doing something with that outside of the app itself.

Logging is an important feature for all applications and scripts. Many times its just an outgrowth of the creative development process or debugging after the fact. Either way you need a way to dynamically change the volume and detail of the output of your apps without resorting to commenting out `print()` statements. Python already has some great builtin feature to help with this but there is a great module out there that really sets the bar. More on that later. For now lets take our previous example and make it a little better.

```python
import random
import time

import os  #---> Need this to access environment variables

def logging_example(message): #---> Create a wrapper around our print statement to determine if we should print or not based on environment variable

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
```

Thats a little bit better. Now we can control just how verbose our output is based on an environment variable. It would be better if we could have multiple levels of output and even send save the output of different levels to a text file or something without printing a bunch of stuff to the command line for the user to see. Let me introduce you to Loguru. This is also known as logging level. Usually errors are always logged so those would be at a high level, whereas debug statements are common throughout an application and are considered low level. This way your logs only show the minimal information required while allowing the threshold for what is minimal to be easily configured.  

## Loguru

![Loguru project logo](https://raw.githubusercontent.com/Delgan/loguru/master/docs/_static/img/logo.png)

Loguru makes all that we've talked about so far easy and automatic. An extremely over simplistic explanation is that Loguru works like the `logging_example("Here is a simple message")` function from the previous example. It has a lot of flexibility and customization options however it is still just as simple to use. The only added mandatory extra "config" is to pass what logging level a message is. So for example: `logger.debug("Here is a simple message")`.

Loguru also gives a lot of really great information back on our log messages. Lets take the previous example and update it with Loguru.

```python
import random
import time

from loguru import logger

logger.add("demo.log", rotation="1 week", retention="5 weeks", compression="zip")  


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

```

Now lets compare the output from the previous example and the current one.

Previous:

```App started
Counting cars in: 
henry_ford
buck_chevy
jimmy_jeep
Starting to count cars
henry_ford
four_door_cars: 6
three_door_cars: 6
Total cars at henry_ford: 12
done counting cars
```

Current:

```s
2021-04-02 05:48:58.715 | DEBUG    | __main__:<module>:45 - App started
2021-04-02 05:48:58.715 | INFO     | __main__:<module>:47 - Counting cars in: henry_ford,buck_chevy,jimmy_jeep
2021-04-02 05:48:58.716 | DEBUG    | __main__:count_cars:12 - Starting to count cars
2021-04-02 05:48:58.716 | DEBUG    | __main__:count_cars:14 - henry_ford
2021-04-02 05:48:58.716 | DEBUG    | __main__:count_cars:18 - four_door_cars: 8
2021-04-02 05:48:59.117 | DEBUG    | __main__:count_cars:24 - three_door_cars: 1
2021-04-02 05:48:59.518 | DEBUG    | __main__:count_cars:30 - Total cars at henry_ford: 9
2021-04-02 05:48:59.919 | DEBUG    | __main__:count_cars:34 - done counting cars
```

Loguru automatically gives us a timestamp, log level, and even the code location of the message. This make fixing issues and understanding whats happing in your code exponentially easier.

### What to do with your logs

Now that you have some handy logs you need to save them somewhere. Printing the app's log to the screen is handy but you need some sort of retention especially if the app is running in the background or automatically. Loguru makes adding a destination for your logs super simple via the `logger.add()` function.

#### **Log File**

The most basic example of this saving the logs to a log file. Simply add `logger.add("app.log")` to the application and a copy of your logs will be saved in a text file named `app.log`. The most recent example above already has this setup but with a few extra options.

`logger.add("demo.log", rotation="1 week", retention="5 weeks", compression="zip")`

Those extra options tell Loguru to rotate the log file every week, keep 5 weeks worth of files, and compress the files to save space. Log rotation just means taking the current log file and saving it as a different file and start over in a empty text file. This makes finding a log from sometime in the past easier and helps to prevent your hard drive from filling up from log data.

#### **Log Service**

Even better than saving the logs to the local computer is shipping them off to a service. This has the added advantage of surviving any sort of failure of the host computer. So if your app had a but that deleted every file on the hard drive because of a typo the logs will still exist elsewhere.

My default log service is AWS Cloudwatch Logs. There are plenty of "better" options out there but most of my work is done in AWS so it is generally easier for me to use it. To get those logs into AWS we will use a package called `Watchtower`. This all assumes you have an AWS account which is free to setup and many services have free tiers of use. Also you will need to ensure you have setup your AWS credentials on the computer where your app is running.

Lets go update our example with watchtower. It is as simple as adding `logger.add(watchtower.CloudWatchLogHandler(log_group="/kh.com/better_py_logging", stream_name="demotime"))` We can leave the bit in that saves the logs to the local hard drive as well.

```python
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

```

Now if we log into AWS we can see our logs even if the host computer fails in some way. This is real handy if your app is running on a remote computer that you don't have remote control over. You can also setup monitor and alerts to go off based on patterns in the logs.

![screenshot of log data in AWS](/images/better-python-logging/aws_cw_logs.png)


---

Proper logging in Python can be added to any project no matter the size or complexity. Doing so will save you plenty of time and fustration. 