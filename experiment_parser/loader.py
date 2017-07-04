
import re
import sys
from scapy.all import *
import json
from experiment import *
import pickle


class Loader():

    def __init__(self, path, test_id):
        self.path = path
        self.test_id = test_id
        # do not ask... it just works... 
        self.raw_tdma_re = re.compile("((?P<node1>.*)i:[ ]+r57:[ ]+(?P<n1r1>[0-9A-Fa-f]{4})[ ]+r58:[ ]+(?P<n1r2>[0-9A-Fa-f]{4})\\n\\n)((?P<node2>.*)i:[ ]+r57:[ ]+(?P<n2r1>[0-9A-Fa-f]{4})[ ]+r58:[ ]+(?P<n2r2>[0-9A-Fa-f]{4})\\n\\n)")

    def load(self):
        try:
            self.__load_dat_file()
        except:
            print "Unable to load dat file: " + self.path + self.test_id + ".dat"
            raise

        try:
            self.__load_cap_file()
        except:
            print "Unable to load cap file: " + self.test_id
            raise
        
        return Experiment(self.test_parameters.copy(), self.cap_file)


    def __load_cap_file(self):

        self.cap_file = rdpcap(self.path + self.test_id + ".pcap") 

    def __load_dat_file(self):

        with open(self.path + self.test_id + ".dat", 'r') as f:
            info = json.loads(f.read())
        info.update(self.__parse_tdma_counter(info["raw_tdma_counters"]))
        self.test_parameters = info
        
    def __parse_tdma_counter(self, raw_data):

        match = self.raw_tdma_re.match(raw_data)
        r = match.groupdict()
        # it does not check inside node1 and node2 if the nodes are correct
        return {
                "node1_tdma_counter" : int( r["n1r1"] + r["n1r2"], base=16),
                "node2_tdma_counter" : int( r["n2r1"] + r["n2r2"], base=16)
                }
