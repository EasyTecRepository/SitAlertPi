#!/usr/bin/env python3
# coding by Easy Tec
# based on: http://joe703.de/2021/02/28/abstandsmessung-mit-hc-sr04-ultraschallsensorsensor/

import RPi.GPIO as GPIO
import time

# sensor ports
SENSOR_TRIGGER = 23
SENSOR_ECHO = 24
PIN_output_LED_r = 16
PIN_output_LED_b = 20

# Define your Distance from your desk to the floor
def_distance =  900 # Better higher value than lower value! Note tolerance +/- of approx. 20 mm | in mm

# Speed and duration of blue light
duration = 2
speed = 0.08

# Time before stand-up
time_before_stand_up =  5 # in seconds | default: 30 min (18000 s)

### PLEASE DO NOT ADJUST ###

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_TRIGGER, GPIO.OUT)
GPIO.setup(SENSOR_ECHO, GPIO.IN)
GPIO.setup(PIN_output_LED_r, GPIO.OUT)
GPIO.setup(PIN_output_LED_b, GPIO.OUT)

measuring_max = 1               # in seconds
measuring_trig = 0.00001        # in seconds
measuring_paus = 10             # in seconds
measuring_factor = (343460 / 2)
distance_max = 4000        # Max value in mm
distance_max_err = distance_max + 1

def SENSOR_GetDistance():
    GPIO.output(SENSOR_TRIGGER, True)
    time.sleep(measuring_trig)
    GPIO.output(SENSOR_TRIGGER, False)
    #
    starttime = time.time()
    maxtime = starttime + measuring_max
    #
    while starttime < maxtime and GPIO.input(SENSOR_ECHO) == 0:
        starttime = time.time()
    #
    #
    stoptime = starttime
    #
    while stoptime < maxtime and GPIO.input(SENSOR_ECHO) == 1:
        stoptime = time.time()
    #
    if stoptime < maxtime:
        #
        my_time = stoptime - starttime
        #
        distance = my_time * measuring_factor
    else:
        # set fail value
        distance = distance_max_err
    #
    return int(distance)
#
def police_blue_light(duration, speed, pause_flag):
    starttime_blue_light = time.time()

    while time.time() - starttime_blue_light < duration and not pause_flag:
        GPIO.output(PIN_output_LED_r, GPIO.HIGH)
        GPIO.output(PIN_output_LED_b, GPIO.LOW)
        time.sleep(speed)
        GPIO.output(PIN_output_LED_r, GPIO.LOW)
        GPIO.output(PIN_output_LED_b, GPIO.HIGH)
        time.sleep(speed)
        GPIO.output(PIN_output_LED_b, GPIO.LOW)

    time.sleep(1)
#
def mainloop():
    try:
        pause_flag = False
        starttime_main = time.time()
        GPIO.output(PIN_output_LED_r, GPIO.LOW)
        GPIO.output(PIN_output_LED_b, GPIO.LOW)
        while True:
            Spacing = SENSOR_GetDistance()

            if Spacing >= distance_max:
                #
                print ("No Object found")
            else:
                #
                print ("Measured distance = %i mm" % Spacing)
                if Spacing < def_distance and (past_time := time.time() - starttime_main) >= time_before_stand_up:
                    print("Alert")
                    police_blue_light(duration, speed, pause_flag)
                    print("wait {} seconds".format(time_before_stand_up))
                    time.sleep(time_before_stand_up) # wait
            time.sleep(measuring_paus)

    # if detect keyboard interrupt
    except KeyboardInterrupt:
        print("Stopped by user")
        print("Cleanup GPIO...")
        GPIO.cleanup()

# Main Loop
mainloop()
