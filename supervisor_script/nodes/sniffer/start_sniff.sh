#!/bin/bash

# start_sniff.sh INTERFACE FILENAME
# start a tcpdump session saving record to filename

sudo tcpdump -i $1 -XXX -nn -s 0 -w $2 &
