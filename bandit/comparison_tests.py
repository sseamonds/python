import numpy as np

#
# Encapsulates name and conversion rate of a bandit
# scenarios : dictionary of scenarios [key=name/ values=(conversion_rate)]
#
class BanditScenario:

    def __init__(self, scenarios):
        self._scenarios = scenarios

    # given a treatment, calculate whether it's sucessful or not
    def next_result(self, treatment):
        return np.random.binomial(1, self._scenarios[treatment]['conversion_rate'])

class BanditScenarioDeterministic:
    
    def __init__(self,scenarios,flips):
        self._scenarios = scenarios
        self._flips = flips
        self._i = 0
        
    def next_result(self,treatment):
        if(self._scenarios[treatment]['conversion_rate'] > self._flips[self._i]):
            retval = 1
        else:
            retval = 0
        self._i = self._i + 1
        return retval

# Single run, multi-trial for provided bandit algorithm
# Return list of results from each trial
def multitrial_bandit(bandit_algorithm, numTrials=10, probs=[.3, .4, .5]):
    results = [0]*numTrials
    scenarios = BanditScenario({
        'A': {'conversion_rate': probs[0],},
        'B': {'conversion_rate': probs[1],}
    })

    for visitor_i in range(numTrials):
        treatment = bandit_algorithm.choose_treatment()
        results[visitor_i] = scenarios.next_result(treatment)
    return results

# for those algos which require current results to make their next decision
def multitrial_resultbased_bandit(bandit_algorithm, numTrials=10, 
                                  probs=[.3, .4, .5]):
    TREATMENT = 0
    RESULT = 1

    # results as treatment/boolean pairs
    results = (['']*numTrials, [0]*numTrials)

    scenarios = BanditScenario({
        'A': {
            'conversion_rate': probs[0],
        },
        'B': {
            'conversion_rate': probs[1],
        }
    })

    for visitor_i in range(numTrials):
        treatment = bandit_algorithm.choose_treatment(results)
        results[TREATMENT][visitor_i] = treatment
        results[RESULT][visitor_i] = scenarios.next_result(treatment)

    return results[RESULT]
    
def multitrial_result_deterministic_bandit(bandit_algorithm, 
                                           flips=np.random.uniform(0,1,10), 
                                           probs=[.4,.8]):
    TREATMENT = 0
    RESULT = 1
    numTrials = flips.shape[0]
    
    results = (['']*numTrials,[0]*numTrials)
    
    scenarios = BanditScenarioDeterministic({
        'A': {
            'conversion_rate': probs[0],
        },
        'B': {
            'conversion_rate': probs[1],
        },
    },
    flips)

    for visitor_i in range(numTrials):
        treatment = bandit_algorithm.choose_treatment(results)
        results[TREATMENT][visitor_i] = treatment
        results[RESULT][visitor_i] = scenarios.next_result(treatment)
        
    return results[RESULT]