#!/usr/bin/python

import json

import sys


def main():

    if len(sys.argv) != 3:
        print "Usage: %s JSON_INPUT CSV_OUTPUT" % (sys.argv[0])
        sys.exit(-1)

    with open(sys.argv[1], 'r') as f:
        json_data = json.load(f)

    json_data = json_data["good_experiment"]
    node = "node2"


    csv_fields = ["intensity_diff", "delay",  "theoric_intensity", "success_rate_of_first", "success_rate_of_second"]

    with open(sys.argv[2], 'w') as f:
        f.write(','.join(csv_fields))
        f.write('\n')
        for i in json_data:
            intensity = int(i["node2"]["intensity"][0]) - int(i["node1"]["intensity"][0])

            theoric_intensity = int(i["experiment_info"]["intensity"][1]) - int(i["experiment_info"]["intensity"][0])
            delay = i['experiment_info']["int_delays"]
            succ_rate1 = i["node1"]["rx_rate"]
            succ_rate2 = i["node2"]["rx_rate"]
            f.write(','.join([str(intensity), str(delay), str(theoric_intensity),  str(succ_rate1), str(succ_rate2)]))
            f.write('\n')

if __name__ == "__main__":
    main()

'''


{
        "node1": {
            "exp_pkt_count": 1,
            "rx_rate": 0.0005219206680584551,
            "intensity": [-76.49458911058505, 0.3328812534312061],
            "tdma_counter": 1916
        },
        "node2": {
            "exp_pkt_count": 1827,
            "rx_rate": 0.9530516431924883,
            "intensity": [-72.17469050894086, 0.604427417857454],
            "tdma_counter": 1917
        },
        "experiment_info": {
            "raw_tdma_counters": "10.0.0.39i: r57: 0000  r58: 077C\n\n10.0.0.34i: r57: 0000  r58: 077D\n\n",
            "node1_tdma_counter": 1916,
            "delays": "0xa000",
            "intensity": ["14", "15"],
            "node2_tdma_counter": 1917,
            "test_id": "TEST_intensity1_14_intensity2_15_delay_0xa000_rate_12M.dat",
            "bitrate": "12M"
        }
'''
