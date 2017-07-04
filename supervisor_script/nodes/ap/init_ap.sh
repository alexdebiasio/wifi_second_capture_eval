#!/bin/bash

sudo modprobe b43 qos=0

sudo ifconfig wlan0 172.16.0.37 up

sudo hostapd -B /home/wireless/hostapd.conf

sudo iw dev wlan0 interface add fish0 type monitor

sudo ifconfig fish0 up
