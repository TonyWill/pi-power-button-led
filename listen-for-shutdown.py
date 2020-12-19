#!/usr/bin/env python3

from gpiozero import LED, Button
import subprocess

led = LED(4)
power_button = Button(3)
led.on()

power_button.wait_for_press()
led.blink(0.1,0.1)
subprocess.call(['shutdown', '-h', 'now'], shell=False)
