#!/bin/bash


#    stop_test: Questo script deve estrarre i contatori tdma
#                               dma_count1:FFFF,tdma_count2:FFFF


sudo killall -s SIGKILL iperf > /dev/null  2>&1


sudo readshm |tail -n2 | head -n1 | egrep -o  "r57:[ ]+[0-9A-F]{4}[ ]+r58:[ ]+[0-9A-F]{4}" 



