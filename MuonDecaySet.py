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

    def __init__(self, **kwargs):
        
        self.dataset = []
        
        if kwargs.get('set') == True:
            
            inputDataset = kwargs.get('dataset')
            
            for row in range(length(inputDataset)):
                for col in range(length(inputDataset[row])):
                    self.dataset.append(inputDataset[row][col])
        
        else:
            self.tau = kwargs.get('tau')
            self.interval = kwargs.get('interval')
            self.size = kwargs.get('size')
        
    def generateSet(self):
        
        while len(self.dataset) < self.size:
            randomX = np.random.uniform() * self.interval
            randomY = np.random.uniform() * (1/self.tau)
            if randomY <= (1/self.tau) * (math.exp(-randomX/self.tau)):
                self.dataset.append(randomX)
        
    def getDataset(self):
        
        return(self.dataset)
        
    def writeToFile(self):
        
        datafile = open('decaytimes.txt', 'w')
        datafile.write(self.dataset)
        
    def plotHistogram(self, bins):
        
        pl.hist(self.dataset[:], bins=bins)
        pl.savefig('outputHistogram.pdf')
        pl.show()
        
