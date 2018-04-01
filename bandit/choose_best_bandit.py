import numpy as np

#
# Choose the treatment which currently has the highest success rate,
# naive and greedy, serves as a baseline
#
class ChooseTheBestBandit:

    def __init__(self, treatments):
        self._treatments = treatments

    # Laplace adjustment to account for 0's
    # Allows losers to get a chance still and safe division
    @staticmethod
    def probOfWinning(wins, losses):
        return (wins + 1) / (wins + losses + 2)

    # Choose next treatment based on which is the current winner
    # results : tuple with 2 lists, one of treatments of each trial and one of
    # result for each trial
    def choose_treatment(self, results):
        TREATMENT = 0
        RESULT = 1

        # number of trials and successes from each treatment
        trials_indices_a = list(np.where(np.array(results[TREATMENT]) == 'A')[0])
        num_trials_a = len(trials_indices_a)
        num_successes_a = list(results[RESULT][i] for i in trials_indices_a).count(1)
        success_perc_a = ChooseTheBestBandit.probOfWinning(num_successes_a, (num_trials_a - num_successes_a))

        trials_indices_b = list(np.where(np.array(results[TREATMENT]) == 'B')[0])
        num_trials_b = len(trials_indices_b)
        num_successes_b = list(results[RESULT][i]
                               for i in trials_indices_b).count(1)
        success_perc_b = ChooseTheBestBandit.probOfWinning(
            num_successes_b, (num_trials_b - num_successes_b))

        if(success_perc_a > success_perc_b):
            return 'A'
        else:
            return'B'

    def __str__(self):
        return "ChooseTheBestBandit[" + "treatment=" + self._treatment + "]"

    def __repr__(self):
        return self.__str__()