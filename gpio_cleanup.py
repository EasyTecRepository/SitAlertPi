#!/usr/bin/env python3
import RPi.GPIO as GPIO
#
SENSOR_TRIGGER = 23
SENSOR_ECHO = 24
PIN_output_LED_r = 16
PIN_output_LED_b = 20
#
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_TRIGGER, GPIO.OUT)
GPIO.setup(SENSOR_ECHO, GPIO.IN)
GPIO.setup(PIN_output_LED_r, GPIO.OUT)
GPIO.setup(PIN_output_LED_b, GPIO.OUT)
GPIO.cleanup()
