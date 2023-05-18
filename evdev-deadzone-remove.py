#!/bin/python3
import sys
import subprocess

# This script automates the process of removing an erronous 6% deadzone added by
# evdev when handling event driven axis. This deadzone can bee seen in the
# calibration data from $evdev-joystick --showcal <device>

# Device ID ***can be found at /dev/input/by-id/
# Comment out or add new devices as needed, ensure you add/remove another loop
device1 = "/dev/input/by-id/usb-VIRPIL_Controls_20230328_L-VPC_Throttle_MT-50CM3_FF-event-joystick"
device2 = "/dev/input/by-id/usb-VKB-Sim_©_Alex_Oz_2021_VKBsim_Gladiator_EVO_R-event-joystick"
device3 = "/dev/input/by-id/usb-VKB-Sim_©_Alex_Oz_2021_VKBsim_T-Rudder-event-joystick"

#Ensure all axis are covered
axisCount1 = "6"
axisCount2 = "8"
axisCount3 = "4"


for axis in range(6):
    command = ["evdev-joystick", "--evdev", device1, "--axis", str(axis), "--deadzone", "0"]
    # Capture and print output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
    # Loop through standard out
    for line in process.stdout:
        print(line, end="")

for axis in range(8):
    command = ["evdev-joystick", "--evdev", device2, "--axis", str(axis), "--deadzone", "0"]
    # Capture  output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
    # Loop through standard out
    for line in process.stdout:
        print(line, end="")

for axis in range(4):
    command = ["evdev-joystick", "--evdev", device3, "--axis", str(axis), "--deadzone", "0"]
    # Capture and print output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
    # Loop through standard out
    for line in process.stdout:
        print(line, end="")
