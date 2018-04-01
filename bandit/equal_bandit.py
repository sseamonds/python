import numpy as np

#
# Choose each bandit uniformly
#
class EqualBandit:

    def __init__(self, treatments):
        self._treatments = treatments

    # Choose next treatment uniformly randomly
    def choose_treatment(self):
        return self._treatments[np.random.randint(low=0, high=len(self._treatments))]

    def __str__(self):
        return "EqualBandit[" + "treatment=" + self._treatment + "]"

    def __repr__(self):
        return self.__str__()
