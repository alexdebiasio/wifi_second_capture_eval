


class Experiment():
    def __init__(self, info, cap):
        self.info = info
        self.cap = cap

    def __del__(self):
        del(self.cap)
