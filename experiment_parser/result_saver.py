import json
import Queue

def save_result_to_file(filename, good, bad):


    wrap_up = { "good_experiment" : good, "bad_experiment" : bad}

    json_str = json.dumps(wrap_up)
    print json_str

    try:
        with open(filename, 'w') as f:
            f.write(json_str)
        print "Result saved to disk"

    except:
        print "Problem in writing result to disk.\n" + json_str
'''
def save_result_to_file(filename, good_queue, bad_queue):

    good_res = from_queue_to_list(good_queue)
    bad_res = from_queue_to_list(bad_queue)

    wrap_up = { "good_experiment" : good_res, "bad_experiment" : bad_res }

    json_str = json.dumps(wrap_up)
    print json_str

    try:
        with open(filename, 'w') as f:
            f.write(json_str)
        print "Result saved to disk"

    except:
        print "Problem in writing result to disk.\n" + json_str
'''
def from_queue_to_list(q):
    tmp = []
    try:
        r = q.get(False)
        tmp.append(r)
    except Queue.Empty:
        return tmp
