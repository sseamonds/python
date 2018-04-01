# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:05:09 2016

@author: sseamonds
"""
import numpy as np


# Choose the treatment which is currently winning
# Switch when current stops winning
class ChooseTheWinnerBandit:

    def __init__(self, treatments):
        self._treatments = treatments

    # Choose next treatment based on which is the current winner
    # results : tuple with 2 lists, one of treatments of each trial and one of result for each trial
    def choose_treatment(self, results):
        TREATMENT = 0
        RESULT = 1
        
        current_index = results[0].index('') - 1
        # default to first treatment in list
        if current_index==-1:
            return self._treatments[0]

        current_treatment = results[TREATMENT][current_index]
        current_result = results[RESULT][current_index]

        if current_result:
            return current_treatment
        else:
            # back to the beginning
            if (self._treatments.index(current_treatment)+1) >= len(self._treatments):
                return self._treatments[0]
            # choose next in line
            else:
                return self._treatments[self._treatments.index(current_treatment)+1]

    def __str__(self):
        return "ChooseTheWinnerBandit[" + "treatment=" + self._treatment + "]"

    def __repr__(self):
        return self.__str__()