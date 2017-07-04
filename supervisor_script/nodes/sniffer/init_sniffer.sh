#!/bin/bash

# init_sniffer.sh is responsible for raising a monitor interface and for set up the enviroment of the sniffer



mkdir -p /home/wireless/tests

sudo iw dev wlan0 interface add fish0 type monitor
sudo ifconfig wlan0 down
sudo ifconfig fish0 up
#sudo iw dev fish0 set channel 14
sudo iwconfig fish0 chan 14
