"""
    Dataset of simulated Muon decay times using the Monte Carlo technique.
    Author: Alexander S. Wheaton
    Date: 3 October 2018
    Updated: 3 October 2018
"""

class(object) MuonDecaySet(self):

    def __init__(self, tau, size):
        
        self.dataset = []
        
        self.tau = tau
        
        self.size = size
    
    def generateSet(self):
        
        for i in self.size:
            randomX = numpy.random.uniform() * self.range
            randomY = numpy.random.uniform()
            if randomY <= (1/self.tau) * (exp(-randomX/self.tau)):
                self.dataset.append(randomX)
        
    def writeToFile(self):
    
    def plotHistogram(self):
    
