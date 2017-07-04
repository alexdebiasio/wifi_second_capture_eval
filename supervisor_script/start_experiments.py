#!/usr/bin/python
import itertools
import subprocess
import time
import json

TEST_DURATION = 60 
STA1_DELAY = "0x8000"
ap = "10.0.0.37"
sta1 = "10.0.0.39"
sta2 = "10.0.0.34"
sniffer = "10.0.0.100"
user = "root"
#bitmask = "0xFF0F"
bitmask = "0xFFFF" # bigger bitmask for high delay experiment
cmd_path = "/home/wireless/nodes"

stations = [sta1, sta2]



#FIXME Please Alex, parse the experiments configuration from a file....
# test finali 4 maggio
intensity_levels = [("1","10")]
delays = ["0x1001"]
tx_rate = ["11M"]


# ap command
def call_beacon(sta, cmd):
    if cmd == "start":
        cmd_str = 'ssh %s@%s -F ssh_config "%s/beacon_send.py fish0 start"' % (user, sta, cmd_path)
    elif cmd == "stop":
        cmd_str = 'ssh %s@%s -F ssh_config "%s/beacon_send.py fish0 stop"' % (user, sta, cmd_path)
    subprocess.call(cmd_str, shell=True)

def send_start_beacon_from_ap():
    call_beacon(ap, "start")

def send_stop_beacon_from_ap():
    call_beacon(ap, "stop")

# stations command
def get_tdma_counter_from_sta(sta):
    cmd_str = 'ssh %s@%s -F ssh_config "%s/station/tdma_report.sh"' % (user, sta, cmd_path)
    return subprocess.check_output(cmd_str, shell=True)

def call_start_test(sta, int_lev, delay, rate):
    cmd_str = 'ssh %s@%s -F ssh_config "%s/station/start_test.sh  %s %s %s %s"' % (user, sta, cmd_path, int_lev, delay, bitmask, rate)
    print cmd_str
    #return Popen object in order to be able to wait until it finishes
    return subprocess.Popen(cmd_str, shell=True)

def call_stop_test(sta):
    cmd_str = 'ssh %s@%s -F ssh_config "%s/station/stop_test.sh"' % (user, sta, cmd_path)
    #return Popen object in order to be able to wait until it finishes
    return subprocess.Popen(cmd_str, shell=True)


# sniffer command
def start_sniffer(test_id):
    cmd_str = 'ssh wireless@%s -F ssh_config "%s/sniffer/start_sniff.sh fish0 %s "' % (sniffer, cmd_path, test_id)
    print cmd_str
    subprocess.Popen (cmd_str, shell=True)

def stop_sniffer(test_id, intensity, delays, bitrate):
    # get tdma counter from stations
    tdma_stat = ""
    for i in stations:
        tdma_stat = tdma_stat + i + "i: " +  get_tdma_counter_from_sta(i) + "\n"
    test_info = {
            "intensity" : intensity,
            "delays" : delays,
            "bitrate" : bitrate,
            "raw_tdma_counters" : tdma_stat,
            "test_id" : test_id
            }

    f_path = "/home/wireless/tests/%s" % (test_id)
    cmd_str = """ssh wireless@%s -F ssh_config '%s/sniffer/stop_sniff.sh'""" % (sniffer, cmd_path)
    with open("./test_dat/%s" % (test_id), 'w') as f:
        json.dump(test_info,f)
    subprocess.call (cmd_str, shell=True)



def main():

    for i, d, r in itertools.product(intensity_levels,delays, tx_rate):
        #sta1 must be called with the same delay every time
        print "======================================="
        print "new test with param %s %s %s" %(i,d,r)
        # create unique id of test
        test_id = "TEST_intensity1_%s_intensity2_%s_delay_%s_rate_%s" % (i[0],i[1],d,r)
        #start sniffer
        start_sniffer("/home/wireless/tests/"+test_id+".pcap")

        sta1_child = call_start_test(sta1, i[0], STA1_DELAY, r)
        sta2_child = call_start_test(sta2, i[1], d, r)
        sta1_child.wait()
        sta2_child.wait()
        time.sleep(1)
        # start test
        send_start_beacon_from_ap()
        print "Start"
        time.sleep(TEST_DURATION)
        send_stop_beacon_from_ap()
        print "Finish"
        
        wait_list = []
        for s in stations:
            wait_list.append(call_stop_test(s))
        for j in wait_list:
            j.wait()
        stop_sniffer(test_id + ".dat", i, d, r)
        print "end of this test"


if __name__ == '__main__':
    main()
