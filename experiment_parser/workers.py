#from multiprocessing import Queue
from experiment_analyzer import *
import Queue
import traceback
from abc import ABCMeta, abstractmethod


class Workers():
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        pass

class LoaderAnalyzerThread(Workers):
    
    def __init__(self, loader_queue, result_queue, wrong_experiment_queue):
        self.loader_queue = loader_queue
        self.result_queue = result_queue
        self.wrong_experiment_queue = wrong_experiment_queue

    def run(self):
        while True:
            try:
                load_obj = self.loader_queue.get(block=False)
                try:
                    
                    experiment = load_obj.load()

                except Exception as e:
                    print "Unable to load experiment " + load_obj.test_id
                    print e
                    self.wrong_experiment_queue.put({"test_id":load_obj.test_id, "when":"onload", "exception": str(e), "trace": traceback.format_exc() })
                    continue

                try:

                    analyzer_obj = ExperimentAnalyzer(experiment)
                    res = analyzer_obj.analyze()
                    self.result_queue.put(res)

                except Exception as e:
                    print "Unable to analyze an experiment"
                    print e
                    self.wrong_experiment_queue.put({"test_id":load_obj.test_id, "when":"onanalyze", "exception": str(e), "trace": traceback.format_exc() })

                finally:
                    # Force cleanup
                    del(analyzer_obj)
                    del(experiment)
            except Queue.Empty:
                pass
                #self.result_queue.put("DONE")
                #self.wrong_experiment_queue.put("DONE")
                #return

                
#REMOVE    ---DEPRECATED---
class ExpAnalyzerThread(Workers):

    def __init__(self, experiment_analyzer_queue, result_queue):
        self.experiment_analyzer_queue = experiment_analyzer_queue
        self.result_queue = result_queue

    def run(self):
        while True:
            exp_obj = self.experiment_analyzer_queue.get(block=True)
            if exp_obj == -1:
                self.result_queue.put(-1)
            else:
                try:
                    result = exp_obj.analyze()
                except Exception as e:
                    print "Unable to analyze an experiment"
                    print e
                    self.result_queue(-1)
                else:
                    self.result_queue.put(result)

