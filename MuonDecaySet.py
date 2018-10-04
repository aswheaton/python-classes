"""
    Dataset of simulated Muon decay times using the Monte Carlo technique.
    Author: Alexander S. Wheaton
    Date: 3rd October 2018
    Updated: 4th October 2018
"""
import math
import numpy as np
import matplotlib.pylab as pl

class MuonDecaySet(object):

    def __init__(self, tau, interval, size):
        
        self.dataset = []
        
        self.tau = tau
        self.interval = interval
        self.size = size
        
    def generateSet(self):
        
        while len(self.dataset) < self.size:
            randomX = np.random.uniform() * self.interval
            randomY = np.random.uniform() * (1/self.tau)
            if randomY <= (1/self.tau) * (math.exp(-randomX/self.tau)):
                self.dataset.append(randomX)
        
    def printSet(self):
        
        print(self.dataset)
        
    def writeToFile(self):
        
        datafile = open('decaytimes.txt', 'w')
        datafile.write(self.dataset)
        
    def plotHistogram(self):
        
        pl.hist(self.dataset[:], bins=100)
        pl.savefig('outputHistogram.pdf')
        pl.show()
        
