#!/usr/bin/env python

from scapy.all import *
import sys


def send_beacon(interface, vendor_field):

    bssid = "00:16:ce:27:79:43"
    srcmac = "01:01:00:00:00:00"
    dstmac = "ff:ff:ff:ff:ff:ff"  

    dot11hdr = Dot11(FCfield='to-DS',type=0x02, \
                subtype=0x20,addr1=bssid,addr2=srcmac,addr3=dstmac)


    pkt = RadioTap()\
                    /Dot11(subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=srcmac, addr3=bssid, SC=1111) \
                        / Dot11Beacon(cap=0x0401)                                                           \
                        / Dot11Elt(ID='SSID', info="Fenice")                                                    \
                        / Dot11Elt(ID='vendor', info=vendor_field)\
                        / Dot11Elt(ID='DSset', info=chr(15))
    sendp(pkt, iface=interface, count=5, verbose=True)


def main():
    if len(sys.argv) != 3:
        print "Usage: %s INTERFACE start|stop" % (sys.argv[0])
        sys.exit(1)

    # asd & bsd are magic string, don't ask.. :-)
    if sys.argv[2] == "start":
        send_beacon(sys.argv[1], "asd")
    else:
        send_beacon(sys.argv[1], "bsd")



if __name__ == "__main__":
    main()
