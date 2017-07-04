#!/bin/bash
cd /lib/firmware/b43
sudo killagents.sh
make && echo "Compilato"
sudo rmmod b43 && echo "modulo rimosso"
sudo modprobe b43 qos=0 && echo "modulo caricato"
sudo ifconfig wlan0 172.16.0.39 up && echo "ifconfig"
sudo wpa_supplicant -iwlan0 -B -c /home/wireless/wpasupplicant.conf && echo "wpa"
sudo writeshm 0xFF0 0x4000 && echo "shm"
sudo writeshm 0xFF2 0xFF0F && echo "shm"
sudo iwconfig wlan0 rate 54M
sudo arp -i wlan0 -s 172.16.0.37 00:16:ce:27:79:43 
