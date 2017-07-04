#!/bin/bash


# stop_sniff.sh REPORT_STR REPORT_FILE
# send SIGINT to all tcpdump sessions and write REPORT_STR to REPORT_FILE

sudo killall -s SIGINT tcpdump
sleep 1
#echo $1 > $2
