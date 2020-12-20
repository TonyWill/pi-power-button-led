#!/usr/bin/env python3

from gpiozero import PWMLED, Button
import subprocess

led = PWMLED(4)
power_button = Button(3)
led.pulse(1,2)

power_button.wait_for_press()

subprocess.call(['shutdown', '-h', 'now'], shell=False)
