#
# Choose same bandit every time
#
class SingleBandit:

    def __init__(self, treatments, treatment):
        self._treatments = treatments
        self._treatment = treatment

    # get next treatment string index
    def choose_treatment(self):
        return self._treatment

    def __str__(self):
        return "SingleBandit[" + "treatment=" + self._treatment + "]"

    def __repr__(self):
        return self.__str__()
