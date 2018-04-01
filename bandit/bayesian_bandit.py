from numpy import random
import numpy as np

#
# Use bayesian approach to choose the next treatment
#
# Beta prior and binomial likelihood to calculate the prob 
#  of winning for each treatment
#
# See : https://www.chrisstucchio.com/blog/2013/bayesian_bandit.html
#
class BayesianBandit:
    
    def __init__(self, treatments):
        self._treatments = treatments

    #
    # Calculate beta (prior) prob for each treatments current results and
    #   select the one with the highest prob
    #
    # args:
    #   results - wins/losses for each bandit
    #
    def choose_treatment(self, results):
        TREATMENT = 0
        RESULT = 1
        
        # number of trials and successes from each treatment
        trials_indices_a = list(np.where(np.array(results[TREATMENT]) == 'A')[0])
        num_trials_a = len(trials_indices_a)
        num_successes_a = list( results[RESULT][i] for i in trials_indices_a ).count(1)
        
        trials_indices_b = list(np.where(np.array(results[TREATMENT]) == 'B')[0])
        num_trials_b = len(trials_indices_b)
        num_successes_b = list( results[RESULT][i] for i in trials_indices_b ).count(1) 
        
        return BayesianBandit.arg_max_beta(self._treatments, [num_trials_a, num_trials_b], [num_successes_a, num_successes_b])
        
    def __str__(self):
        return "BayesianBandit[" + "treatment=" + self._treatment + "]"

    def __repr__(self):
        return self.__str__()

    #
    # Calculate posterior beta for current parameters (which is the prior) for each set of trial/win counts
    # Receive list of treaments, trials for each, successes for each
    # 
    # returns: treatment associated with the max prob
    #
    @staticmethod
    def arg_max_beta(treatments, num_trials, num_successes):
        max_beta = 0
        arg_max = ''

        for i in range(len(treatments)):
            rbeta = random.beta(1 + num_successes[i], 1 + num_trials[i] - num_successes[i])

            if(rbeta >= max_beta):
                max_beta = rbeta
                arg_max = treatments[i]

        return arg_max