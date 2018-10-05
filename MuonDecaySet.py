"""
    Dataset of simulated Muon decay times using the Monte Carlo technique.
    Author: Alexander S. Wheaton
    Date: 3rd October 2018
    Updated: 5th October 2018
"""
import math
import numpy as np
import matplotlib.pylab as pl

class MuonDecaySet(object):

    def __init__(self, **kwargs):
        
        """
            Either imports a dataset or initialises parameters necessary to
            generate one using the generateSet() method.
        """
        
        self.dataset = []
        
        if kwargs.get('set') == True:
            
            inputDataset = kwargs.get('dataset')
            
            for row in range(len(inputDataset)):
                for col in range(len(inputDataset[row])):
                    self.dataset.append(inputDataset[row][col])
        
        else:
            self.trueTau = kwargs.get('trueTau')
            self.interval = kwargs.get('interval')
            self.size = kwargs.get('size')
        
    def generateSet(self):
        
        """
            Generates a set of decay times from an exponential distribution
            using the box Monte Carlo method.
        """
        
        while len(self.dataset) < self.size:
            randomX = np.random.uniform() * self.interval
            randomY = np.random.uniform() * (1/self.trueTau)
            if randomY <= (1/self.trueTau) * (math.exp(-randomX/self.trueTau)):
                self.dataset.append(randomX)
        
    def writeToFile(self):
        
        """
            Exports a datafile of simulated decay times, if they exist.
        """
        
        if len(self.dataset) != 0:
            datafile = open('decaytimes.txt', 'w')
            datafile.write(str(self.dataset))
            datafile.close()
            
    def getExperimentalTau(self):
        
        return sum(self.dataset) / len(self.dataset)
        
    def getDataset(self):
        
        return(self.dataset)
        
    def plotHistogram(self, bins):
        
        pl.hist(self.dataset[:], bins=bins)
        pl.title('Frequency of Decay Events vs. Lifetime')
        pl.xlabel('Time Elapsed after Capture (s)')
        pl.ylabel('Frequency of Decay Events')
        pl.savefig('decayEventsHistogram.pdf')
        pl.show()
