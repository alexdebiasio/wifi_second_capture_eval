import Queue
import loader
import os

class ExperimentLoaderCreator():
    """ Create a loader object for each experiment in path """

    def __init__(self, path, experiment_queue):
        self.path = path
        self.experiment_queue = experiment_queue

    def fill_queue(self):
        exp_list = self.__get_experiment_list()

        for i in exp_list:
            self.experiment_queue.put(loader.Loader(self.path, i))

    def __get_experiment_list(self):
        exp_list = []
        for f in os.listdir(self.path):
            if f.endswith(".dat"):
                exp_list.append(f[:-4])
        return exp_list
