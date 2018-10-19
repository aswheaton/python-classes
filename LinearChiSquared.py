"""
    Chi-Squared calculation for a linear data set and its errors given 
    Author: Alexander S. Wheaton
    Date: 19th October 2018
    Updated: 19th October 2018
"""

import numpy as np
from iminuit import Minuit

class LinearChiSquared(object):

    def __init__(self, filename):
        
        data = np.loadtxt(open(filename,"r"))
        
        self.x = data[:,0]
        self.y = data[:,1]
        self.e = data[:,2]
        
        self.slope = slope
        self.intercept = intercept
        
    def getChiSquared(self, slope, intercept):
        
        chiSquared = np.sum((self.y - (slope * self.x + intercept)) / 2.0)**2.0
        return chiSquared
        
    def minimisedChiSquared(self):
            
        minimisation = Minuit(self.getChiSquared, m=1, c=1, errordef = 1)
        self.minimumChiSquared, self.optParameters = minimisation.migrad()
        minimisation.minos()
        
        minimisation = m.draw_mnprofile('y')
