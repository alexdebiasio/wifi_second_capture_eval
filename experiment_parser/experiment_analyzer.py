from scapy.all import *
import json
import statistics

CALIBRATION_PORT = [7146,7147]
EXPERIMENT_PORT = 3939


class ExperimentAnalyzer():

    #def __init__(self, exp, nodes_list=["00:14:a4:28:a6:4e", "00:03:c9:df:ed:81"], ap_addr=["10.0.0.37", "00:16:ce:27:79:43", "01:01:00:00:00:00"]):
    def __init__(self, exp, nodes_list=[ "00:03:c9:df:ed:81","00:14:a4:28:a6:4e"], ap_addr=["10.0.0.37", "00:16:ce:27:79:43", "01:01:00:00:00:00"]):
        self.exp = exp
        self.nodes_list = nodes_list
        self.ap_addr = ap_addr

    def __del__(self):
        del(self.exp)

    
    def analyze(self):
        print "=========================================================="
        print self.exp.info["test_id"]
        print "=========================================================="

        captures = self.__filter_unknown_nodes(self.exp.cap, set(self.nodes_list).union(set(self.ap_addr)))
        
        
        starttime, endtime = self.__get_experiment_bound(captures)

        if starttime == 0 or endtime == 0:
            raise ValueError("Corrupted pcap")


        captures = self.__filter_UDP_port(captures, set(CALIBRATION_PORT).union(set([EXPERIMENT_PORT])))

        node_pkt_list = []
        for i in self.nodes_list:
            node_pkt_list.append({
                "node": i,
                "exp_pkt": self.__extract_experiment_pkt(captures, i, starttime, endtime),
                "bad_fcs_pkt": self.extract_bad_fcs_pkt(captures, i ,starttime, endtime),
                "calibr_pkt": self.__extract_calibration_pkt(captures, i)
                })



        #construct response dict
        r = {
                "experiment_info" : self.exp.info,
                "node1" : {
                    "intensity" : self.__get_rssi_stat_from_pkt(node_pkt_list[0]["calibr_pkt"]),
                    "exp_pkt_count": len(node_pkt_list[0]["exp_pkt"]),
                    "tdma_counter" : self.exp.info["node1_tdma_counter"],
                    "bad_pkt_count": len(node_pkt_list[0]['bad_fcs_pkt']),
                        },
                "node2" : {
                    "intensity" : self.__get_rssi_stat_from_pkt(node_pkt_list[1]["calibr_pkt"]),
                    "exp_pkt_count": len(node_pkt_list[1]["exp_pkt"]),
                    "tdma_counter" : self.exp.info["node2_tdma_counter"],
                    "bad_pkt_count": len(node_pkt_list[1]['bad_fcs_pkt']),
                        }
            }
        try:
            r["node1"]["rx_rate"] = r["node1"]["exp_pkt_count"] / float(r["node1"]["tdma_counter"])
        except ZeroDivisionError:
            r["node1"]["rx_rate"] = -1.0

        try:
            r["node2"]["rx_rate"] = r["node2"]["exp_pkt_count"] / float(r["node2"]["tdma_counter"])
        except ZeroDivisionError:
            r["node2"]["rx_rate"] = -1.0

        delays = r["experiment_info"]["delays"]
        delays = delays[-2:] + delays[-4:-2]
        r["experiment_info"]["int_delays"] = int(delays, 16)
        r["experiment_info"]["tx_delays"] = int(delays, 16) - 0x80




        print json.dumps(r)

        return r



    
    def __get_experiment_bound(self, pkt_list):
        #get ap beacon
        beacon_list = [i for i in pkt_list if i[Dot11].subtype==8L]
        start = end = 0
        for i in beacon_list:
            if start == 0:
                #FIXME it requires that ssid does not contain "asd" substr
                if i.haslayer(Dot11Elt) and i[Dot11Elt][1].info == "asd":
                    start = i.time
            if end == 0:
                #FIXME it requires that ssid does not contain "bsd" substr
                if i.haslayer(Dot11Elt) and i[Dot11Elt][1].info == "bsd":
                    end = i.time
                    break
        return (start, end)
            


    def __filter_unknown_nodes(self, pkt_list, known_nodes):
        ''' Remove nodes not in self.nodes_list ''' 
        addr_set = set(known_nodes)
        return [ i for i in pkt_list if i.haslayer(Dot11) and ((i[Dot11].addr1 in addr_set)\
                or (i[Dot11].addr2 in addr_set))]

    def __filter_UDP_port(self, pkt_list, port_list):
        ''' Keep only UDP pkt with dport in port_list '''
        port_list = set(port_list)

        return [i for i in pkt_list if i.haslayer(UDP)\
                and i[UDP].dport in port_list]

    def __extract_calibration_pkt(self, pkt_list, node):
        ''' return calibration pkts of specific node '''
        return [i for i in pkt_list if i[UDP].dport in CALIBRATION_PORT\
                and i[Dot11].addr2 == node]

    def __extract_experiment_pkt(self, pkt_list, node, starttime, endtime):
        ''' return experiment pkt of specific node '''
        return  [j for j in self.__extract_window(pkt_list,starttime,endtime) if j[UDP].dport == EXPERIMENT_PORT and str(j[Dot11].addr2) == str(node)
                and (ord(str(j)[16]) & 0x40) != 0x40]
                #and hex(ord(str(j)[16])) != '0x40']

    def extract_bad_fcs_pkt(self, pkt_list, node, starttime, endtime):
        ''' return bad fcs pkt of specific node '''
        '''
        In [82]: hex(ord(str(b[5846])[16]))
        Out[82]: '0x40'
        '''
        return  [j for j in self.__extract_window(pkt_list,starttime,endtime) if j[UDP].dport == EXPERIMENT_PORT and str(j[Dot11].addr2) == str(node)
                and (ord(str(j)[16]) & 0x40) == 0x40]

    def __extract_window(self, pkt_list, start, end):
        return [i for i in pkt_list if i.time>start and i.time<end]

    def __get_rssi_stat_from_pkt(self, pkt_list):
        ''' Retrun (means, variance) of rssi '''
        values = [self.__extract_rssi(i) for i in pkt_list if self.__extract_rssi(i) != 0]

        return (statistics.mean(values), statistics.variance(values))


    def __extract_rssi(self,pkt):
        try: 
            return -(256-ord(pkt.notdecoded[-4:-3]))
        except:
            try:
                return pkt.rssi - 256 - 0xFFFFFF00
            except:
                return 0
