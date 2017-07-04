#!/bin/bash

# this script should setup correctly the 4 nodes for experiments


echo "set AP"
ssh -F ssh_config w37 "/home/wireless/nodes/ap/init_ap.sh" 


echo "set sta1"
ssh -F ssh_config w39 "/home/wireless/nodes/station/init_station.sh"


echo "set sta2"
ssh -F ssh_config w34 "/home/wireless/nodes/station/init_station.sh"


echo "set sniffer"
ssh -F ssh_config w100 "/home/wireless/nodes/sniffer/init_sniffer.sh"




