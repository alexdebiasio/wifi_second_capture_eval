#!/bin/bash


# calibration.sh PORT
# this script launch an iperf session for 5 sec in order to calibrate the received rssi


killall -s SIGKILL iperf


echo "Start calibration"


nohup iperf -c 172.16.0.37 -u -p $1 -t 1000 -b 20M >>/dev/null & 
sleep 5
killall -s SIGKILL iperf


echo "End calibration"
