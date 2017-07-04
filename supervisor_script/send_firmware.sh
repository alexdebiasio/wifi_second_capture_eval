#!/bin/bash

#This script upload the patched firmware to the two nodes

scp -F ssh_config ../firmware/ucode5.asm root@w34:/lib/firmware/b43
scp -F ssh_config ../firmware/ucode5.asm root@w39:/lib/firmware/b43
