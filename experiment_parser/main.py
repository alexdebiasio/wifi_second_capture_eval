#!/usr/bin/python2.7

import multiprocessing
import workers
import experiment_loader_creator
import sys
import result_saver
from experiment import *
from scapy.all import  *





def main():

    if len(sys.argv) != 4:
        print "Usage: %s EXPERIMENTS_PATH OUTPUT_FILE NUMBER_OF_THREAD" % (sys.argv[0])
        sys.exit(-1)

    NUMBER_OF_WORKERS = int(sys.argv[3])

    loaders_queue = multiprocessing.Queue()
    exp_loader = experiment_loader_creator.ExperimentLoaderCreator(sys.argv[1], loaders_queue)
    exp_loader.fill_queue()
    number_of_test = loaders_queue.qsize()
    print "Number of test to analyze: ", number_of_test
    result_queue = multiprocessing.Queue(number_of_test)
    wrong_experiment_queue = multiprocessing.Queue(number_of_test)



    worker_list = []
    thread_list = []

    good_res = []
    bad_res =[]

    for i in range(NUMBER_OF_WORKERS):
        worker_list.append(workers.LoaderAnalyzerThread(loaders_queue, result_queue, wrong_experiment_queue))

    #spawn some process

    for i in worker_list:
        thread_list.append(multiprocessing.Process(target=i.run))

    for i in thread_list:
        i.start()

    '''
    #wait until all finishes
    for i in thread_list:
        i.join()
    '''
    while number_of_test != 0:
        try:
            good_res.append(result_queue.get(timeout=1))
            number_of_test -= 1
        except:
            pass
        try:
            bad_res.append(wrong_experiment_queue.get(timeout=1))
            number_of_test -= 1
        except:
            pass

    #write result

    result_saver.save_result_to_file(sys.argv[2], good_res, bad_res)

    # terminate workers (con un botto in testa)

    for i in thread_list:
        i.terminate()






if __name__ == "__main__":
    main()
