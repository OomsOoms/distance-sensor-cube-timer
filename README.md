# distance-sensor-cube-timer

A rubiks cube timer using a distance sensor and a raspberry pi 4, and possibly the pi pico to reduce size and cost.

## How to use

Download the folder 'distance-sensor-cube-timer' and run the python script 'timer' to start using the timer.

The electronics to make this consist of a raspberry pi 4 (I will be looking into using a pi pico), a bread board, jumper cables and a 
[Distance sensor](https://thepihut.com/products/ultrasonic-distance-sensor-hcsr04?variant=1054704288&currency=GBP&utm_medium=product_sync&utm_source=google&utm_content).
Then follow the diagram below to connect the sensor to the pi.

![Distance sensor wiring](https://tutorials-raspberrypi.de/wp-content/uploads/2014/05/ultraschall_Steckplatine.png)
[How to use the distance sensor](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)

All the times and averages will be stored in /distance-sensor-cube-timer/times.txt'.

you can edit the file 'config.py' to chnage the delay, activation distance and average size.

To start and stop the timer hold and object infront of the sensor, it must be within the distance set by 'config.py'in cm for it to register. hold the object
infront of the sensor the amout of time set in 'config.py', when removed the timer will start, to stop the timer put and object back infront of the sensor, then repeat.

you can change the input method by impoorting another module, make sure it outputs True and False, for example, when there is something infront of the sensor it outputs True.

## Contribution

If you want to contribute to the project please follow these

* All variables must be written in snake case e.g. distance_sensor
* classes must be writen in camel case
* Please use double quotes for strings
* Make use of white sapce to make code more readable
* Comment where necessary to add clarification

This project uses [semantic versioning](https://semver.org/)
