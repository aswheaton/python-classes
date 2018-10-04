"""
    Dataset of simulated Muon decay times using the Monte Carlo technique.
    Author: Alexander S. Wheaton
    Date: 3 October 2018
    Updated: 3 October 2018
"""

import numpy as np

class MuonDecaySet(object):

    def __init__(self, tau, interval, size):
        
        self.dataset = []
        
        self.tau = tau
        self.interval = interval
        self.size = size
        
    def generateSet(self):
        
        for i in self.size:
            randomX = np.random.uniform() * self.interval
            randomY = np.random.uniform()
            if randomY <= (1/self.tau) * (exp(-randomX/self.tau)):
                self.dataset.append(randomX)
        
    def writeToFile(self):
        
        datafile = open('decaytimes.txt', 'w')
        datafile.write(self.dataset)
        
    # def plotHistogram(self):
        
