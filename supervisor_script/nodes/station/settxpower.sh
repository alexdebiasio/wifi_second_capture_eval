#!/bin/bash

#sblocco UDP porta 20000
echo "asdf" > /dev/udp/172.16.0.37/20000
#setto la potenza del tx
iwconfig wlan0 txpower $1

echo "Fix power with 10 second of iperf"
nohup iperf -c 172.16.0.37 -u -p 7148 -t 1000 -b 20M  &
sleep 10
echo "end of Fix power with 10 second of iperf"
killall -s SIGKILL iperf

#blocco UDP sulla porta 1000
echo "asdgf" >/dev/udp/172.16.0.37/10000

