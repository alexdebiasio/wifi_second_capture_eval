#!/bin/bash

#This script upload a copy of the supervisor scripts to all the nodes

scp -F ssh_config -r nodes w37:
scp -F ssh_config -r nodes w34:
scp -F ssh_config -r nodes w39:
scp -F ssh_config -r nodes w100:
