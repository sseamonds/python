import math
import numpy as np
import choose_best_bandit

#
# Epsilon percent of the time play the most successful bandit (so far)
# (1 - Epsilon) percent of the time give a losing bandit a chance
#
class EpsilonGreedyBandit:

    def __init__(self, treatments):
        self._treatments = treatments

    def choose_treatment(self, results):
        TREATMENT = 0
        RESULT = 1
        EPSILON = .9

        # number of trials and successes from each treatment
        trials_indices_a = list(np.where(np.array(results[TREATMENT]) == 'A')[0])
        num_trials_a = len(trials_indices_a)
        num_successes_a = list( results[RESULT][i] for i in trials_indices_a ).count(1)
        success_perc_a = choose_best_bandit.ChooseTheBestBandit.probOfWinning(num_successes_a, (num_trials_a-num_successes_a))

        trials_indices_b = list(np.where(np.array(results[TREATMENT]) == 'B')[0])
        num_trials_b = len(trials_indices_b)
        num_successes_b = list( results[RESULT][i] for i in trials_indices_b ).count(1)     
        success_perc_b = choose_best_bandit.ChooseTheBestBandit.probOfWinning(num_successes_b, (num_trials_b-num_successes_b))

        if np.random.binomial(1, (1 - EPSILON)) == 1 :
            if(success_perc_a > success_perc_b):
                return 'B'
            else:
                return 'A'
        else:
            if(success_perc_a > success_perc_b):
                return 'A'
            else:
                return 'B'
