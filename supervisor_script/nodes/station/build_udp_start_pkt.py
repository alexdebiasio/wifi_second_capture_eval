#!/usr/bin/python 


import sys

tx_pwr = sys.argv[1]
cli_delay = sys.argv[2]
bitmask = sys.argv[3]
rate = sys.argv[4]

s = "txpower:%d,delay:%s,bitmask:%s,rate:%s"
s = s % (int(tx_pwr), cli_delay[2:], bitmask[2:], int(rate[:-1]))


sys.stdout.write(s)
sys.stdout.flush()
sys.exit()
