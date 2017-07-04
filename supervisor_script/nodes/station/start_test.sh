#!/bin/bash


#    start_test: Questo script deve resettare i contatori TDMA sulla shared memory (writeshm), e settare i valori corretti dix_power, cli_delay e bitmask
#                        infine deve mandare un pacchetto UDP sulla porta 7144 contenente il seguenti campi:
#                               xpower:00,delay:FFFF,bitmask:FFFF,rate:00
#
# ./start_test.sh TX_POWER CLI_DELAY BITMASK RATE

#/home/wireless/script_che_fa_tutto_quello_che_deve_fare.sh
killall -s SIGKILL iperf


writeshm 0xFF4 0x0100 && echo "Counter resetted"

/home/wireless/nodes/station/settxpower.sh  $1 && echo "Power fixed"
iwconfig wlan0 rate $4


writeshm 0xFF0 $2 && echo "Delay setted"
writeshm 0xFF2 $3 && echo "Bitmask setted"

#str=$(python /home/wireless/nodes/build_udp_start_pkt.py $1 $2 $3 $4)
#echo $str
#sleep 1
#echo $str > /dev/udp/10.0.0.100/7144 && echo "spedito"
sleep 1
echo "Start calibration interval"

/home/wireless/nodes/station/calibration.sh 7146


echo "Launch iperf"
nohup iperf -c 172.16.0.37 -u -p 3939 -t 1000 -b 20M >>/dev/null & 

echo "Done"

