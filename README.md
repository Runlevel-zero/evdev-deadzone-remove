# evdev-deadzone-remove
Simple script to automate the removal of unwanted deadzones silently applied to event driven axis. 


There are better ways to fix this.


A udev rule is probably more appropriate for your needs
but if you are stubborn this might save you some time.
You must edit the script for your configuration. You can find your device path at
```/dev/input/by-id/```
